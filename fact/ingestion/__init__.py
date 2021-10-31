from .record import DiskRecord

from fact.exceptions import (
    LoopDeviceSetupError,
    LoopDeviceDetachError,
    MountPartitionError,
    UnmountPartitionError,
)
from fact.utils.decompression import decompress_gzip
from fact.utils.hashing import calculate_sha256

from subprocess import Popen, PIPE
from pathlib import Path
from tempfile import mkstemp

from typing import List


class Analyzer:
    """Base class for all analyzers"""

    def __init__(self, artifact_path: Path, artifact_hash: str) -> None:
        self.artifact_path = artifact_path
        self.decompress_path: Path
        if self.hash_integrity_check(artifact_hash):
            self.gzip_decompress()

    def gzip_decompress(self) -> None:
        artifact_suffix = "".join(self.artifact_path.suffixes[:-1])
        _, decompress_path = mkstemp(artifact_suffix, self.artifact_path.stem)
        self.decompress_path = Path(decompress_path)
        self.decompress_path.unlink()
        decompress_gzip(self.artifact_path, self.decompress_path, True)

    def hash_integrity_check(self, expected_hash: str) -> bool:
        actual_hash = calculate_sha256(self.artifact_path)
        return actual_hash == expected_hash


class DiskAnalyzer(Analyzer):
    def __init__(self, disk_image_path: Path, artifact_hash: str):
        super().__init__(disk_image_path, artifact_hash)
        self.loop_device_path: Path
        self.mount_paths: List[Path]
        self.partitions: List[Path]

    def __enter__(self):
        self.setup()
        return self

    def __exit__(self):
        self.cleanup()

    def setup(self):
        self._setup_loop_device()
        self._identify_partitions()
        self._mount_partitions()

    def cleanup(self):
        self._unmount_partitions()
        self._detach_loop_device()

    def analyse(self):
        return self._traverse_partitions()

    def _exec_command(self, cmd: list):
        with Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
            stdout, stderr = proc.communicate()
            proc_status = proc.wait()
        return proc_status, stdout.decode().strip(), stderr.decode().strip()

    def _setup_loop_device(self):
        cmd = [
            "losetup",
            "--find",
            "--show",
            "--read-only",
            "--partscan",
            self.decompress_path,
        ]
        proc_status, stdout, stderr = self._exec_command(cmd)
        if proc_status != 0:
            raise LoopDeviceSetupError(stderr)
        else:
            self.loop_device_path = Path(stdout)

    def _detach_loop_device(self):
        cmd = ["losetup", "--detach", self.loop_device_path]
        proc_status, _, stderr = self._exec_command(cmd)
        if proc_status != 0:
            raise LoopDeviceDetachError(stderr)
        else:
            return True

    def _identify_partitions(self):
        device_path = Path("/dev")
        self.partitions = []
        for p in device_path.iterdir():
            if (
                str(p).startswith(str(self.loop_device_path))
                and p != self.loop_device_path
            ):
                self.partitions.append(p)

    def _mount_partitions(self):
        try:
            self.partitions
        except AttributeError:
            raise

        self.mount_paths = []
        mnt_base_path = Path("/mnt/")
        for p in self.partitions:
            p_mnt_path = mnt_base_path / p
            if not p_mnt_path.exists():
                p_mnt_path.mkdir(parents=True)
            cmd = [
                "mount",
                "--options",
                "noload",
                "--read-only",
                p,
                p_mnt_path,
            ]
            proc_status, _, stderr = self._exec_command(cmd)
            if proc_status != 0:
                p_mnt_path.rmdir()
                raise MountPartitionError(stderr)
            else:
                self.mount_paths.append(p_mnt_path)

    def _unmount_partitions(self):
        try:
            self.mount_paths
        except AttributeError:
            raise

        for path in self.mount_paths:
            cmd = ["umount", path]
            proc_status, _, stderr = self._exec_command(cmd)
            if proc_status != 0:
                raise UnmountPartitionError(stderr)
            else:
                path.rmdir()

    def _traverse_partitions(self):
        partitions_records = []
        for path in self.mount_paths:
            file_paths = path.rglob("*")
            partitions_records.append(map(DiskRecord, file_paths))
        return partitions_records
