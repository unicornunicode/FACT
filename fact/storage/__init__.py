import logging
import os
import errno

from pathlib import Path

from enum import Enum
from uuid import UUID

DEFAULT_PATH = Path("/var/lib/fact")


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


class Task:
    def __init__(self, task_uuid: UUID):
        self.task_uuid = task_uuid
        self.disks: list[Disk] = []
        self.memories: list[Memory] = []

    def get_task_uuid(self):
        return str(self.task_uuid)

    def add_disk(self, disk_name: str, artifact_type: DataType):
        disk = Disk(disk_name, artifact_type)
        self.disks.append(disk)

    def add_memory(self, disk_name: str, artifact_type: DataType):
        memory = Memory(disk_name, artifact_type)
        self.memories.append(memory)

    def get_task_path(self):
        task_uuid = self.get_task_uuid()
        return Path(task_uuid)

    def _get_artifacts(self):
        artifacts = {"disk": [], "memory": []}
        for disk in self.disks:
            artifacts["disk"].append(disk.get_artifact_info())
        for mem in self.memories:
            artifacts["memory"].append(mem.get_artifact_info())
        return artifacts

    def get_task_info(self):
        task_uuid = self.get_task_uuid()
        artifacts = self._get_artifacts()
        return {"task_uuid": task_uuid, "artifacts": artifacts}


class Storage:
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
            pass  # Raise custom exception
        self.tasks.append(task)

    def get_storage_path(self):
        return self.data_dir

    def get_filesystem_info(self):
        tasks = [task.get_task_info() for task in self.tasks]
        return {"data_dir": self.data_dir, "tasks": tasks}

    @classmethod
    def duplicate_storage_from_dict(cls, storage_dict: dict, new_data_dir: Path):
        pass
