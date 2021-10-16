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
    WorkerTask,
    WorkerTaskResult,
    TaskNoneResult,
    TaskCollectDisk,
    TaskCollectDiskResult,
    TaskCollectMemory,
    TaskCollectMemoryResult,
)
from ..controller_pb2_grpc import WorkerTasksStub
from ..utils.stream import Stream

# Data
from uuid import UUID
import platform


log = logging.getLogger(__name__)


class Worker:
    """
    The Worker gets tasks from the controller and executes them
    """

    _controller_addr: str
    _storage_dir: Path
    _uuid_file: Path
    _uuid: Optional[UUID] = None

    def __init__(self, controller_addr: str, storage_dir: Path):
        self._controller_addr = controller_addr

        self._storage_dir = storage_dir
        self._ensure_storage_dir()

        self._uuid_file = self._storage_dir / "worker.uuid"
        self._load_uuid()

    def _ensure_storage_dir(self) -> None:
        """
        Ensure storage_dir exists
        """
        if not self._storage_dir.is_dir():
            self._storage_dir.mkdir(parents=True)

    def _load_uuid(self) -> None:
        """
        Load and return the worker UUID
        """
        if self._uuid_file.is_file():
            self._uuid = UUID(bytes=self._uuid_file.read_bytes())
            self._uuid_file.touch()

    def _set_uuid(self, uuid: UUID) -> None:
        """
        Set and save the worker UUID
        """
        self._uuid = uuid
        self._uuid_file.write_bytes(uuid.bytes)

    @property
    def hostname(self) -> str:
        """
        The current machine hostname
        """
        return platform.node()

    async def _handle_task_collect_disk(
        self, task_uuid: UUID, task: TaskCollectDisk
    ) -> None:
        log.error("Task collect_disk not implemented")

    async def _handle_task_collect_memory(
        self, task_uuid: UUID, task: TaskCollectMemory
    ) -> None:
        log.error("Task collect_memory not implemented")

    async def _handle_worker_task(self, task: WorkerTask) -> WorkerTaskResult:
        """
        Handle one incoming worker task, returning the result
        """
        log.debug(task)
        task_type = task.WhichOneof("task")
        task_uuid = UUID(bytes=task.uuid)
        if task_type == "task_none":
            await asyncio.sleep(1)
            return WorkerTaskResult(uuid=task_uuid.bytes, task_none=TaskNoneResult())
        if task_type == "task_collect_disk":
            await self._handle_task_collect_disk(task_uuid, task.task_collect_disk)
            return WorkerTaskResult(
                uuid=task_uuid.bytes, task_collect_disk=TaskCollectDiskResult()
            )
        if task_type == "task_collect_memory":
            await self._handle_task_collect_memory(task_uuid, task.task_collect_memory)
            return WorkerTaskResult(
                uuid=task_uuid.bytes, task_collect_memory=TaskCollectMemoryResult()
            )
        raise Exception("Unreachable: Invalid task type")

    async def _exchange_handshake(
        self, responses: Stream[SessionResults], events: AsyncIterator[SessionEvents]
    ) -> None:
        """
        Register this worker with the database
        """
        if self._uuid is None:
            previous_uuid = b""
        else:
            previous_uuid = self._uuid.bytes
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
        if self._uuid is None:
            self._set_uuid(UUID(bytes=first_event.worker_acceptance.uuid))

    async def start(self) -> None:
        async with insecure_channel(self._controller_addr) as channel:
            stub = WorkerTasksStub(channel)
            responses: Stream[SessionResults] = Stream()
            events: AsyncIterator[SessionEvents] = stub.Session(responses).__aiter__()

            try:
                await self._exchange_handshake(responses, events)
            except Exception as e:
                log.warn(e)
                return

            async for event in events:
                # For now, synchronously and sequentially handle incoming tasks
                # TODO: Handle tasks in parallel
                try:
                    result = await self._handle_worker_task(event.worker_task)
                except Exception as e:
                    log.warn(e)
                    return
                await responses.add(SessionResults(worker_task_result=result))

    async def stop(self) -> None:
        pass


# vim: set et ts=4 sw=4:
