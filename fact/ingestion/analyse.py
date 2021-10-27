from fact.storage import Artifact

# from fact.utils.decompression import decompress_gzip

from pathlib import Path
from tempfile import mkstemp


class Analyzer:
    """Base class for all analyzers"""

    def __init__(
        self, artifact_path: Path, artifact: Artifact, artifact_hash: str
    ) -> None:
        self.decompress_path: Path
        self.artifact_path = artifact_path
        self.artifact_type = artifact.get_artifact_type()
        self.artifact_name = artifact.artifact_name
        if self.hash_integrity_check(artifact_hash):
            self.gzip_decompress()

    def gzip_decompress(self) -> None:
        artifact_suffix = "".join(self.artifact_path.suffixes[:-1])
        _, decompress_path = mkstemp(artifact_suffix, self.artifact_path.stem)
        self.decompress_path = Path(decompress_path)
        self.decompress_path.unlink()  # let decompress_gzip create file
        # decompress_gzip(
        #     self.artifact_path, self.decompress_path, True
        # )  # Include exception handling

    def hash_integrity_check(self, file_hash: str) -> bool:
        # Move and use sha256 util from test/utils
        return True


class DiskAnalyzer(Analyzer):
    def __init__(self, artifact_path: Path, artifact: Artifact, artifact_hash: str):
        super().__init__(artifact_path, artifact, artifact_hash)

    def __enter__(self):
        self.setup()
        return self

    def __exit__(self):
        pass

    def setup(self):
        pass  # setup the disk image

    @staticmethod
    def attach_loop_device(disk_path: Path) -> Path:
        loop_device_path: Path = Path()
        # create loop device with losetup
        return loop_device_path  # loop device path (/dev/loopXX)

    @staticmethod
    def identify_partitions(loop_device: Path) -> dict:
        partitions: dict = dict()
        # get all paritions with lsblk
        return partitions

    @staticmethod
    def mount_partition(partition: str, loop_device: Path) -> Path:
        mounted_path: Path = Path()
        # mount parition of loop device
        return mounted_path  # mounted path

    @staticmethod
    def traverse_file_system(self, mount_path: Path) -> dict:
        file_system_info: dict = dict()
        # traverse with pathlib.Path.rglob("*")
        # get all info on all files and dirs with pathlib.Path.lstat
        return file_system_info
