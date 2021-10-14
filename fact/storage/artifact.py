from pathlib import Path
from enum import Enum


class ArtifactType(Enum):
    unknown = 0
    disk = 1
    memory = 2


class DataType(Enum):
    unknown = 0
    full = 1
    partition = 2
    process = 3


class Artifact:
    def __init__(
        self,
        artifact_name: str,
        artifact_type: ArtifactType = ArtifactType.unknown,
        sub_type: DataType = DataType.unknown,
    ):
        self.artifact_name = artifact_name
        self.artifact_type = artifact_type
        self.sub_type = sub_type

    def get_artifact_type(self):
        return self.artifact_type.name

    def get_sub_type(self):
        return self.sub_type.name

    def get_artifact_path(self):
        artifact_type = self.get_artifact_type()
        sub_type = self.get_sub_type()
        return Path(artifact_type) / Path(sub_type) / Path(self.artifact_name)

    def get_artifact_info(self):
        sub_type = self.get_sub_type()
        return {"artifact_name": self.artifact_name, "sub_type": sub_type}


class Disk(Artifact):
    artifact_type: ArtifactType = ArtifactType.disk

    def __init__(self, artifact_name: str, sub_type: DataType = DataType.unknown):
        super().__init__(artifact_name, Disk.artifact_type, sub_type)


class Memory(Artifact):
    artifact_type: ArtifactType = ArtifactType.memory

    def __init__(self, artifact_name: str, sub_type: DataType = DataType.unknown):
        super().__init__(artifact_name, Memory.artifact_type, sub_type)
