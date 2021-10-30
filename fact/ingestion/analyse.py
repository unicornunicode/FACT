from fact.utils.decompression import decompress_gzip
from fact.utils.hashing import calculate_sha256

from subprocess import Popen, PIPE
from pathlib import Path
from tempfile import mkstemp
import re

from typing import List


class Analyzer:
    """Base class for all analyzers"""

    def __init__(
        self, sudo_password: str, artifact_path: Path, artifact_hash: str
    ) -> None:
        self.sudo_password = sudo_password
        self.decompress_path: Path
        self.artifact_path = artifact_path
        if self.hash_integrity_check(artifact_hash):
            self.gzip_decompress()

    def gzip_decompress(self) -> None:
        artifact_suffix = "".join(self.artifact_path.suffixes[:-1])
        _, decompress_path = mkstemp(artifact_suffix, self.artifact_path.stem)
        self.decompress_path = Path(decompress_path)
        self.decompress_path.unlink()
        decompress_gzip(
            self.artifact_path, self.decompress_path, True
        )  # Include exception handling

    def hash_integrity_check(self, expected_hash: str) -> bool:
        actual_hash = calculate_sha256(self.artifact_path)
        return actual_hash == expected_hash


class DiskAnalyzer(Analyzer):
    def __init__(self, sudo_password: str, disk_image_path: Path, artifact_hash: str):
        super().__init__(sudo_password, disk_image_path, artifact_hash)
        self.loop_device_path: Path
        self.mount_paths: List[Path]
        self.file_systems: List

    def __enter__(self):
        self.setup()
        return self

    def __exit__(self):
        self.cleanup()

    def setup(self):
        self._setup_loop_device()
        self._identify_file_systems()
        self._mount_file_systems()

    def cleanup(self):
        self._unmount_file_systems()
        self._detach_loop_device()

    def analyse(self):
        return self._traverse_file_systems()

    def _setup_loop_device(self):
        cmd = [
            "sudo",
            "-S",
            "losetup",
            "--find",
            "--show",
            "--read-only",
            self.disk_image_path,
        ]
        with Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
            stdout, stderr = proc.communicate(self.sudo_password.encode())
        if not stderr.decode():
            self.loop_device_path = stdout.decode().strip()
        else:
            pass  # raise exception

    def _detach_loop_device(self):
        cmd = ["sudo", "-S", "losetup", "--detach", self.loop_device_path]
        with Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
            _, stderr = proc.communicate(self.sudo_password.encode())
        if not stderr.decode():
            return
        else:
            pass  # raise exception

    def _identify_file_systems(self):
        sector_size = 512
        cmd = [
            "sudo",
            "-S",
            "fdisk",
            "--list",
            "--sector-size",
            str(sector_size),
            self.loop_device_path,
        ]
        with Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
            stdout, stderr = proc.communicate(self.sudo_password.encode())
        if not stderr.decode():
            fdisk_output = stdout.decode().strip()
            partition_table = re.search(
                r"Device\s*Start\s*End\s*Sectors\s*Size\s*Type\s*([.\S\W]*)",
                fdisk_output,
            )

            self.file_systems = []
            if partition_table:
                records = partition_table.group(1).split("\n")
                for record in records:
                    partition = re.split(r"\s+", record)
                    partition_columns = len(partition)
                    if partition_columns == 1:
                        break
                    elif partition_columns > 5:
                        diff = 5 - partition_columns
                        partition = partition[:diff] + " ".join(partition[diff:])

                    if partition[-1] == "Linux filesystem":
                        start_sector = int(partition[1])
                        self.file_systems.append(str(start_sector * sector_size))
                    # TODO: Add more types
        else:
            pass  # raise exception

    def _mount_file_systems(self):
        try:
            self.file_systems
        except AttributeError:
            raise

        mnt_base_path = "/mnt/diskartf"
        for idx, fs in enumerate(self.file_systems):
            fs_mnt_path = Path(mnt_base_path + str(idx))
            if not fs_mnt_path.exists():
                fs_mnt_path.mkdir(parents=True)
            cmd = [
                "sudo",
                "-S",
                "mount",
                "--options",
                f"offset={fs},ro,noload",
                self.loop_device_path,
                fs_mnt_path,
            ]
            with Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
                _, stderr = proc.communicate(self.sudo_password.encode())
            if not stderr.decode():
                self.mount_paths.append(fs_mnt_path)
                continue
            else:
                pass  # raise exception / log error

    def _unmount_file_systems(self):
        try:
            self.mount_paths
        except AttributeError:
            raise

        for path in self.mount_paths:
            cmd = ["sudo", "-S", "umount", path]
            with Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
                _, stderr = proc.communicate(self.sudo_password.encode())
            if not stderr.decode():
                continue
            else:
                pass  # raise exception / log error

    def _traverse_file_systems(self):
        file_system_info = dict()
        # TODO: Traverse with pathlib.Path.rglob("*") and
        # get all info on all files and dirs with pathlib.Path.lstat
        return file_system_info
