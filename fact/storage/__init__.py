from .types import ArtifactType
from fact.exceptions import (
    TaskExistsError,
    TaskNotFoundError,
    TaskInvalidUUID,
    ArtifactExistsError,
    ArtifactNotFoundError,
    ArtifactInvalidName,
    ArtifactInvalidType,
)

from pathlib import Path
from uuid import UUID
from typing import BinaryIO, List, Union
import logging

log = logging.getLogger(__name__)

# TODO: Rewrite the storage API to always produce writestreams, for
# compatibility with S3 buckets


class Artifact:
    """
    Stores information about an artifact
    """

    def __init__(self, artifact_name: str = "", artifact_type: str = "") -> None:
        """Initialises an Artifact object

        :param artifact_name: Name of artifact
        :param artifact_type: Type of artifact
        :raises:
            ArtifactInvalidName: Invalid name. Cannot be empty.
            ArtifactInvalidType: Invalid artifact type, needs to be found in ArtifactType
        """
        if not artifact_name:
            raise ArtifactInvalidName("Invalid empty name", artifact_name)

        if not artifact_type:
            artifact_type = ArtifactType.unknown.name
        elif not Artifact.is_valid_artifact_type(artifact_type):
            valid_types = "{" + ", ".join(ArtifactType.__members__.keys()) + "}"
            err_msg = f"Invalid artifact type. Select from: {valid_types}"
            raise ArtifactInvalidType(err_msg, artifact_type)

        self.artifact_name = artifact_name
        self.artifact_type = ArtifactType[artifact_type]

    def get_artifact_type(self) -> str:
        """Gets artifact type of instance
        :return: Artifact type
        """
        return self.artifact_type.name

    def get_artifact_path(self) -> tuple[Path, Path]:
        """Gets artifact path of instance
        :return: (Artifact path, Artifact name) ->
                 ( {artifact_type}, {artifact_name} )
        """
        artifact_type = self.get_artifact_type()
        artifact_path = Path(artifact_type)
        return artifact_path, Path(self.artifact_name)

    def get_artifact_info(self) -> dict[str, str]:
        """Gets artifact info of instance
        :return: Artifact info (Attributes of instance)
        """
        artifact_type: str = self.get_artifact_type()
        return {"artifact_name": self.artifact_name, "artifact_type": artifact_type}

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

    def __init__(self, data_dir: Path) -> None:
        """Initialises a Storage object

        :param data_dir: Data directory for storage
        :raises:
            DirectoryExistsError: Directory exists already
            PermissionError: Insufficient permission to create directory
        """
        self.data_dir = data_dir
        self.tasks: List[Task] = []

        if self.data_dir.exists():
            log.info("Existing directory found. Attempting to restore Storage.")
            self._restore_storage()
        else:
            try:
                self.data_dir.mkdir(parents=True, exist_ok=True)
            except PermissionError as e:
                raise e

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

        artifact_type_path, artifact_name = artifact.get_artifact_path()
        artifact_path: Path = (
            self.get_storage_path() / task.get_task_path() / artifact_type_path
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

        artifact_type_path, artifact_name = task_artifact.get_artifact_path()
        artifact_path: Path = (
            self.get_storage_path()
            / task.get_task_path()
            / artifact_type_path
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

    def _restore_storage(self) -> None:
        """Restores instance from files and folders in self.data_dir"""
        file_paths = self.data_dir.rglob("*")
        for fpath in file_paths:
            pruned_fpath = fpath.relative_to(self.data_dir)
            fpath_parts = pruned_fpath.parts

            num_of_parts = len(fpath_parts)
            if num_of_parts > 3:
                log.warning(
                    f"Unknown folder structure. Skipping reconstruction of {pruned_fpath}."
                )
                continue

            try:
                task_uuid_str = fpath_parts[0]
                task = Task(task_uuid_str)
                self.add_task(task)
            except TaskInvalidUUID:
                log.warning(
                    f"Invalid task UUID: {task_uuid_str}. "
                    + f"Skipping reconstruction of {pruned_fpath}."
                )
                continue
            except TaskExistsError:
                pass

            if num_of_parts == 3:
                _, artifact_type, artifact_name = fpath_parts
                try:
                    artifact = Artifact(artifact_name, artifact_type)
                except ArtifactInvalidName:
                    log.warning(
                        f"Invalid artifact name: {artifact_name}. "
                        + f"Skipping reconstruction of {pruned_fpath}."
                    )
                    continue
                except ArtifactInvalidType:
                    log.warning(
                        f"Invalid artifact type: {artifact_type}. "
                        + f"Skipping reconstruction of {pruned_fpath}."
                    )
                    continue
                else:
                    self.add_task_artifact(task_uuid_str, artifact)


class Session:
    """Provides a session to interact with storage and manage the file system"""

    def __init__(self, storage: Storage, task: Task, artifact: Artifact):
        self.storage = storage
        self.task = task
        self.artifact = artifact
        self.file_io: BinaryIO

    def __enter__(self):
        self.setup()
        return self

    def __exit__(self, *exc):
        self.close()

    def setup(self):
        """Add self.task to self.storage and self.artifact to that task
        and open Binary IO to that artifact path."""
        try:
            self.storage.add_task(self.task)
        except TaskExistsError:
            pass
        task_uuid = self.task.get_task_uuid()
        artifact_path = self.storage.add_task_artifact(task_uuid, self.artifact)
        self.file_io = open(artifact_path, "wb")

    def write(self, data: bytes):
        """Write data to self.file_io
        :param data: Data to be written to artifact"""
        try:
            self.file_io.write(data)
        except AttributeError:
            raise

    def close(self):
        """Close self.file_io"""
        try:
            self.file_io.close()
        except AttributeError:
            raise
