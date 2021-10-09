import logging

from pathlib import Path
from shutil import copy
import os
import errno

from enum import Enum
from uuid import UUID
from time import time

DEFAULT_PATH = Path("/var/lib/fact")

class DataType(Enum):
    full = 1
    partition = 2
    process = 3


class Artifact:
    def __init__(self, src_path: Path, dst_path: Path, file_type: DataType):
        self.file_name = dst_path.name
        self.file_type = file_type
        Artifact.write_to_fs(src_path, dst_path)

    @staticmethod
    def write_to_fs(src_path: Path, dst_path: Path):
        if not src_path.exists():
            raise OSError(errno.ENOENT, os.strerror(errno.ENOENT), src_path.resolve())
        copy(src_path, dst_path)


class Disk(Artifact):
    def __init__(self, src_path: Path, dst_path: Path, file_type: DataType):
        super().__init__(src_path, dst_path, file_type)


class Memory(Artifact):
    def __init__(self, src_path: Path, dst_path: Path, file_type: DataType):
        super().__init__(src_path, dst_path, file_type)


class Timecapsule:
    def __init__(self, timestamp: time):
        self.timestamp = timestamp
        self.disks: list[Disk] = []
        self.memories: list[Memory] = []

    def add_disk(self, disk_path: Path, dst_path: Path, file_type: DataType):
        disk = Disk(disk_path, dst_path, file_type)
        self.disks.append(disk)

    def add_memory(self, memory_path: Path, dst_path: Path, file_type: DataType):
        memory = Memory(memory_path, dst_path, file_type)
        self.memories.append(memory)


class Target:
    def __init__(self, storage_dir: Path, target_uuid: UUID):
        self.storage_dir = storage_dir
        self.target_uuid = target_uuid
        self.target_dir = storage_dir / str(target_uuid)
        if not self.target_dir.exists():
            self.target_dir.mkdir(parents=True, exist_ok=True)
        self.timecapsules: list[Timecapsule] = []

    def is_timecapsule_exists(self, timecapsule: Timecapsule):
        target_timestamp = timecapsule.timestamp
        for t in self.timecapsules:
            if t.timestamp == target_timestamp:
                return True
        return False

    def add_timecapsule(self, timecapsule: Timecapsule):
        if not self.is_timecapsule_exists(timecapsule):
            self.timecapsules.append(timecapsule)


class Storage:
    def __init__(self, data_dir: Path = DEFAULT_PATH):
        if not data_dir.exists():
            data_dir.mkdir(parents=True, exist_ok=True)
        self.data_dir = data_dir
        self.targets: list[Target] = []

    def is_target_exists(self, target: Target):
        target_uuid = target.target_uuid
        for t in self.targets:
            if t.target_uuid == target_uuid:
                return True
        return False

    def add_target(self, target: Target):
        if not self.is_target_exists(target):
            self.targets.append(target)

    def get_filesystem(self):
        fs = dict()
        for t in self.targets:
            target = dict()
            for tc in t.timecapsules:
                timecapsule = {"disks": [], "memories": []}
                for dk in tc.disks:
                    timecapsule["disks"].append(dk.file_name)
                for mem in tc.memories:
                    timecapsule["memories"].append(mem.file_name)
                target[tc.timestamp] = timecapsule
            fs[t.target_uuid] = target
        return fs

    @classmethod
    def duplicate_storage_from_dict(cls, storage_dict: dict):
        pass
