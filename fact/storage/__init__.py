from fact.exceptions import (
    DirectoryExistsError,
    StorageExistsError,
    TaskExistsError,
    TaskInvalidUUID,
    ArtifactInvalidName,
    ArtifactInvalidType,
    ArtifactInvalidSubType,
)
from .enumerate import ArtifactType, DataType

from pathlib import Path
from uuid import UUID


class Artifact:
    def __init__(
        self, artifact_name: str = "", artifact_type: str = "", sub_type: str = ""
    ):
        if not artifact_name:
            raise ArtifactInvalidName("Invalid empty name", artifact_name)

        if not artifact_type:
            artifact_type = ArtifactType.unknown.name
        elif not Artifact.is_valid_artifact_type(artifact_type):
            err_msg = "Invalid artifact type"
            valid_types = ", ".join(ArtifactType.__members__.keys())
            err_msg += ". Select from: {" + valid_types + "}"
            raise ArtifactInvalidType(err_msg, artifact_type)

        if not sub_type:
            sub_type = DataType.unknown.name
        elif not Artifact.is_valid_sub_type(sub_type):
            err_msg = "Invalid sub type"
            valid_types = ", ".join(DataType.__members__.keys())
            err_msg += ". Select from: {" + valid_types + "}"
            raise ArtifactInvalidSubType(err_msg, sub_type)

        self.artifact_name = artifact_name
        self.artifact_type = ArtifactType[artifact_type]
        self.sub_type = DataType[sub_type]

    def get_artifact_type(self):
        return self.artifact_type.name

    def get_sub_type(self):
        return self.sub_type.name

    def get_artifact_path(self):
        artifact_type = self.get_artifact_type()
        sub_type = self.get_sub_type()
        artifact_path = Path(artifact_type) / Path(sub_type)
        if not artifact_path.exists():
            try:
                artifact_path.mkdir(parents=True, exist_ok=True)
            except PermissionError as e:
                raise e
        return artifact_path / Path(self.artifact_name)

    def get_artifact_info(self):
        sub_type = self.get_sub_type()
        return {
            "artifact_name": self.artifact_name,
            "artifact_type": self.artifact_type,
            "sub_type": sub_type,
        }

    @classmethod
    def create_artifact(cls, artifact_info: dict):
        artifact_name, artifact_type, sub_type = Artifact.extract_info(artifact_info)
        if (
            Artifact.is_valid_artifact_name(artifact_name)
            and Artifact.is_valid_artifact_type(artifact_type)
            and Artifact.is_valid_sub_type(sub_type)
        ):
            return cls(artifact_name, artifact_type, sub_type)
        return None

    @staticmethod
    def extract_info(artifact_info: dict):
        name: str = artifact_info.get("artifact_name", "")
        artifact_type: str = artifact_info.get("artifact_type", "")
        sub_type: str = artifact_info.get("sub_type", "")
        return name, artifact_type, sub_type

    @staticmethod
    def is_valid_artifact_name(artifact_name: str):
        return bool(artifact_name)

    @staticmethod
    def is_valid_artifact_type(artifact_type: str):
        return artifact_type in ArtifactType.__members__

    @staticmethod
    def is_valid_sub_type(sub_type: str):
        return sub_type in DataType.__members__


class Task:
    def __init__(self, task_uuid_str: str = ""):
        if not Task.is_valid_uuid(task_uuid_str):
            raise TaskInvalidUUID("Invalid Task UUID", task_uuid_str)
        self.task_uuid = UUID(task_uuid_str)
        self.artifacts: list[Artifact] = []

    def add_artifact(self, artifact: Artifact):
        self.artifacts.append(artifact)

    def get_task_uuid(self):
        return str(self.task_uuid)

    def get_task_path(self):
        task_uuid: str = self.get_task_uuid()
        return Path(task_uuid)

    def _get_artifacts(self):
        artifacts: list[dict] = []
        for artifact in self.artifacts:
            artifacts.append(artifact.get_artifact_info())
        return artifacts

    def get_task_info(self):
        task_uuid = self.get_task_uuid()
        artifacts = self._get_artifacts()
        return {"task_uuid": task_uuid, "artifacts": artifacts}

    @classmethod
    def _recreate_task(cls, task_info: dict):
        task_uuid_str: str = task_info.get("task_uuid", "")
        if not Task.is_valid_uuid(task_uuid_str):
            raise TaskInvalidUUID("Invalid Task UUID", task_uuid_str)
        task: Task = cls(task_uuid_str)

        artifacts: list[dict] = task_info.get("artifacts", [])
        for a in artifacts:
            artifact: Artifact = Artifact.create_artifact(a)
            if artifact:
                task.add_artifact(artifact)

        return task

    @staticmethod
    def is_valid_uuid(uuid_str: str):
        try:
            UUID(uuid_str)
        except ValueError:
            return False
        else:
            return True


class Storage:
    DEFAULT_PATH = Path("/var/lib/fact")

    def __init__(self, data_dir: Path = DEFAULT_PATH):
        if data_dir.exists():
            raise DirectoryExistsError("Directory exists already", str(data_dir))
        try:
            data_dir.mkdir(parents=True, exist_ok=False)
        except PermissionError as e:
            raise e
        self.data_dir = data_dir
        self.tasks: list[Task] = []

    def is_task_exists(self, task: Task):
        task_uuid = task.task_uuid
        for t in self.tasks:
            if t.task_uuid == task_uuid:
                return True
        return False

    def add_task(self, task: Task):
        if self.is_task_exists(task):
            raise TaskExistsError("Task exists already", task.get_task_uuid())
        self.tasks.append(task)

    def get_storage_path(self):
        return self.data_dir

    def get_storage_info(self):
        data_dir: str = str(self.get_storage_path())
        tasks = [task.get_task_info() for task in self.tasks]
        return {"data_dir": data_dir, "tasks": tasks}

    @classmethod
    def clone_storage(cls, storage_dict: dict, new_data_dir: Path):
        old_data_dir: Path = storage_dict.get("data_dir", Storage.DEFAULT_PATH)
        if old_data_dir == new_data_dir:
            raise StorageExistsError("Storage exists already", str(new_data_dir))
        storage: Storage = cls(new_data_dir)

        tasks: list[dict] = storage_dict.get("tasks", [])
        for t in tasks:
            task: Task = Task._recreate_task(t)
            storage.add_task(task)

        return storage
