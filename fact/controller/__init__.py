import asyncio
import logging
from typing import Optional, Iterable, List, AsyncIterator, AsyncGenerator

# Protocol
from grpc.aio import server as grpc_server, Server, ServicerContext
from grpc import StatusCode
from google.protobuf.timestamp_pb2 import Timestamp
from ..controller_pb2 import (
    SessionResults,
    SessionEvents,
    WorkerAcceptance,
    WorkerTask,
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
)
from ..tasks_pb2 import (
    TaskNone,
    TaskCollectDisk,
    CollectDiskSelector,
    TaskCollectMemory,
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
from uuid import UUID, uuid4
from sqlalchemy import create_engine, select
from sqlalchemy.orm import scoped_session, sessionmaker
from .database import (
    Base,
    Worker,
    Target,
    Task,
    TaskType,
    TaskStatus,
    CollectDiskSelectorGroup,
)
from .mappings import (
    collect_disk_selector_group_from_proto,
    collect_disk_selector_group_from_db,
    task_status_from_db,
)


log = logging.getLogger(__name__)


class Controller:
    """
    The Controller gets tasks from the UI and schedules them onto workers

    >>> c = Controller("localhost:5123", "sqlite:///:memory:")
    """

    listen_addr: str
    server: Server

    def __init__(self, listen_addr: str, database_addr: str, database_echo=False):
        self.listen_addr = listen_addr
        self.server = grpc_server()
        # Database
        # TODO: Switch to async_engine when there is sqlite support
        engine = create_engine(database_addr, echo=database_echo, future=True)
        Base.metadata.create_all(engine)
        self.session = scoped_session(sessionmaker(bind=engine))
        # Services
        worker_tasks = WorkerTasks(controller=self)
        add_WorkerTasksServicer_to_server(worker_tasks, self.server)
        management = Management(controller=self)
        add_ManagementServicer_to_server(management, self.server)

    async def _create_task(
        self,
        target_uuid: UUID,
        task_type: TaskType,
        task_collect_disk_selector_group: Optional[CollectDiskSelectorGroup] = None,
    ) -> UUID:
        session = self.session()
        uuid = uuid4()
        with session.begin():
            task = Task(
                uuid=uuid,
                target=target_uuid,
                type=task_type,
                task_collect_disk_selector_group=task_collect_disk_selector_group,
            )
            session.add(task)
        return uuid

    async def _list_task(self) -> Iterable[Task]:
        session = self.session()
        with session.begin():
            stmt = select(Task)
            return session.execute(stmt).scalars().all()

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
        session = self.session()
        uuid = uuid4()
        with session.begin():
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
        session = self.session()
        with session.begin():
            stmt = select(Target)
            return session.execute(stmt).scalars().all()

    async def _list_worker(self) -> Iterable[Worker]:
        session = self.session()
        with session.begin():
            stmt = select(Worker)
            return session.execute(stmt).scalars().all()

    async def _create_worker(self, uuid: UUID, hostname: str) -> None:
        session = self.session()
        with session.begin():
            worker = Worker(uuid=uuid, hostname=hostname)
            session.add(worker)

    async def _update_worker(self, uuid: UUID, hostname: str) -> None:
        session = self.session()
        with session.begin():
            stmt = select(Worker).where(Worker.uuid == uuid)
            worker: Worker = session.execute(stmt).scalar_one()
            worker.hostname = hostname

    def _assign_task_to_worker(self, workers: List[Worker], task: Task) -> bool:
        # TODO: Actually schedule across multiple workers
        if len(workers) == 0:
            return False
        task.worker = workers[0].uuid
        return True

    async def _process_incoming_tasks(self) -> None:
        session = self.session()
        assigned = False
        while True:
            with session.begin():
                # Find all workers
                stmt_workers = select(Worker)
                rows_workers = session.execute(stmt_workers).scalars()
                workers: List[Worker] = rows_workers.all()

                # Find all waiting tasks
                stmt = select(Task).where(Task.status == TaskStatus.WAITING).limit(5)
                rows = session.execute(stmt).scalars()
                tasks: List[Task] = rows.all()

                assigned = False
                for task in tasks:
                    assigned = self._assign_task_to_worker(workers, task)

            if not assigned:
                await asyncio.sleep(10)

    async def start(self) -> None:
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
            selector_group = collect_disk_selector_group_from_proto(
                request.task_collect_disk.selector.group
            )
            uuid = await self.controller._create_task(
                target_uuid=target_uuid,
                task_type=TaskType.task_none,
                task_collect_disk_selector_group=selector_group,
            )
        elif task_type == "task_collect_memory":
            uuid = await self.controller._create_task(
                target_uuid=target_uuid, task_type=TaskType.task_none
            )
        else:
            context.abort(StatusCode.INVALID_ARGUMENT)
            raise Exception("Unreachable: Invalid task type")
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
                        group=collect_disk_selector_group_from_db(
                            task.task_collect_disk_selector_group
                        )
                    )
                )
                if task.type == TaskType.task_collect_disk
                and task.task_collect_disk_selector_group is not None
                else None
            )
            task_collect_memory = (
                TaskCollectMemory()
                if task.type == TaskType.task_collect_memory
                else None
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
            raise Exception("Unreachable: Invalid task type")
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

    async def Session(
        self, request: AsyncIterator[SessionResults], context: ServicerContext
    ) -> AsyncGenerator[SessionEvents, None]:
        try:
            async for response in self._exchange_handshake(request):
                yield response
        except Exception as e:
            log.warn(e)
            context.abort(StatusCode.FAILED_PRECONDITION)
            return

        while True:
            # Send request
            worker_task = WorkerTask(uuid=uuid4().bytes, task_none=TaskNone())
            yield SessionEvents(worker_task=worker_task)

            # Read subsequent results
            worker_task_result = await request.__anext__()
            log.debug(worker_task_result)

            await asyncio.sleep(1_000)


# vim: set et ts=4 sw=4:
