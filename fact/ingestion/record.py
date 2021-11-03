from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Union


@dataclass
class RecordBase:
    """Base record class for all artifacts"""

    fact_artifact: str
    fact_type: str


@dataclass
class FileRecord(RecordBase):
    """Record class for disk"""

    st_mode: int
    st_ino: int
    st_nlink: int
    st_uid: int
    st_gid: int
    st_size: int
    st_atime: float
    st_mtime: float
    st_ctime: float

    @classmethod
    def from_stat_result(
        cls, artifact: str, type: str, os_stat: os.stat_result
    ) -> FileRecord:
        return cls(
            fact_artifact=artifact,
            fact_type=type,
            st_mode=os_stat.st_mode,
            st_ino=os_stat.st_ino,
            st_nlink=os_stat.st_nlink,
            st_uid=os_stat.st_uid,
            st_gid=os_stat.st_gid,
            st_size=os_stat.st_size,
            st_atime=os_stat.st_atime,
            st_mtime=os_stat.st_mtime,
            st_ctime=os_stat.st_ctime,
        )


Record = Union[FileRecord]
