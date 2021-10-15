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
        return {
            "artifact_name": self.artifact_name,
            "artifact_type": self.artifact_type,
            "sub_type": sub_type,
        }

    @classmethod
    def create_artifact(cls, **kwargs: str):
        name, artifact_type, sub_type = Artifact.extract_info(kwargs)
        if Artifact.verify_info(name, artifact_type, sub_type):
            return cls(name, ArtifactType[artifact_type], DataType[sub_type])
        return None

    @staticmethod
    def extract_info(**kwargs: str):
        name = kwargs.get("artifact_name", "")
        artifact_type = kwargs.get("artifact_type", "")
        sub_type = kwargs.get("sub_type", "")
        return name, artifact_type, sub_type

    @staticmethod
    def verify_info(name: str, artifact_type: str, sub_type: str):
        if (
            not name
            and artifact_type in ArtifactType.__members__
            and sub_type in DataType.__members__
        ):
            return True
        return False
