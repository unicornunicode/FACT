import logging
from uuid import UUID
from pathlib import Path
from contextlib import contextmanager
from typing import Generator, Sequence

from .types import Storage, ArtifactType, Readable, Writeable
from ..exceptions import (
    ArtifactExistsError,
    ArtifactNotFoundError,
)

log = logging.getLogger(__name__)

# TODO: Rewrite the storage API to always produce writestreams, for
# compatibility with S3 buckets


class FilesystemStorage(Storage):
    _directory: Path

    def __init__(self, directory: Path):
        self._directory = directory

    def _get_path(
        self, task_uuid: UUID, artifact_name: str, artifact_type: ArtifactType
    ) -> Path:
        return self._directory / str(task_uuid) / artifact_type / artifact_name

    @contextmanager
    def reader(
        self,
        task_uuid: UUID,
        artifact_name: str,
        artifact_type: ArtifactType,
        decompress: bool = True,
    ) -> Generator[Readable, None, None]:
        path = self._get_path(task_uuid, artifact_name, artifact_type)
        if not path.exists():
            raise ArtifactNotFoundError(task_uuid, artifact_name, artifact_type)

        with open(path, "rb") as f:
            if decompress:
                yield self.wrap_decompress(f)
            else:
                yield f

    @contextmanager
    def writer(
        self,
        task_uuid: UUID,
        artifact_name: str,
        artifact_type: ArtifactType,
        compressed: bool = False,
    ) -> Generator[Writeable, None, None]:
        path = self._get_path(task_uuid, artifact_name, artifact_type)
        if path.exists():
            raise ArtifactExistsError(task_uuid, artifact_name, artifact_type)

        # Create parent directories
        for parent in reversed(path.parents):
            if parent.exists():
                continue
            parent.mkdir()

        with open(path, "wb") as f:
            if not compressed:
                yield self.wrap_compress(f)
            else:
                yield f

    def list_artifacts(
        self, task_uuid: UUID, artifact_type: ArtifactType
    ) -> Sequence[str]:
        path = self._directory / str(task_uuid) / artifact_type
        artifacts = []
        for artifact in path.iterdir():
            artifacts.append(artifact.name)
        return artifacts

    def wrap_decompress(self, r: Readable) -> Readable:
        raise NotImplementedError

    def wrap_compress(self, w: Writeable) -> Writeable:
        raise NotImplementedError


# vim: set et ts=4 sw=4:
