import logging
import os
import errno

from pathlib import Path
from uuid import UUID

from artifact import DataType, Disk, Memory


class Task:
    def __init__(self, task_uuid: UUID):
        self.task_uuid = task_uuid
        self.disks: list[Disk] = []
        self.memories: list[Memory] = []

    def add_disk(self, disk_name: str, sub_type: DataType):
        disk = Disk(disk_name, sub_type)
        self.disks.append(disk)

    def add_memory(self, memory_name: str, sub_type: DataType):
        memory = Memory(memory_name, sub_type)
        self.memories.append(memory)

    def get_task_uuid(self):
        return str(self.task_uuid)

    def get_task_path(self):
        task_uuid: str = self.get_task_uuid()
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

    @classmethod
    def _recreate_task(cls, **kwargs: dict[str, dict[str, list]]):
        task_uuid_str: str = kwargs.get("task_uuid")
        try:
            task_uuid = UUID(task_uuid_str)
        except ValueError:
            return  # Raise custom exception
        task: Task = cls(task_uuid)

        artifacts: dict[str, list] = kwargs.get("artifacts")

        disk_artifacts: list[dict] = artifacts.get("disk")
        for d in disk_artifacts:
            d_name = d.get("artifact_name")  # Need to check for empty str
            d_sub_type_str = d.get("sub_type")
            d_sub_type = DataType[d_sub_type_str]  # Need to check val
            task.add_disk(disk_name=d_name, sub_type=d_sub_type)

        memory_artifacts: list[dict] = artifacts.get("memory")
        for m in memory_artifacts:
            m_name = m.get("artifact_name")  # Need to check for empty str
            m_sub_type_str = m.get("sub_type")
            m_sub_type = DataType[m_sub_type_str]  # Need to check val
            task.add_memory(memory_name=m_name, sub_type=m_sub_type)

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
            pass  # Raise custom exception
        self.tasks.append(task)

    def get_storage_path(self):
        return self.data_dir

    def get_filesystem_info(self):
        tasks = [task.get_task_info() for task in self.tasks]
        return {"data_dir": self.data_dir, "tasks": tasks}

    @classmethod
    def duplicate_storage(cls, storage_dict: dict, new_data_dir: Path):
        old_data_dir: Path = storage_dict.get("data_dir", Storage.DEFAULT_PATH)
        if old_data_dir == new_data_dir:
            pass  # Raise custom exception
        storage: Storage = cls(new_data_dir)

        tasks: list[dict[str, dict[str, list]]] = storage_dict.get("tasks", [])
        for t in tasks:
            task: Task = Task._recreate_task(t)
            storage.add_task(task)

        return storage
