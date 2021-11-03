import pytest

from fact.ingestion import DiskAnalyzer

from pathlib import Path


@pytest.fixture
def disk_analyzer():
    disk_gz_path = Path("test/files/disk.raw.gz")
    try:
        disk_analyzer = DiskAnalyzer(
            disk_image_path=disk_gz_path,
            artifact_hash="cfff29e041c818881a58a5ac1ddc68f6fa05b02504485c327822d6df2e131fa5",
        )
    except PermissionError:
        pytest.skip()
    return disk_analyzer


def test_init_analyzer(disk_analyzer: DiskAnalyzer):
    assert disk_analyzer.decompress_path


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
