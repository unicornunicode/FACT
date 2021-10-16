import logging
import os
import errno

from pathlib import Path
from uuid import UUID

from artifact import Artifact


class Task:
    def __init__(self, task_uuid: UUID):
        self.task_uuid = task_uuid
        self.artifacts: list[Artifact] = []

    def add_artifact(self, artifact):
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
    def _recreate_task(cls, **kwargs: str):
        task_uuid_str: str = kwargs.get("task_uuid")
        try:
            task_uuid = UUID(task_uuid_str)
        except ValueError as e:
            raise TaskInvalidUUID("Invalid Task UUID", task_uuid_str) from e
        task: Task = cls(task_uuid)

        artifacts: list[dict] = kwargs.get("artifacts")
        for a in artifacts:
            artifact: Artifact = Artifact.create_artifact(a)
            if artifact:
                task.add_artifact(artifact)

        return task


class Storage:
    DEFAULT_PATH = Path("/var/lib/fact")

    def __init__(self, data_dir: Path = DEFAULT_PATH):
        if not data_dir.exists():
            data_dir.mkdir(parents=True, exist_ok=True)
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

    def get_filesystem_info(self):
        tasks = [task.get_task_info() for task in self.tasks]
        return {"data_dir": self.data_dir, "tasks": tasks}

    @classmethod
    def clone_storage(cls, storage_dict: dict, new_data_dir: Path):
        old_data_dir: Path = storage_dict.get("data_dir", Storage.DEFAULT_PATH)
        if old_data_dir == new_data_dir:
            raise StorageExistsError("Storage exists already", new_data_dir)
        storage: Storage = cls(new_data_dir)

        tasks: list[dict[str, dict[str, list]]] = storage_dict.get("tasks", [])
        for t in tasks:
            task: Task = Task._recreate_task(t)
            storage.add_task(task)

        return storage
