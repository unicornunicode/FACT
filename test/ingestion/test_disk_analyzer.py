import pytest

from fact.ingestion import DiskAnalyzer

from pathlib import Path
from tempfile import NamedTemporaryFile
import gzip


@pytest.fixture
def disk_analyzer():
    with NamedTemporaryFile("wb") as disk_f:
        with gzip.open(Path("test/files/test_data.gz"), "rb") as f:
            while buf := f.read(65535):
                disk_f.write(buf)
        disk_f.flush()

        try:
            disk_analyzer = DiskAnalyzer(
                disk_image_path=disk_f.name,
            )
        except PermissionError:
            pytest.skip()
        return disk_analyzer


def test_setup_disk(disk_analyzer: DiskAnalyzer):
    # Call each function called in DiskAnalyzer.setup()

    disk_analyzer._setup_loop_device()
    disk_analyzer._identify_partitions()
    disk_analyzer._mount_partitions()

    disk_analyzer.cleanup()


def test_cleanup_disk(disk_analyzer: DiskAnalyzer):
    disk_analyzer.setup()

    # Call each function called in DiskAnalyzer.cleanup()

    disk_analyzer._unmount_partitions()
    assert disk_analyzer.mount_paths is not None
    for mp in disk_analyzer.mount_paths:
        assert not mp.exists()

    disk_analyzer._detach_loop_device()
