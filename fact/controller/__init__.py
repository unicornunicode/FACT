import asyncio
import logging
from typing import Optional, AsyncIterator, AsyncGenerator

# Protocol
from grpc.aio import server as grpc_server, Server, ServicerContext
from grpc import StatusCode
from ..controller_pb2 import (
    SessionResults,
    SessionEvents,
    WorkerAcceptance,
    WorkerTask,
    TaskNone,
)
from ..controller_pb2_grpc import WorkerTasksServicer, add_WorkerTasksServicer_to_server

# Data
from uuid import UUID, uuid4
from sqlalchemy import create_engine, select, update
from sqlalchemy.orm import Session
from .database import Base, Worker


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
        engine = create_engine(database_addr, echo=database_echo, future=True)
        Base.metadata.create_all(engine)
        self.session = Session(engine)
        # Services
        worker_tasks = WorkerTasks(controller=self)
        add_WorkerTasksServicer_to_server(worker_tasks, self.server)

    async def _create_worker(self, uuid: UUID, hostname: str) -> None:
        with self.session.begin():
            worker = Worker(uuid=uuid, hostname=hostname)
            self.session.add(worker)

    async def _update_worker(self, uuid: UUID, hostname: str) -> None:
        with self.session.begin():
            stmt_find = select(Worker).where(Worker.uuid == uuid)
            worker_found: Optional[Worker] = self.session.execute(stmt_find).scalar()
            if worker_found is None:
                raise Exception(f"Worker with UUID {uuid} not found")
            stmt_update_hostname = (
                update(Worker).where(Worker.uuid == uuid).values(hostname=hostname)
            )
            self.session.execute(stmt_update_hostname)

    async def start(self) -> None:
        log.info(f"Starting server on {self.listen_addr}")
        self.server.add_insecure_port(self.listen_addr)
        await self.server.start()
        await self.server.wait_for_termination()

    async def stop(self, grace: float) -> None:
        await self.server.stop(grace)


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
            self.controller._create_worker(uuid, registration.hostname)
        else:
            # Existing worker
            uuid = UUID(bytes=registration.previous_uuid)
            self.controller._update_worker(uuid, registration.hostname)
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
            worker_task = WorkerTask(uuid=b"", task_none=TaskNone())
            yield SessionEvents(worker_task=worker_task)

            # Read subsequent results
            worker_task_result = await request.__anext__()
            log.debug(worker_task_result)

            await asyncio.sleep(10)


# vim: set et ts=4 sw=4:
