from pathlib import Path
from datetime import datetime


class Record:
    """Base record class for all artifacts"""

    def __init__(self, file_path: Path):
        """Initialises the record for the artifact"""
        self.fact_filepath = file_path
        self.fact_analysisdatetime = datetime.now()


class DiskRecord(Record):
    """Record class for disk"""

    def __init__(self, file_path: Path) -> None:
        """Initialises the record for the file/folder on disk"""
        super().__init__(file_path)
        self._get_fs_attributes()

    def _get_fs_attributes(self) -> None:
        """Get the stat of the file/folder"""
        os_stat = self.fact_filepath.lstat()

        self.fs_mode = os_stat.st_mode
        self.fs_ino = os_stat.st_ino
        self.fs_dev = os_stat.st_dev
        self.fs_nlink = os_stat.st_nlink
        self.fs_uid = os_stat.st_uid
        self.fs_gid = os_stat.st_gid
        self.fs_size = os_stat.st_size
        self.fs_atime = os_stat.st_atime
        self.fs_mtime = os_stat.st_mtime
        self.fs_ctime = os_stat.st_ctime
