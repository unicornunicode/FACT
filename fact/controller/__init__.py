import asyncio
import logging
from typing import Optional, Iterable, List, Tuple, AsyncIterator, AsyncGenerator

# Protocol
from grpc.aio import server as grpc_server, Server, ServicerContext
from grpc import StatusCode
from google.protobuf.timestamp_pb2 import Timestamp
from ..controller_pb2 import (
    SessionResults,
    SessionEvents,
    WorkerAcceptance,
    WorkerTask,
    WorkerTaskResult,
)
from ..management_pb2 import (
    CreateTaskRequest,
    CreateTaskResult,
    ListTaskRequest,
    ListTaskResult,
    ListTask,
    CreateTargetRequest,
    CreateTargetResult,
    ListTargetRequest,
    ListTargetResult,
    ListTarget,
    ListWorkerRequest,
    ListWorkerResult,
    ListWorker,
)
from ..tasks_pb2 import (
    Target as ProtoTarget,
    TaskNone,
    TaskCollectDisk,
    CollectDiskSelector,
    TaskCollectMemory,
    TaskCollectLsblk,
    SSHAccess,
)
from ..controller_pb2_grpc import (
    WorkerTasksServicer,
    add_WorkerTasksServicer_to_server,
)
from ..management_pb2_grpc import (
    ManagementServicer,
    add_ManagementServicer_to_server,
)

# Data
from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from .database import (
    Base,
    Worker,
    Target,
    TargetLsblkResult,
    Task,
    TaskType,
    TaskStatus,
)
from .mappings import (
    task_status_from_db,
)


log = logging.getLogger(__name__)
logging.getLogger("aiosqlite").setLevel(logging.WARN)


