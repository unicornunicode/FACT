from fact.exceptions import (
    DirectoryExistsError,
    # StorageExistsError,
    TaskExistsError,
    TaskNotFoundError,
    TaskInvalidUUID,
    ArtifactExistsError,
    ArtifactNotFoundError,
    ArtifactInvalidName,
    ArtifactInvalidType,
    ArtifactInvalidSubType,
)
from .enumerate import ArtifactType, DataType

from pathlib import Path
from uuid import UUID
from typing import Union


class Artifact:
    """
    Stores information about an artifact
    """

    def __init__(
        self, artifact_name: str = "", artifact_type: str = "", sub_type: str = ""
    ) -> None:
        """Initialises an Artifact object

        :param artifact_name: Name of artifact
        :param artifact_type: Type of artifact
        :param sub_type: Sub type of artifact
        :raises:
            ArtifactInvalidName: Invalid name. Cannot be empty.
            ArtifactInvalidType: Invalid artifact type, needs to be found in ArtifactType
            ArtifactInvalidSubType: Invalid artifact sub type, needs to be found in DataType
        """
        if not artifact_name:
            raise ArtifactInvalidName("Invalid empty name", artifact_name)

        if not artifact_type:
            artifact_type = ArtifactType.unknown.name
        elif not Artifact.is_valid_artifact_type(artifact_type):
            valid_types = "{" + ", ".join(ArtifactType.__members__.keys()) + "}"
            err_msg = f"Invalid artifact type. Select from: {valid_types}"
            raise ArtifactInvalidType(err_msg, artifact_type)

        if not sub_type:
            sub_type = DataType.unknown.name
        elif not Artifact.is_valid_sub_type(sub_type):
            valid_types = "{" + ", ".join(DataType.__members__.keys()) + "}"
            err_msg = f"Invalid sub type. Select from: {valid_types}"
            raise ArtifactInvalidSubType(err_msg, sub_type)

        self.artifact_name = artifact_name
        self.artifact_type = ArtifactType[artifact_type]
        self.sub_type = DataType[sub_type]

    def get_artifact_type(self) -> str:
        """Gets artifact type of instance
        :return: Artifact type
        """
        return self.artifact_type.name

    def get_sub_type(self) -> str:
        """Gets artifact sub type of instance
        :return: Artifact sub type
        """
        return self.sub_type.name

    def get_artifact_path(self) -> tuple[Path, Path]:
        """Gets artifact path of instance
        :return: (Artifact path, Artifact name) ->
                 ( {artifact_type}/{sub_type}, {artifact_name} )
        """
        artifact_type = self.get_artifact_type()
        sub_type = self.get_sub_type()
        artifact_path = Path(artifact_type) / Path(sub_type)
        return artifact_path, Path(self.artifact_name)

    def get_artifact_info(self) -> dict[str, str]:
        """Gets artifact info of instance
        :return: Artifact info (Attributes of instance)
        """
        artifact_type: str = self.get_artifact_type()
        sub_type: str = self.get_sub_type()
        return {
            "artifact_name": self.artifact_name,
            "artifact_type": artifact_type,
            "sub_type": sub_type,
        }

    # @classmethod
    # def create_artifact(cls, artifact_info: dict):
    #     artifact_name, artifact_type, sub_type = Artifact.extract_info(artifact_info)
    #     if not Artifact.is_valid_artifact_name(artifact_name):
    #         raise ArtifactInvalidName("Invalid empty name", artifact_name)
    #     if not Artifact.is_valid_artifact_type(artifact_type):
    #         valid_types = "{" + ", ".join(ArtifactType.__members__.keys()) + "}"
    #         err_msg = f"Invalid artifact type. Select from: {valid_types}"
    #         raise ArtifactInvalidType(err_msg, artifact_type)
    #     if not Artifact.is_valid_sub_type(sub_type):
    #         valid_types = "{" + ", ".join(DataType.__members__.keys()) + "}"
    #         err_msg = f"Invalid sub type. Select from: {valid_types}"
    #         raise ArtifactInvalidSubType(err_msg, sub_type)
    #     return cls(artifact_name, artifact_type, sub_type)

    # @staticmethod
    # def extract_info(artifact_info: dict):
    #     name: str = artifact_info.get("artifact_name", "")
    #     artifact_type: str = artifact_info.get("artifact_type", "")
    #     sub_type: str = artifact_info.get("sub_type", "")
    #     return name, artifact_type, sub_type

    @staticmethod
    def is_valid_artifact_name(artifact_name: str) -> bool:
        """Checks if artifact name is not empty
        :param artifact_name: Name of artifact
        :return: Validation result
        """
        return bool(artifact_name)

    @staticmethod
    def is_valid_artifact_type(artifact_type: str) -> bool:
        """Checks if artifact type exists in ArtifactType
        :param artifact_type: Type of artifact
        :return: Validation result
        """
        return artifact_type in ArtifactType.__members__

    @staticmethod
    def is_valid_sub_type(sub_type: str) -> bool:
        """Checks if artifact sub type exists in DataType
        :param sub_type: Sub type of artifact
        :return: Validation result
        """
        return sub_type in DataType.__members__


class Task:
    """
    Stores information about a task
    """

    def __init__(self, task_uuid_str: str = "") -> None:
        """Initialises a Task object

        :param task_uuid_str: UUID string of task
        :raises:
            TaskInvalidUUID: Invalid task UUID
        """
        if not Task.is_valid_uuid(task_uuid_str):
            raise TaskInvalidUUID("Invalid Task UUID", task_uuid_str)
        self.task_uuid = UUID(task_uuid_str)
        self.artifacts: list[Artifact] = []

    def get_artifact(self, artifact_info: dict) -> Union[Artifact, None]:
        """Gets artifact matching the artifact info in instance

        :param artifact_info: Artifact info
        :return: The artifact matched or None
        """
        for a in self.artifacts:
            if a.get_artifact_info() == artifact_info:
                return a
        return None

    def is_artifact_exists(self, artifact_info: dict) -> bool:
        """Checks if artifact exists in instance based on artifact info

        :param artifact_info: Artifact info
        :return: Whether the artifact exists
        """
        artifact: Union[Artifact, None] = self.get_artifact(artifact_info)
        if artifact is not None:
            return True
        return False

    def add_artifact(self, artifact: Artifact) -> None:
        """Adds artifact to instance if it is does not exist already

        :param artifact: The artifact to add to instance
        :raises:
            ArtifactExistsError: Artifact exists already
        """
        artifact_info: dict = artifact.get_artifact_info()
        if self.is_artifact_exists(artifact_info):
            raise ArtifactExistsError("Artifact exists already", artifact_info)
        self.artifacts.append(artifact)

    def get_task_uuid(self) -> str:
        """Gets task UUID of instance

        :returns: Task UUID
        """
        return str(self.task_uuid)

    def get_task_path(self) -> Path:
        """Gets task path of instance

        :returns: Task path
        """
        task_uuid: str = self.get_task_uuid()
        return Path(task_uuid)

    def _get_artifacts(self) -> list[dict]:
        """Gets list of artifact info in task instance

        :returns: List of artifact info
        """
        artifacts: list[dict] = []
        for artifact in self.artifacts:
            artifacts.append(artifact.get_artifact_info())
        return artifacts

    def get_task_info(self) -> dict:
        """Gets task info of instance

        :returns: Task info (Attributes of instance)
        """
        task_uuid = self.get_task_uuid()
        artifacts = self._get_artifacts()
        return {"task_uuid": task_uuid, "artifacts": artifacts}

    # @classmethod
    # def _recreate_task(cls, task_info: dict):
    #     task_uuid_str: str = task_info.get("task_uuid", "")
    #     if not Task.is_valid_uuid(task_uuid_str):
    #         raise TaskInvalidUUID("Invalid Task UUID", task_uuid_str)
    #     task: Task = cls(task_uuid_str)

    #     artifacts: list[dict] = task_info.get("artifacts", [])
    #     for a in artifacts:
    #         artifact: Artifact = Artifact.create_artifact(a)
    #         if artifact:
    #             task.add_artifact(artifact)

    #     return task

    @staticmethod
    def is_valid_uuid(uuid_str: str) -> bool:
        """Checks if UUID string is valid
        :param uuid_str: UUID of task
        :return: Validation result
        """
        try:
            UUID(uuid_str)
        except ValueError:
            return False
        else:
            return True


class Storage:
    """
    Manages the file system and maintains a structure with
    Task and Artifact objects

    Structure:
        Storage
            |__ Task
                    |__ Artifact
                    |__ Artifact
            |__ Task
    """

    DEFAULT_PATH = Path("/var/lib/fact")

    def __init__(self, data_dir: Path = DEFAULT_PATH) -> None:
        """Initialises a Storage object

        :param data_dir: Data directory for storage
        :raises:
            DirectoryExistsError: Directory exists already
            PermissionError: Insufficient permission to create directory
        """
        if data_dir.exists():
            raise DirectoryExistsError("Directory exists already", str(data_dir))
        try:
            data_dir.mkdir(parents=True, exist_ok=False)
        except PermissionError as e:
            raise e
        self.data_dir = data_dir
        self.tasks: list[Task] = []

    def get_task(self, task_uuid: str) -> Union[Task, None]:
        """Gets task of instance matching the task UUID

        :param task_uuid: Task UUID
        :return: The task matched or None
        """
        for t in self.tasks:
            if t.get_task_uuid() == task_uuid:
                return t
        return None

    def is_task_uuid_exists(self, task_uuid: str) -> bool:
        """Checks if task exists in instance based on task UUID

        :param task_uuid: Task UUID
        :return: Whether the task exists
        """
        task: Union[Task, None] = self.get_task(task_uuid)
        if task is not None:
            return True
        return False

    def add_task(self, task: Task) -> None:
        """Adds task to instance if it is does not exist already

        :param task: The task to add to instance
        :raises:
            TaskExistsError: Task exists already
        """
        task_uuid: str = task.get_task_uuid()
        if self.is_task_uuid_exists(task_uuid):
            raise TaskExistsError("Task exists already", task.get_task_uuid())
        self.tasks.append(task)

    def add_task_artifact(self, task_uuid: str, artifact: Artifact) -> Path:
        """Adds artifact to a task that exists in instance already
        and provides path to store in file system

        :param task_uuid: UUID of task to add to instance
        :param artifact: Artifact to store in instance
        :returns: Artifact path to store in file system
        :raises:
            TaskNotFoundError: Task does not exist in instance
            PermissionError: Insufficient permission to create directory
        """
        task: Union[Task, None] = self.get_task(task_uuid)
        if task is None:
            storage_path = str(self.get_storage_path())
            raise TaskNotFoundError(
                f"Task does not exists in {storage_path}", task_uuid
            )
        task.add_artifact(artifact)

        artifact_info_path, artifact_name = artifact.get_artifact_path()
        artifact_path: Path = (
            self.get_storage_path() / task.get_task_path() / artifact_info_path
        )
        if not artifact_path.exists():
            try:
                artifact_path.mkdir(parents=True, exist_ok=True)
            except PermissionError as e:
                raise e

        artifact_full_path: Path = artifact_path / artifact_name
        return artifact_full_path

    def get_task_artifact_path(self, task_uuid: str, artifact: Artifact) -> Path:
        """Gets path to where artifact of task in instance is stored on file system

        :param task_uuid: UUID of task to add to instance
        :param artifact: Artifact to store in instance
        :returns: Artifact path where it is store on file system
        :raises:
            TaskNotFoundError: Task does not exist in instance
            ArtifactNotFoundError: Artifact does not exist in instance
        """
        task: Union[Task, None] = self.get_task(task_uuid)
        if task is None:
            storage_path = str(self.get_storage_path())
            raise TaskNotFoundError(
                f"Task does not exists in {storage_path}", task_uuid
            )
        artifact_info = artifact.get_artifact_info()
        task_artifact: Union[Artifact, None] = task.get_artifact(artifact_info)
        if task_artifact is None:
            raise ArtifactNotFoundError(
                f"Artifact does not exist in {task_uuid}", artifact_info
            )

        artifact_info_path, artifact_name = task_artifact.get_artifact_path()
        artifact_path: Path = (
            self.get_storage_path()
            / task.get_task_path()
            / artifact_info_path
            / artifact_name
        )
        return artifact_path

    def get_storage_path(self) -> Path:
        """Gets path of instance in file system

        :return: The data directory of instance
        """
        return self.data_dir

    def get_storage_info(self) -> dict:
        """Gets storage info of instance

        :returns: Storage info (Attributes of instance)
        """
        data_dir: str = str(self.get_storage_path())
        tasks = [task.get_task_info() for task in self.tasks]
        return {"data_dir": data_dir, "tasks": tasks}

    # @classmethod
    # def clone_storage(cls, storage_dict: dict, new_data_dir: Path):
    #     old_data_dir: Path = storage_dict.get("data_dir", Storage.DEFAULT_PATH)
    #     if old_data_dir == new_data_dir:
    #         raise StorageExistsError("Storage exists already", str(new_data_dir))
    #     storage: Storage = cls(new_data_dir)

    #     tasks: list[dict] = storage_dict.get("tasks", [])
    #     for t in tasks:
    #         task: Task = Task._recreate_task(t)
    #         storage.add_task(task)

    #     return storage
