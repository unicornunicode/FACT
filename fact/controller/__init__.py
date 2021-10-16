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


class WorkerTasks(WorkerTasksServicer):
    session: Session

    def __init__(self, session: Session):
        self.session = session

    async def Session(
        self, request: AsyncIterator[SessionResults], context: ServicerContext
    ) -> AsyncGenerator[SessionEvents, None]:
        # Read in the first request
        first_result: SessionResults = await request.__anext__()
        # First request must be a worker_registration
        if first_result.WhichOneof("result") != "worker_registration":
            context.abort(StatusCode.FAILED_PRECONDITION)
            return
        # Register the worker
        registration = first_result.worker_registration
        if registration.previous_uuid == b"":
            # New worker
            uuid = uuid4()
            with self.session.begin():
                worker = Worker(uuid=uuid, hostname=registration.hostname)
                self.session.add(worker)
            yield SessionEvents(worker_acceptance=WorkerAcceptance(uuid=uuid.bytes))
        else:
            # Existing worker
            uuid = UUID(bytes=registration.previous_uuid)
            with self.session.begin():
                stmt_find = select(Worker).where(Worker.uuid == uuid)
                worker_found: Optional[Worker] = self.session.execute(
                    stmt_find
                ).scalar()
                if worker_found is None:
                    log.warn("Worker connected but UUID not found")
                    return
                if worker_found.hostname != registration.hostname:
                    stmt_update_hostname = (
                        update(Worker)
                        .where(Worker.uuid == uuid)
                        .values(hostname=registration.hostname)
                    )
                    self.session.execute(stmt_update_hostname)
            yield SessionEvents(
                worker_acceptance=WorkerAcceptance(uuid=registration.previous_uuid)
            )

        while True:
            # Send request
            worker_task = WorkerTask(uuid=b"", task_none=TaskNone())
            yield SessionEvents(worker_task=worker_task)

            # Read subsequent results
            worker_task_result = await request.__anext__()
            log.debug(worker_task_result)

            await asyncio.sleep(10)


class Controller:
    """
    The Controller gets tasks from the UI and schedules them onto workers

    >>> c = Controller("localhost:5123")
    """

    listen_addr: str
    server: Server

    def __init__(self, listen_addr: str, database_addr: str):
        self.listen_addr = listen_addr
        self.server = grpc_server()
        engine = create_engine(database_addr, echo=True, future=True)
        Base.metadata.create_all(engine)
        session = Session(engine)
        # Services
        worker_tasks = WorkerTasks(session=session)
        add_WorkerTasksServicer_to_server(worker_tasks, self.server)

    async def start(self):
        log.info(f"Starting server on {self.listen_addr}")
        self.server.add_insecure_port(self.listen_addr)
        await self.server.start()
        await self.server.wait_for_termination()

    async def stop(self, grace: float):
        await self.server.stop(grace)


# vim: set et ts=4 sw=4:
