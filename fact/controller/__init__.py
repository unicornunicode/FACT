import asyncio
import logging
from typing import Optional, List, AsyncIterator, AsyncGenerator

# Protocol
from grpc.aio import server as grpc_server, Server, ServicerContext
from grpc import StatusCode
from ..controller_pb2 import (
    SessionResults,
    SessionEvents,
    WorkerAcceptance,
    WorkerTask,
    TaskNone,
    CreateTaskRequest,
    CreateTaskResult,
)
from ..controller_pb2_grpc import (
    WorkerTasksServicer,
    add_WorkerTasksServicer_to_server,
    ManagementServicer,
    add_ManagementServicer_to_server,
)

# Data
from uuid import UUID, uuid4
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from .database import Base, Worker, Task, TaskType, TaskStatus, CollectDiskSelectorGroup
from .mappings import collect_disk_selector_group_proto


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
        self.session = Session(engine)
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
        uuid = uuid4()
        with self.session.begin():
            task = Task(
                uuid=uuid,
                target=target_uuid,
                type=task_type,
                task_collect_disk_selector_group=task_collect_disk_selector_group,
            )
            self.session.add(task)
        return uuid

    async def _create_worker(self, uuid: UUID, hostname: str) -> None:
        with self.session.begin():
            worker = Worker(uuid=uuid, hostname=hostname)
            self.session.add(worker)

    async def _update_worker(self, uuid: UUID, hostname: str) -> None:
        with self.session.begin():
            stmt = select(Worker).where(Worker.uuid == uuid)
            worker: Worker = self.session.execute(stmt).scalar_one()
            worker.hostname = hostname

    def _assign_task_to_worker(self, workers: List[Worker], task: Task) -> bool:
        # TODO: Actually schedule across multiple workers
        if len(workers) == 0:
            return False
        task.worker = workers[0].uuid
        return True

    async def _process_incoming_tasks(self) -> None:
        assigned = False
        while True:
            with self.session.begin():
                # Find all workers
                stmt_workers = select(Worker)
                rows_workers = self.session.execute(stmt_workers).scalars()
                workers: List[Worker] = rows_workers.all()

                # Find all waiting tasks
                stmt = select(Task).where(Task.status == TaskStatus.WAITING).limit(5)
                rows = self.session.execute(stmt).scalars()
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
    ) -> Optional[CreateTaskResult]:
        try:
            target_uuid = UUID(bytes=request.target)
            task_type = request.WhichOneof("task")
            if task_type == "task_none":
                uuid = await self.controller._create_task(
                    target_uuid=target_uuid, task_type=TaskType.task_none
                )
            elif task_type == "task_collect_disk":
                selector_group = collect_disk_selector_group_proto(
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
                raise Exception("Unreachable: Invalid task type")
            return CreateTaskResult(uuid=uuid.bytes)
        except Exception as e:
            log.warn(e)
            context.abort(StatusCode.INVALID_ARGUMENT)
            return None


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
