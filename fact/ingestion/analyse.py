from fact.utils.decompression import decompress_gzip
from fact.utils.hashing import calculate_sha256

from subprocess import Popen, PIPE
from pathlib import Path
from tempfile import mkstemp

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
        self.paritions: List[Path]

    def __enter__(self):
        self.setup()
        return self

    def __exit__(self):
        self.cleanup()

    def setup(self):
        self._setup_loop_device()
        self._identify_partitions()
        self._mount_paritions()

    def cleanup(self):
        self._unmount_paritions()
        self._detach_loop_device()

    def analyse(self):
        return self._traverse_paritions()

    def _setup_loop_device(self):
        cmd = [
            "sudo",
            "-S",
            "losetup",
            "--find",
            "--show",
            "--read-only",
            "--partscan",
            self.disk_image_path,
        ]
        with Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
            stdout, stderr = proc.communicate(self.sudo_password.encode())
        proc_status = proc.wait()
        if proc_status != 0:
            print(stderr.decode())  # raise exception with stderr.decode()
        else:
            self.loop_device_path = Path(stdout.decode().strip())

    def _detach_loop_device(self):
        cmd = ["sudo", "-S", "losetup", "--detach", self.loop_device_path]
        with Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
            _, stderr = proc.communicate(self.sudo_password.encode())
        proc_status = proc.wait()
        if proc_status != 0:
            print(stderr.decode())  # raise exception with stderr.decode()
        else:
            return

    def _identify_partitions(self):
        device_path = Path("/dev")
        self.partitions = []
        for p in device_path.iterdir():
            if str(p).startswith(self.loop_device_path) and p != self.loop_device_path:
                self.partitions.append(p)

    def _mount_paritions(self):
        try:
            self.paritions
        except AttributeError:
            raise

        mnt_base_path = Path("/mnt/")
        for p in self.paritions:
            p_mnt_path = mnt_base_path / p
            if not p_mnt_path.exists():
                p_mnt_path.mkdir(parents=True)
            cmd = [
                "sudo",
                "-S",
                "mount",
                "--options",
                "noload",
                "--read-only",
                self.loop_device_path,
                p_mnt_path,
            ]
            with Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
                _, stderr = proc.communicate(self.sudo_password.encode())
            proc_status = proc.wait()
            if proc_status != 0:
                print(
                    stderr.decode()
                )  # raise exception with stderr.decode() / log error
            else:
                self.mount_paths.append(p_mnt_path)

    def _unmount_paritions(self):
        try:
            self.mount_paths
        except AttributeError:
            raise

        for path in self.mount_paths:
            cmd = ["sudo", "-S", "umount", path]
            with Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
                _, stderr = proc.communicate(self.sudo_password.encode())
            proc_status = proc.wait()
            if proc_status != 0:
                print(
                    stderr.decode()
                )  # raise exception with stderr.decode() / log error
            else:
                path.rmdir()

    def _traverse_paritions(self):
        file_system_info = dict()
        # TODO: Traverse with pathlib.Path.rglob("*") and
        # get all info on all files and dirs with pathlib.Path.lstat
        return file_system_info
