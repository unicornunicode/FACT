import asyncio
import logging
from pathlib import Path
from typing import Optional, AsyncIterable

# Protocol
from grpc.aio import insecure_channel
from ..controller_pb2 import (
    SessionResults,
    SessionEvents,
    WorkerRegistration,
    WorkerTaskResult,
    TaskNoneResult,
)
from ..controller_pb2_grpc import WorkerTasksStub
from ..utils.itertools import chain
from .stream import Stream

# Data
from uuid import UUID
import platform


log = logging.getLogger(__name__)


class Worker:
    controller_addr: str
    storage_dir: Path
    uuid_file: Path
    uuid: Optional[UUID] = None

    def __init__(self, controller_addr: str, storage_dir: Path):
        self.controller_addr = controller_addr
        self.storage_dir = storage_dir

        # Ensure storage_dir exists
        if not self.storage_dir.is_dir():
            self.storage_dir.mkdir(parents=True)

        # Read uuid
        self.uuid_file = storage_dir / "uuid"
        if self.uuid_file.is_file():
            self.uuid = UUID(bytes=self.uuid_file.read_bytes())
            self.uuid_file.touch()

    def write_uuid(self, uuid: UUID):
        self.uuid = uuid
        self.uuid_file.write_bytes(uuid.bytes)

    @property
    def hostname(self):
        return platform.node()

    async def start(self):
        async with insecure_channel(self.controller_addr) as channel:
            stub = WorkerTasksStub(channel)

            if self.uuid is None:
                first_result = SessionResults(
                    worker_registration=WorkerRegistration(hostname=self.hostname)
                )
            else:
                first_result = SessionResults(
                    worker_registration=WorkerRegistration(
                        uuid=self.uuid.bytes, hostname=self.hostname
                    )
                )

            response_stream: Stream[SessionResults] = Stream()
            responses: AsyncIterable[SessionResults] = chain(
                [
                    first_result,
                ],
                response_stream,
            )
            session_events: AsyncIterable[SessionEvents] = stub.Session(responses)

            first_event = await session_events.__aiter__().__anext__()
            if first_event.WhichOneof("event") != "worker_acceptance":
                return

            async for session_event in session_events:
                worker_task = session_event.worker_task
                log.debug(worker_task)

                await asyncio.sleep(1)

                await response_stream.add(
                    SessionResults(
                        worker_task_result=WorkerTaskResult(task_none=TaskNoneResult())
                    )
                )

    async def stop(self):
        pass


# vim: set et ts=4 sw=4:
