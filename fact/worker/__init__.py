import logging
from contextlib import contextmanager
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import List, Optional, Literal, Generator, AsyncIterator

# Protocol
from grpc.aio import insecure_channel
from ..controller_pb2 import (
    SessionResults,
    SessionEvents,
    WorkerRegistration,
    WorkerAcceptance,
    WorkerTask,
    WorkerTaskResult,
)
from ..tasks_pb2 import (
    Target,
    TaskCollectDisk,
    TaskCollectDiskResult,
    TaskCollectMemory,
    TaskCollectMemoryResult,
    TaskCollectDiskinfo,
    TargetDiskinfo,
    TaskCollectDiskinfoResult,
    TaskIngest,
    TaskIngestResult,
)
from ..controller_pb2_grpc import WorkerTasksStub
from ..utils.stream import Stream

# Data
from uuid import UUID
import platform

# FACT
from fact.target import SSHTargetAccess
from fact.target.types import TargetAccess
from fact.storage import Session, Storage, Task, Artifact
from fact.ingestion import DiskAnalyzer
from fact.ingestion.destinations import DestinationElasticsearch


@contextmanager
def _storage_open(
    storage: Storage,
    task_uuid: UUID,
    artifact_name: str,
    artifact_type: Literal["disk"],
) -> Generator[Session, None, None]:
    # TODO: Move this into storage
    task = Task(str(task_uuid))
    artifact = Artifact(artifact_name, artifact_type)
    with Session(storage, task, artifact) as s:
        yield s


log = logging.getLogger(__name__)


class Worker:
    """
    The Worker gets tasks from the controller and executes them
    """

    _controller_addr: str
    _storage: Storage
    _storage_dir: Path
    _uuid_file: Path
    _uuid: Optional[UUID] = None
    _ingest_destination: Optional[DestinationElasticsearch] = None

    def __init__(self, controller_addr: str, storage_dir: Path):
        self._controller_addr = controller_addr

        # TODO: S3 storage abstraction
        self._storage = Storage(storage_dir)

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

    async def _setup(self, info: WorkerAcceptance) -> None:
        self._ingest_destination = DestinationElasticsearch(
            hosts=info.elasticsearch.hosts
        )

    def _remote(self, target: Target) -> TargetAccess:
        access_type = target.WhichOneof("access")
        if access_type == "ssh":
            return SSHTargetAccess(
                host=target.ssh.host,
                user=target.ssh.user,
                port=target.ssh.port,
                private_key=target.ssh.private_key,
            )
        else:
            raise Exception(f"Invalid remote access type {access_type}")

    async def _handle_task_obtain_diskinfo(
        self, task_uuid: UUID, target: Target, task: TaskCollectDiskinfo
    ) -> List[TargetDiskinfo]:
        remote = self._remote(target)
        try:
            diskinfo_result = remote.get_all_available_disk()
        except Exception as e:
            log.error("Failed to perform SSH", e)
            return []

        # Convert to grpc compatible version
        grpc_diskinfo_results = []
        for device_name, size, type, mountpoint in diskinfo_result:
            grpc_diskinfo_results.append(
                TargetDiskinfo(
                    device_name=device_name,
                    size=size,
                    type=type,
                    mountpoint=mountpoint,
                )
            )
        return grpc_diskinfo_results

    async def _handle_task_collect_disk(
        self, task_uuid: UUID, target: Target, task: TaskCollectDisk
    ) -> None:
        remote = self._remote(target)
        with _storage_open(self._storage, task_uuid, task.device_name, "disk") as f:
            try:
                remote.collect_image(task.device_name, f)
            except Exception as e:
                log.error("Failed to collect disk", e)

    async def _handle_task_collect_memory(
        self, task_uuid: UUID, target: Target, task: TaskCollectMemory
    ) -> None:
        log.error("Task collect_memory not implemented")

    async def _handle_task_ingest(
        self,
        task_uuid: UUID,
        task: TaskIngest,
    ) -> None:
        # Should not happen: We have already called _setup()
        assert self._ingest_destination is not None

        # HACK: Get the first artifact. We should only have one artifact per
        # task. A task is never called with multiple disks at the moment.
        s_task = self._storage.get_task(str(UUID(bytes=task.collected_uuid)))
        assert s_task is not None
        # TODO: Rewrite the storage API to avoid using dict
        s_task_info = s_task.get_task_info()
        assert s_task_info is not None
        s_artifact_info = s_task_info.get("artifacts", []).pop()
        assert s_artifact_info is not None
        s_artifact = s_task.get_artifact(s_artifact_info)
        assert s_artifact is not None
        # TODO: Rewrite the storage API to always produce writestreams, for
        # compatibility with S3 buckets
        artifact_path = self._storage.get_task_artifact_path(
            str(s_task.task_uuid), s_artifact
        )

        # Copy the file into a temporary file
        with NamedTemporaryFile("wb", suffix=".gz") as f:
            # HACK: Directly read from artifact_path since we already have it
            log.debug(str(artifact_path))
            with open(artifact_path, "rb") as artifact_f:
                while buf := artifact_f.read(65535):
                    f.write(buf)
            f.flush()

            # TODO: Read disk image from a Writable stream
            log.debug(f.name)
            with DiskAnalyzer(Path(f.name), None) as analyzer:
                for record in analyzer.analyse():
                    await self._ingest_destination.index(
                        UUID(bytes=task.collected_uuid), record
                    )

    async def _handle_worker_task(self, task: WorkerTask) -> WorkerTaskResult:
        """
        Handle one incoming worker task, returning the result
        """
        log.debug(task)
        task_type = task.WhichOneof("task")
        task_uuid = UUID(bytes=task.uuid)
        if task_type == "task_collect_disk":
            await self._handle_task_collect_disk(
                task_uuid, task.target, task.task_collect_disk
            )
            return WorkerTaskResult(
                uuid=task_uuid.bytes, task_collect_disk=TaskCollectDiskResult()
            )
        if task_type == "task_collect_memory":
            await self._handle_task_collect_memory(
                task_uuid, task.target, task.task_collect_memory
            )
            return WorkerTaskResult(
                uuid=task_uuid.bytes, task_collect_memory=TaskCollectMemoryResult()
            )
        if task_type == "task_collect_diskinfo":
            diskinfos = await self._handle_task_obtain_diskinfo(
                task_uuid, task.target, task.task_collect_diskinfo
            )
            return WorkerTaskResult(
                uuid=task_uuid.bytes,
                task_collect_diskinfo=TaskCollectDiskinfoResult(diskinfos=diskinfos),
            )
        if task_type == "task_ingest":
            await self._handle_task_ingest(task_uuid, task.task_ingest)
            return WorkerTaskResult(
                uuid=task_uuid.bytes, task_ingest=TaskIngestResult()
            )
        raise Exception("Unreachable: Invalid task type")

    async def _exchange_handshake(
        self, responses: Stream[SessionResults], events: AsyncIterator[SessionEvents]
    ) -> None:
        """
        Register this worker with the database
        """
        if self._uuid is None:
            registration = WorkerRegistration(hostname=self.hostname)
        else:
            registration = WorkerRegistration(
                previous_uuid=self._uuid.bytes, hostname=self.hostname
            )
        # Send the first request
        await responses.add(SessionResults(worker_registration=registration))
        # Read the first event
        first_event = await events.__anext__()
        # First event must be a worker_acceptance
        if first_event.WhichOneof("event") != "worker_acceptance":
            raise Exception("First event received was not a worker_acceptance event")
        # Preserve assigned UUID
        if self._uuid is None:
            self._set_uuid(UUID(bytes=first_event.worker_acceptance.uuid))
        # Perform additional setup
        await self._setup(first_event.worker_acceptance)

    async def start(self) -> None:
        async with insecure_channel(self._controller_addr) as channel:
            stub = WorkerTasksStub(channel)
            responses: Stream[SessionResults] = Stream()
            events: AsyncIterator[SessionEvents] = stub.Session(responses).__aiter__()

            try:
                await self._exchange_handshake(responses, events)
            except Exception as e:
                log.critical("Failed to exchange handshake", e)
                raise

            async for event in events:
                # For now, synchronously and sequentially handle incoming tasks
                # TODO: Handle tasks in parallel
                try:
                    result = await self._handle_worker_task(event.worker_task)
                except Exception as e:
                    log.critical("Failed to process incoming tasks", e)
                    raise
                await responses.add(SessionResults(worker_task_result=result))

    async def stop(self) -> None:
        pass


# vim: set et ts=4 sw=4:
