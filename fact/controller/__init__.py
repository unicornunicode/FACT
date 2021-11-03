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
    GetTargetRequest,
    GetTargetResult,
    ListTargetDiskinfoRequest,
    ListTargetDiskinfoResult,
    ListTargetDiskinfo,
    ListWorkerRequest,
    ListWorkerResult,
    ListWorker,
)
from ..tasks_pb2 import (
    Target as ProtoTarget,
    TaskCollectDisk,
    TaskCollectMemory,
    TaskCollectDiskinfo,
    TaskIngest,
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
    TargetDiskinfo,
    Task,
    TaskType,
    TaskStatus,
)
from .mappings import task_status_from_db


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
        task_type: TaskType,
        target_uuid: Optional[UUID] = None,
        task_collect_disk_device_name: Optional[str] = None,
        task_ingest_collected_uuid: Optional[UUID] = None,
    ) -> UUID:
        uuid = uuid4()
        async with self.session() as session:
            async with session.begin():
                task = Task(
                    uuid=uuid,
                    target=target_uuid,
                    type=task_type,
                    task_collect_disk_device_name=task_collect_disk_device_name,
                    task_ingest_collected_uuid=task_ingest_collected_uuid,
                )
                session.add(task)
        return uuid

    async def _list_task(self, limit: Optional[int] = None) -> Iterable[Task]:
        async with self.session() as session:
            async with session.begin():
                stmt = select(Task).order_by(Task.created_at.desc())
                if limit is not None and limit > 0:
                    stmt = stmt.limit(limit)
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

    async def _get_target(self, uuid: UUID) -> Target:
        async with self.session() as session:
            async with session.begin():
                stmt = select(Target).where(Target.uuid == uuid)
                target = (await session.execute(stmt)).scalar_one()
                session.expunge_all()
                return target

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

    async def _update_target_diskinfos(
        self, task_uuid: UUID, results: Iterable[Tuple[str, int, str, str]]
    ) -> None:
        async with self.session() as session:
            async with session.begin():
                stmt = select(Task).where(Task.uuid == task_uuid)
                task = (await session.execute(stmt)).scalar_one()
                for device_name, size, type, mountpoint in results:
                    stmt_diskinfo = select(TargetDiskinfo).where(
                        TargetDiskinfo.target == task.target,
                        TargetDiskinfo.device_name == device_name,
                    )
                    diskinfo = (
                        await session.execute(stmt_diskinfo)
                    ).scalar_one_or_none()
                    if diskinfo is not None:
                        diskinfo.size = size
                        diskinfo.type = type
                        diskinfo.mountpoint = mountpoint
                        continue
                    diskinfo = TargetDiskinfo(
                        target=task.target,
                        device_name=device_name,
                        size=size,
                        type=type,
                        mountpoint=mountpoint,
                    )
                    session.add(diskinfo)

    async def _list_target_diskinfos(self, uuid: UUID) -> Iterable[TargetDiskinfo]:
        async with self.session() as session:
            async with session.begin():
                stmt = select(TargetDiskinfo).where(
                    TargetDiskinfo.target == uuid,
                )
                diskinfos = (await session.execute(stmt)).scalars().all()
                session.expunge_all()
                return diskinfos

    async def _update_target_diskinfo_collected(self, task_uuid: UUID) -> None:
        async with self.session() as session:
            async with session.begin():
                stmt = select(Task).where(Task.uuid == task_uuid)
                task = (await session.execute(stmt)).scalar_one()
                stmt_diskinfo = select(TargetDiskinfo).where(
                    TargetDiskinfo.target == task.target,
                    TargetDiskinfo.device_name == task.task_collect_disk_device_name,
                )
                diskinfo = (await session.execute(stmt_diskinfo)).scalar_one()
                diskinfo.collected_at = datetime.utcnow()
                diskinfo.collected_uuid = task.uuid

    async def _pop_worker_next_task(self, uuid: UUID) -> Optional[Tuple[Task, Target]]:
        async with self.session() as session:
            async with session.begin():
                stmt = (
                    select(Task)
                    .where(Task.status == TaskStatus.WAITING, Task.worker == uuid)
                    .limit(1)
                )
                task = (await session.execute(stmt)).scalar_one_or_none()
                if task is None:
                    return None
                stmt_target = select(Target).where(Target.uuid == task.target)
                target = (await session.execute(stmt_target)).scalar_one()
                task.status = TaskStatus.RUNNING
                task.assigned_at = datetime.utcnow()
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
                task.completed_at = datetime.utcnow()

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
        if task_type == "task_collect_disk":
            uuid = await self.controller._create_task(
                task_type=TaskType.task_collect_disk,
                target_uuid=target_uuid,
                task_collect_disk_device_name=request.task_collect_disk.device_name,
            )
        elif task_type == "task_collect_memory":
            uuid = await self.controller._create_task(
                task_type=TaskType.task_collect_memory,
                target_uuid=target_uuid,
            )
        elif task_type == "task_collect_diskinfo":
            uuid = await self.controller._create_task(
                task_type=TaskType.task_collect_diskinfo,
                target_uuid=target_uuid,
            )
        elif task_type == "task_ingest":
            uuid = await self.controller._create_task(
                task_type=TaskType.task_ingest,
                task_ingest_collected_uuid=UUID(
                    bytes=request.task_ingest.collected_uuid
                ),
            )
        else:
            context.abort(StatusCode.INVALID_ARGUMENT)
            raise Exception(f"Unreachable: Invalid task type {task_type}")
        return CreateTaskResult(uuid=uuid.bytes)

    async def ListTask(
        self, request: ListTaskRequest, context: ServicerContext
    ) -> ListTaskResult:
        list_tasks = []
        tasks = await self.controller._list_task(limit=request.limit)
        for task in tasks:
            assert task.uuid is not None
            assert task.status is not None
            assert task.created_at is not None
            created_at = Timestamp(seconds=int(task.created_at.timestamp()))
            assigned_at = (
                Timestamp(seconds=int(task.assigned_at.timestamp()))
                if task.assigned_at is not None
                else None
            )
            completed_at = (
                Timestamp(seconds=int(task.completed_at.timestamp()))
                if task.completed_at is not None
                else None
            )
            target = task.target.bytes if task.target is not None else None
            task_collect_disk = (
                TaskCollectDisk(device_name=task.task_collect_disk_device_name)
                if task.type == TaskType.task_collect_disk
                and task.task_collect_disk_device_name is not None
                else None
            )
            task_collect_memory = (
                TaskCollectMemory()
                if task.type == TaskType.task_collect_memory
                else None
            )
            task_collect_diskinfo = (
                TaskCollectDiskinfo()
                if task.type == TaskType.task_collect_diskinfo
                else None
            )
            task_ingest = (
                TaskIngest(collected_uuid=task.task_ingest_collected_uuid.bytes)
                if task.type == TaskType.task_ingest
                and task.task_ingest_collected_uuid is not None
                else None
            )
            worker = task.worker.bytes if task.worker is not None else None
            list_tasks.append(
                ListTask(
                    uuid=task.uuid.bytes,
                    status=task_status_from_db(task.status),
                    created_at=created_at,
                    assigned_at=assigned_at,
                    completed_at=completed_at,
                    target=target,
                    task_collect_disk=task_collect_disk,
                    task_collect_memory=task_collect_memory,
                    task_collect_diskinfo=task_collect_diskinfo,
                    task_ingest=task_ingest,
                    worker=worker,
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
            assert target.uuid is not None
            list_targets.append(
                ListTarget(
                    uuid=target.uuid.bytes,
                    name=target.name or "",
                    ssh=ssh,
                )
            )
        return ListTargetResult(targets=list_targets)

    async def GetTarget(
        self, request: GetTargetRequest, context: ServicerContext
    ) -> GetTargetResult:
        target_uuid = UUID(bytes=request.uuid)
        target = await self.controller._get_target(target_uuid)
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
        return GetTargetResult(
            target=ListTarget(
                uuid=target.uuid.bytes if target.uuid is not None else None,
                name=target.name or "",
                ssh=ssh,
            )
        )

    async def ListTargetDiskinfo(
        self, request: ListTargetDiskinfoRequest, context: ServicerContext
    ) -> ListTargetDiskinfoResult:
        target_uuid = UUID(bytes=request.uuid)
        diskinfos = await self.controller._list_target_diskinfos(target_uuid)
        list_diskinfos = []
        for diskinfo in diskinfos:
            assert diskinfo.device_name is not None
            assert diskinfo.size is not None
            assert diskinfo.type is not None
            assert diskinfo.mountpoint is not None  # Empty string when no mountpoint
            collected_at = (
                Timestamp(seconds=int(diskinfo.collected_at.timestamp()))
                if diskinfo.collected_at is not None
                else None
            )
            collected_uuid = (
                diskinfo.collected_uuid.bytes
                if diskinfo.collected_uuid is not None
                else None
            )
            list_diskinfos.append(
                ListTargetDiskinfo(
                    device_name=diskinfo.device_name,
                    size=diskinfo.size,
                    type=diskinfo.type,
                    mountpoint=diskinfo.mountpoint,
                    collected_at=collected_at,
                    collected_uuid=collected_uuid,
                )
            )
        return ListTargetDiskinfoResult(diskinfos=list_diskinfos)

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

        assert task.uuid is not None
        ssh = (
            SSHAccess(
                host=target.ssh_host or "",
                user=target.ssh_user or "",
                port=target.ssh_port or 0,
                private_key=target.ssh_private_key or "",
                become=target.ssh_become or False,
                become_password=target.ssh_become_password or "",
            )
            if target.uuid is not None
            else None
        )
        task_target = (
            ProtoTarget(uuid=target.uuid.bytes, ssh=ssh)
            if target.uuid is not None
            else None
        )
        if task.type == TaskType.task_collect_disk:
            assert task.task_collect_disk_device_name is not None
            task_collect_disk = TaskCollectDisk(
                device_name=task.task_collect_disk_device_name
            )
            return WorkerTask(
                uuid=task.uuid.bytes,
                target=task_target,
                task_collect_disk=task_collect_disk,
            )
        elif task.type == TaskType.task_collect_memory:
            task_collect_memory = TaskCollectMemory()
            return WorkerTask(
                uuid=task.uuid.bytes,
                target=task_target,
                task_collect_memory=task_collect_memory,
            )
        elif task.type == TaskType.task_collect_diskinfo:
            task_collect_diskinfo = TaskCollectDiskinfo()
            return WorkerTask(
                uuid=task.uuid.bytes,
                target=task_target,
                task_collect_diskinfo=task_collect_diskinfo,
            )
        elif task.type == TaskType.task_ingest:
            assert task.task_ingest_collected_uuid is not None
            task_ingest = TaskIngest(
                collected_uuid=task.task_ingest_collected_uuid.bytes
            )
            return WorkerTask(
                uuid=task.uuid.bytes,
                task_ingest=task_ingest,
            )
        else:
            raise Exception(f"Unreachable: Invalid task type {task.type}")

    async def _complete_task(self, result: WorkerTaskResult) -> None:
        task_uuid = UUID(bytes=result.uuid)
        task_type = result.WhichOneof("task")
        if task_type == "task_collect_diskinfo":
            diskinfos = []
            for diskinfo in result.task_collect_diskinfo.diskinfos:
                diskinfos.append(
                    (
                        diskinfo.device_name,
                        diskinfo.size,
                        diskinfo.type,
                        diskinfo.mountpoint,
                    )
                )
            await self.controller._update_target_diskinfos(task_uuid, diskinfos)
        elif task_type == "task_collect_disk":
            await self.controller._update_target_diskinfo_collected(task_uuid)
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
            log.error("Failed to exchange handshake", e)
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
                log.error("Recieved an event that is not worker_task_result")
                context.abort(StatusCode.FAILED_PRECONDITION)
                return

            # Read subsequent results
            worker_task_result: WorkerTaskResult = session_result.worker_task_result
            log.debug(worker_task_result)
            await self._complete_task(worker_task_result)


# vim: set et ts=4 sw=4:
