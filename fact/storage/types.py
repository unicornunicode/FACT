from abc import abstractmethod
from uuid import UUID
from typing import Sequence, Literal, Protocol, ContextManager


ArtifactType = Literal["disk", "memory"]


class Readable(Protocol):
    @abstractmethod
    def read(self, n: int = -1) -> bytes:
        pass


class Writeable(Protocol):
    @abstractmethod
    def write(self, s: bytes) -> int:
        pass


class Storage(Protocol):
    @abstractmethod
    def reader(
        self,
        task_uuid: UUID,
        artifact_name: str,
        artifact_type: ArtifactType,
        decompress=False,
    ) -> ContextManager[Readable]:
        pass

    @abstractmethod
    def writer(
        self,
        task_uuid: UUID,
        artifact_name: str,
        artifact_type: ArtifactType,
        compressed=True,
    ) -> ContextManager[Writeable]:
        pass

    @abstractmethod
    def list_artifacts(
        self, task_uuid: UUID, artifact_type: ArtifactType
    ) -> Sequence[str]:
        pass


# vim: set et ts=4 sw=4:
