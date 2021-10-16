import asyncio
import logging
from pathlib import Path
from typing import Optional, AsyncIterator

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
from ..utils.stream import Stream

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
        self.uuid_file = storage_dir / "worker.uuid"
        if self.uuid_file.is_file():
            self.uuid = UUID(bytes=self.uuid_file.read_bytes())
            self.uuid_file.touch()

    def set_uuid(self, uuid: UUID):
        self.uuid = uuid
        self.uuid_file.write_bytes(uuid.bytes)

    @property
    def hostname(self):
        return platform.node()

    async def exchange_handshake(
        self, responses: Stream[SessionResults], events: AsyncIterator[SessionEvents]
    ):
        if self.uuid is None:
            previous_uuid = b""
        else:
            previous_uuid = self.uuid.bytes
        # Send the first request
        registration = WorkerRegistration(
            previous_uuid=previous_uuid, hostname=self.hostname
        )
        await responses.add(SessionResults(worker_registration=registration))
        # Read the first event
        first_event = await events.__anext__()
        # First event must be a worker_acceptance
        if first_event.WhichOneof("event") != "worker_acceptance":
            raise Exception("First event received was not a worker_acceptance event")
        # Preserve assigned UUID
        if self.uuid is None:
            self.set_uuid(UUID(bytes=first_event.worker_acceptance.uuid))

    async def start(self):
        async with insecure_channel(self.controller_addr) as channel:
            stub = WorkerTasksStub(channel)
            responses: Stream[SessionResults] = Stream()
            events: AsyncIterator[SessionEvents] = stub.Session(responses).__aiter__()

            try:
                await self.exchange_handshake(responses, events)
            except Exception as e:
                log.warn(e)
                return

            async for event in events:
                worker_task = event.worker_task
                log.debug(worker_task)

                await asyncio.sleep(1)

                await responses.add(
                    SessionResults(
                        worker_task_result=WorkerTaskResult(task_none=TaskNoneResult())
                    )
                )

    async def stop(self):
        pass


# vim: set et ts=4 sw=4:
