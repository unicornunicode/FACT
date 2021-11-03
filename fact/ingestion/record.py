from __future__ import annotations

import os
from datetime import datetime
from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class RecordBase:
    """Base record class for all artifacts"""

    fact_artifact: str
    fact_type: str


@dataclass
class FileRecord(RecordBase):
    """Record class for disk"""

    partition: Optional[str]
    path: str
    st_mode: int
    st_ino: int
    st_nlink: int
    st_uid: int
    st_gid: int
    st_size: int
    st_atime: datetime
    st_mtime: datetime
    st_ctime: datetime

    @classmethod
    def from_stat_result(
        cls, artifact: str, partition: Optional[str], path: str, os_stat: os.stat_result
    ) -> FileRecord:
        return cls(
            fact_artifact=artifact,
            fact_type="file",
            partition=partition,
            path=path,
            st_mode=os_stat.st_mode,
            st_ino=os_stat.st_ino,
            st_nlink=os_stat.st_nlink,
            st_uid=os_stat.st_uid,
            st_gid=os_stat.st_gid,
            st_size=os_stat.st_size,
            st_atime=datetime.fromtimestamp(os_stat.st_atime),
            st_mtime=datetime.fromtimestamp(os_stat.st_mtime),
            st_ctime=datetime.fromtimestamp(os_stat.st_ctime),
        )


Record = Union[FileRecord]
