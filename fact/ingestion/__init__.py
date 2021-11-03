from .record import FileRecord

from fact.exceptions import (
    LoopDeviceSetupError,
    LoopDeviceDetachError,
    UnmountPartitionError,
)
from fact.utils.decompression import decompress_gzip
from fact.utils.hashing import calculate_sha256

import subprocess
from pathlib import Path
from tempfile import mkstemp
from os import getegid

from typing import Optional, List, Tuple, Generator
import logging

log = logging.getLogger(__name__)


class Analyzer:
    """Base class for all analyzers"""

    def __init__(self, artifact_path: Path, artifact_hash: Optional[str]) -> None:
        self.artifact_path = artifact_path
        self.decompress_path: Path
        if artifact_hash is None:
            self.gzip_decompress()
            return
        if self.hash_integrity_check(artifact_hash):
            self.gzip_decompress()

    def gzip_decompress(self) -> None:
        """Decompress artifact at self.artifact_path"""
        artifact_suffix = "".join(self.artifact_path.suffixes[:-1])
        _, decompress_path = mkstemp(artifact_suffix, self.artifact_path.stem)
        self.decompress_path = Path(decompress_path)
        self.decompress_path.unlink()
        decompress_gzip(self.artifact_path, self.decompress_path, True)

    def hash_integrity_check(self, expected_hash: str) -> bool:
        """Checks the hash of the artifact if it matches expected hash

        :param expected_hash: Expected hash of artifact
        """
        actual_hash = calculate_sha256(self.artifact_path)
        return actual_hash == expected_hash


class DiskAnalyzer(Analyzer):
    """Sets up disk images for analysis"""

    loop_device_path: Optional[Path] = None
    mount_paths: Optional[List[Path]] = None

    def __init__(self, disk_image_path: Path, artifact_hash: Optional[str]) -> None:
        """Initialise Analyzer for disk images

        :param disk_image_path: Path of gzipped disk image for analysis
        :param artifact_hash: Hash of gzipped disk image
        :raises:
            PermissionError: Insufficient permission to initialise class
        """
        if getegid() != 0:
            raise PermissionError(
                f"Insufficient permissions to initialise {self.__class__.__name__}"
                ": Need to be root to set up and mount disk images."
            )
        super().__init__(disk_image_path, artifact_hash)
        assert disk_image_path.exists()

    def __enter__(self):
        self.setup()
        return self

    def __exit__(self, *rest):
        self.cleanup()

    def setup(self) -> None:
        """Wrapper function to call various functions to setup disk image"""
        self._setup_loop_device()
        self._mount_partitions()

    def cleanup(self) -> None:
        """Wrapper function to call various functions to clean up"""
        self._unmount_partitions()
        self._detach_loop_device()

    def analyse(self) -> Generator[FileRecord, None, None]:
        """Wrapper function to call various functions to analyse disk image"""
        return self._traverse_partitions()

    def _exec_command(self, args: List) -> Tuple[int, str, str]:
        """Calls subprocess.Popen for commandline tools

        :param args: A list of commands and arguments to execute
        :returns: A tuple of process status, STDOUT and STDERR
        """
        cmd = subprocess.run(args, capture_output=True)
        return cmd.returncode, cmd.stdout.decode().strip(), cmd.stderr.decode().strip()

    def _setup_loop_device(self) -> None:
        """Setups the disk image as a loop device

        :raises:
            LoopDeviceSetupError: Failure to setup the loop device
        """
        args = [
            "losetup",
            # TODO: Find a mechanism to mount loop devices without depending on
            "--find",
            "--show",
            "--read-only",
            "--partscan",
            self.decompress_path,
        ]
        returncode, stdout, stderr = self._exec_command(args)
        if returncode != 0:
            raise LoopDeviceSetupError(stderr)
        self.loop_device_path = Path(stdout)

    def _detach_loop_device(self) -> None:
        """Detaches the loop device previously setup

        :raises:
            AttributeError: No loop device was initially set up
            LoopDeviceDetachError: Failure to detach the loop device
        """
        assert self.loop_device_path is not None
        args = ["losetup", "--detach", self.loop_device_path]
        returncode, _, stderr = self._exec_command(args)
        if returncode != 0:
            raise LoopDeviceDetachError(stderr)

    def _identify_partitions(self) -> Generator[Path, None, None]:
        """Identifies the partitions of the loop device"""
        assert self.loop_device_path is not None

        device_path = Path("/dev")
        for p in device_path.iterdir():
            if (
                str(p).startswith(str(self.loop_device_path))
                and p != self.loop_device_path
            ):
                yield p

    def _mount_partitions(self) -> None:
        """Mounts the partitions found previously

        :raises:
            AttributeError: No partition search was initialised
            MountPartitionError: Failure to mount the partition
        """
        self.mount_paths = []

        mnt_base_path = Path("/tmp/fact/ingestion")
        for p in self._identify_partitions():
            p_mnt_path = mnt_base_path / p.name
            if not p_mnt_path.exists():
                p_mnt_path.mkdir(parents=True)
            args = [
                "mount",
                "--options",
                "ro,noload",
                p,
                p_mnt_path,
            ]
            returncode, _, stderr = self._exec_command(args)
            if returncode != 0:
                p_mnt_path.rmdir()
                log.warning(stderr)
            else:
                self.mount_paths.append(p_mnt_path)

    def _unmount_partitions(self) -> None:
        """Unmount the partitions mounted previously

        :raises:
            AttributeError: No partitions were mounted
            UnmountPartitionError: Failure to unmount the partition
        """
        assert self.mount_paths is not None

        for path in self.mount_paths:
            args = ["umount", path]
            returncode, _, stderr = self._exec_command(args)
            if returncode != 0:
                raise UnmountPartitionError(stderr)
            path.rmdir()

    def _traverse_partitions(self) -> Generator[FileRecord, None, None]:
        """Traverse the mounted partitions

        :returns: List of map generators of FileRecord for each file
        """
        assert self.mount_paths is not None

        for mount in self.mount_paths:
            file_paths = mount.rglob("*")
            for file in file_paths:
                yield FileRecord.from_stat_result(
                    str(self.artifact_path), str(mount), file.lstat()
                )