class Controller:
    """
    The Controller gets tasks from the UI and schedules them onto workers

    >>> c = Controller("localhost:5123", "sqlite+aiosqlite:///:memory:")
    """

    listen_addr: str
    server: Server

    def __init__(self, listen_addr: str, database_addr: str, database_echo=False):
        self.listen_addr = listen_addr
        self.server = grpc_server()
        # Database
        # TODO: Switch to async_engine when there is sqlite support
        engine = create_async_engine(database_addr, echo=database_echo, future=True)
        self.engine = engine
        self.session = sessionmaker(engine, class_=AsyncSession)
        # Services
        worker_tasks = WorkerTasks(controller=self)
        add_WorkerTasksServicer_to_server(worker_tasks, self.server)
        management = Management(controller=self)
        add_ManagementServicer_to_server(management, self.server)

    async def setup(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def _create_task(
        self,
        target_uuid: UUID,
        task_type: TaskType,
        task_collect_disk_selector_path: Optional[str] = None,
    ) -> UUID:
        uuid = uuid4()
        async with self.session() as session:
            async with session.begin():
                task = Task(
                    uuid=uuid,
                    target=target_uuid,
                    type=task_type,
                    task_collect_disk_selector_path=task_collect_disk_selector_path,
                )
                session.add(task)
        return uuid

    async def _list_task(self) -> Iterable[Task]:
        async with self.session() as session:
            async with session.begin():
                stmt = select(Task)
                tasks = (await session.execute(stmt)).scalars().all()
                session.expunge_all()
                return tasks

    async def _create_target(
        self,
        name: str,
        ssh_host: Optional[str] = None,
        ssh_user: Optional[str] = None,
        ssh_port: Optional[int] = None,
        ssh_private_key: Optional[str] = None,
        ssh_become: Optional[bool] = None,
        ssh_become_password: Optional[str] = None,
    ) -> UUID:
        uuid = uuid4()
        async with self.session() as session:
            async with session.begin():
                target = Target(
                    uuid=uuid,
                    name=name,
                    ssh_host=ssh_host,
                    ssh_user=ssh_user,
                    ssh_port=ssh_port,
                    ssh_private_key=ssh_private_key,
                    ssh_become=ssh_become,
                    ssh_become_password=ssh_become_password,
                )
                session.add(target)
        return uuid

    async def _list_target(self) -> Iterable[Target]:
        async with self.session() as session:
            async with session.begin():
                stmt = select(Target)
                targets = (await session.execute(stmt)).scalars().all()
                session.expunge_all()
                return targets

    async def _list_worker(self) -> Iterable[Worker]:
        async with self.session() as session:
            async with session.begin():
                stmt = select(Worker)
                workers = (await session.execute(stmt)).scalars().all()
                session.expunge_all()
                return workers

    async def _create_worker(self, uuid: UUID, hostname: str) -> None:
        async with self.session() as session:
            async with session.begin():
                worker = Worker(uuid=uuid, hostname=hostname)
                session.add(worker)

    async def _update_worker(self, uuid: UUID, hostname: str) -> None:
        async with self.session() as session:
            async with session.begin():
                stmt = select(Worker).where(Worker.uuid == uuid)
                worker: Worker = (await session.execute(stmt)).scalar_one()
                worker.hostname = hostname

    async def _update_target_lsblk_results(
        self, task_uuid: UUID, results: Iterable[Tuple[str, int, str, str]]
    ) -> None:
        async with self.session() as session:
            async with session.begin():
                stmt = select(Task).where(
                    Task.status == TaskStatus.RUNNING, Task.uuid == task_uuid
                )
                task = (await session.execute(stmt)).scalar_one()
                for device_name, size, type, mountpoint in results:
                    stmt_lsblk_result = select(TargetLsblkResult).where(
                        TargetLsblkResult.target == task.target,
                        TargetLsblkResult.device_name == device_name,
                    )
                    lsblk_result = (
                        await session.execute(stmt_lsblk_result)
                    ).scalar_one_or_none()
                    if lsblk_result is not None:
                        task.size = size
                        task.type = type
                        task.mountpoint = mountpoint
                        continue
                    lsblk_result = TargetLsblkResult(
                        target=task.target,
                        device_name=device_name,
                        size=size,
                        type=type,
                        mountpoint=mountpoint,
                    )
                    session.add(lsblk_result)

    async def _pop_worker_next_task(self, uuid: UUID) -> Optional[Tuple[Task, Target]]:
        async with self.session() as session:
            async with session.begin():
                stmt = select(Task).where(
                    Task.status == TaskStatus.WAITING, Task.worker == uuid
                )
                task = (await session.execute(stmt)).scalar_one_or_none()
                if task is None:
                    return None
                stmt_target = select(Target).where(Target.uuid == task.target)
                target = (await session.execute(stmt_target)).scalar_one()
                task.status = TaskStatus.RUNNING
                task.assignedAt = datetime.utcnow()
                await session.flush()  # TODO: Is this necessary?
                session.expunge_all()
                return task, target

    async def _complete_task(self, uuid: UUID) -> None:
        async with self.session() as session:
            async with session.begin():
                stmt = select(Task).where(
                    Task.status == TaskStatus.RUNNING, Task.uuid == uuid
                )
                task = (await session.execute(stmt)).scalar_one()
                task.status = TaskStatus.COMPLETE

    def _assign_task_to_worker(self, workers: List[Worker], task: Task) -> bool:
        # TODO: Actually schedule across multiple workers
        if len(workers) == 0:
            return False
        task.worker = workers[0].uuid
        return True

    async def _process_incoming_tasks(self) -> None:
        async with self.session() as session:
            assigned = False
            while True:
                async with session.begin():
                    # Find all workers
                    stmt_workers = select(Worker)
                    rows_workers = (await session.execute(stmt_workers)).scalars()
                    workers: List[Worker] = rows_workers.all()

                    # Find all waiting tasks
                    stmt = (
                        select(Task).where(Task.worker == None).limit(5)  # noqa: E711
                    )
                    rows = (await session.execute(stmt)).scalars()
                    tasks: List[Task] = rows.all()

                    assigned = False
                    for task in tasks:
                        assigned = self._assign_task_to_worker(workers, task)

                if not assigned:
                    await asyncio.sleep(10)

    async def start(self) -> None:
        log.info("Initializing database")
        await self.setup()
        log.info(f"Starting server on {self.listen_addr}")
        self.server.add_insecure_port(self.listen_addr)
        await self.server.start()
        tasks = [
            asyncio.create_task(t)
            for t in (
                self.server.wait_for_termination(),
                self._process_incoming_tasks(),
            )
        ]
        await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    async def stop(self, grace: float) -> None:
        await self.server.stop(grace)


class Management(ManagementServicer):
    controller: Controller

    def __init__(self, controller: Controller):
        self.controller = controller

    async def CreateTask(
        self, request: CreateTaskRequest, context: ServicerContext
    ) -> CreateTaskResult:
        target_uuid = UUID(bytes=request.target)
        task_type = request.WhichOneof("task")
        if task_type == "task_none":
            uuid = await self.controller._create_task(
                target_uuid=target_uuid, task_type=TaskType.task_none
            )
        elif task_type == "task_collect_disk":
            uuid = await self.controller._create_task(
                target_uuid=target_uuid,
                task_type=TaskType.task_collect_disk,
                task_collect_disk_selector_path=request.task_collect_disk.selector.path,
            )
        elif task_type == "task_collect_memory":
            uuid = await self.controller._create_task(
                target_uuid=target_uuid, task_type=TaskType.task_collect_memory
            )
        elif task_type == "task_collect_lsblk":
            uuid = await self.controller._create_task(
                target_uuid=target_uuid, task_type=TaskType.task_collect_lsblk
            )
        else:
            context.abort(StatusCode.INVALID_ARGUMENT)
            raise Exception(f"Unreachable: Invalid task type {task_type}")
        return CreateTaskResult(uuid=uuid.bytes)

    async def ListTask(
        self, request: ListTaskRequest, context: ServicerContext
    ) -> ListTaskResult:
        list_tasks = []
        tasks = await self.controller._list_task()
        for task in tasks:
            task_none = TaskNone() if task.type == TaskType.task_none else None
            task_collect_disk = (
                TaskCollectDisk(
                    selector=CollectDiskSelector(
                        path=task.task_collect_disk_selector_path
                    )
                )
                if task.type == TaskType.task_collect_disk
                and task.task_collect_disk_selector_path is not None
                else None
            )
            task_collect_memory = (
                TaskCollectMemory()
                if task.type == TaskType.task_collect_memory
                else None
            )
            task_collect_lsblk = (
                TaskCollectLsblk() if task.type == TaskType.task_collect_lsblk else None
            )
            list_tasks.append(
                ListTask(
                    uuid=task.uuid.bytes if task.uuid is not None else None,
                    status=task_status_from_db(task.status)
                    if task.status is not None
                    else ListTask.Status.WAITING,
                    created_at=Timestamp(seconds=int(task.created_at.timestamp()))
                    if task.created_at is not None
                    else None,
                    assigned_at=Timestamp(seconds=int(task.assigned_at.timestamp()))
                    if task.assigned_at is not None
                    else None,
                    completed_at=Timestamp(seconds=int(task.completed_at.timestamp()))
                    if task.completed_at is not None
                    else None,
                    target=task.target.bytes if task.target is not None else None,
                    task_none=task_none,
                    task_collect_disk=task_collect_disk,
                    task_collect_memory=task_collect_memory,
                    task_collect_lsblk=task_collect_lsblk,
                    worker=task.worker.bytes if task.worker is not None else None,
                )
            )
        return ListTaskResult(tasks=list_tasks)

    async def CreateTarget(
        self, request: CreateTargetRequest, context: ServicerContext
    ) -> CreateTargetResult:
        target_type = request.WhichOneof("access")
        if target_type == "ssh":
            uuid = await self.controller._create_target(
                name=request.name,
                ssh_host=request.ssh.host,
                ssh_user=request.ssh.user,
                ssh_port=request.ssh.port,
                ssh_private_key=request.ssh.private_key,
                ssh_become=request.ssh.become,
                ssh_become_password=request.ssh.become_password,
            )
        else:
            context.abort(StatusCode.INVALID_ARGUMENT)
            raise Exception(f"Unreachable: Invalid target type {target_type}")
        return CreateTargetResult(uuid=uuid.bytes)

    async def ListTarget(
        self, request: ListTargetRequest, context: ServicerContext
    ) -> ListTargetResult:
        list_targets = []
        targets = await self.controller._list_target()
        for target in targets:
            ssh = None
            if target.ssh_host is not None:
                ssh = SSHAccess(
                    host=target.ssh_host or "",
                    user=target.ssh_user or "",
                    port=target.ssh_port or 0,
                    private_key=target.ssh_private_key or "",
                    become=target.ssh_become or False,
                    become_password=target.ssh_become_password or "",
                )
            list_targets.append(
                ListTarget(
                    uuid=target.uuid.bytes if target.uuid is not None else None,
                    name=target.name or "",
                    ssh=ssh,
                )
            )
        return ListTargetResult(targets=list_targets)

    async def ListWorker(
        self, request: ListWorkerRequest, context: ServicerContext
    ) -> ListWorkerResult:
        list_workers = []
        workers = await self.controller._list_worker()
        for worker in workers:
            list_workers.append(
                ListWorker(
                    uuid=worker.uuid.bytes if worker.uuid is not None else None,
                    hostname=worker.hostname or "",
                )
            )
        return ListWorkerResult(workers=list_workers)


class WorkerTasks(WorkerTasksServicer):
    controller: Controller

    def __init__(self, controller: Controller):
        self.controller = controller

    async def _exchange_handshake(
        self, results: AsyncIterator[SessionResults]
    ) -> AsyncGenerator[SessionEvents, None]:
        # Read in the first request
        first_result: SessionResults = await results.__anext__()
        # First request must be a worker_registration
        if first_result.WhichOneof("result") != "worker_registration":
            raise Exception(
                "First result received was not a worker_registration result"
            )
        # Register the worker
        registration = first_result.worker_registration
        if registration.previous_uuid == b"":
            # New worker
            uuid = uuid4()
            await self.controller._create_worker(uuid, registration.hostname)
        else:
            # Existing worker
            uuid = UUID(bytes=registration.previous_uuid)
            await self.controller._update_worker(uuid, registration.hostname)
        yield SessionEvents(worker_acceptance=WorkerAcceptance(uuid=uuid.bytes))

    async def _pop_task(self, worker_uuid: UUID) -> Optional[WorkerTask]:
        next_task = await self.controller._pop_worker_next_task(worker_uuid)
        if next_task is None:
            return None
        task, target = next_task

        ssh = SSHAccess(
            host=target.ssh_host or "",
            user=target.ssh_user or "",
            port=target.ssh_port or 0,
            private_key=target.ssh_private_key or "",
            become=target.ssh_become or False,
            become_password=target.ssh_become_password or "",
        )
        task_target = ProtoTarget(
            uuid=target.uuid.bytes if target.uuid is not None else None, ssh=ssh
        )
        if task.type == TaskType.task_collect_disk:
            task_collect_disk = TaskCollectDisk(
                selector=CollectDiskSelector(
                    path=task.task_collect_disk_selector_path
                    if task.task_collect_disk_selector_path is not None
                    else ""
                )
            )
            return WorkerTask(
                uuid=task.uuid.bytes if task.uuid is not None else None,
                target=task_target,
                task_collect_disk=task_collect_disk,
            )
        elif task.type == TaskType.task_collect_memory:
            task_collect_memory = TaskCollectMemory()
            return WorkerTask(
                uuid=task.uuid.bytes if task.uuid is not None else None,
                target=task_target,
                task_collect_memory=task_collect_memory,
            )
        elif task.type == TaskType.task_collect_lsblk:
            task_collect_lsblk = TaskCollectLsblk()
            return WorkerTask(
                uuid=task.uuid.bytes if task.uuid is not None else None,
                target=task_target,
                task_collect_lsblk=task_collect_lsblk,
            )
        elif task.type == TaskType.task_none:
            return WorkerTask(
                uuid=task.uuid.bytes if task.uuid is not None else None,
                task_none=TaskNone(),
            )
        else:
            raise Exception(f"Unreachable: Invalid task type {task.type}")

    async def _complete_task(self, result: WorkerTaskResult) -> None:
        task_uuid = UUID(bytes=result.uuid)
        task_type = result.WhichOneof("task")
        if task_type == "task_collect_lsblk":
            lsblk_results = []
            for lsblk_result in result.task_collect_lsblk.lsblk_results:
                lsblk_results.append(
                    (
                        lsblk_result.device_name,
                        lsblk_result.size,
                        lsblk_result.type,
                        lsblk_result.mountpoint,
                    )
                )
            await self.controller._update_target_lsblk_results(task_uuid, lsblk_results)
        await self.controller._complete_task(task_uuid)

    async def Session(
        self, request: AsyncIterator[SessionResults], context: ServicerContext
    ) -> AsyncGenerator[SessionEvents, None]:
        uuid: UUID
        try:
            async for response in self._exchange_handshake(request):
                # For now, read UUID from the response
                uuid = UUID(bytes=response.worker_acceptance.uuid)
                yield response
        except Exception as e:
            log.error(f"failed to exchange handshake: {e}")
            context.abort(StatusCode.FAILED_PRECONDITION)
            return

        while True:
            # Grab task off queue
            worker_task = await self._pop_task(uuid)
            if worker_task is None:
                await asyncio.sleep(10)
                continue

            # Send request
            yield SessionEvents(worker_task=worker_task)

            session_result: SessionResults = await request.__anext__()
            if session_result.WhichOneof("result") != "worker_task_result":
                log.error("recieved an event that is not worker_task_result")
                context.abort(StatusCode.FAILED_PRECONDITION)
                return

            # Read subsequent results
            worker_task_result: WorkerTaskResult = session_result.worker_task_result
            log.debug(worker_task_result)
            await self._complete_task(worker_task_result)


# vim: set et ts=4 sw=4:
