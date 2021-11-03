import pytest

from fact.ingestion import DiskAnalyzer

from pathlib import Path


@pytest.fixture
def init_disk_analyzer():
    disk_gz_path = Path("test/files/disk.raw.gz")
    try:
        dsk_anz = DiskAnalyzer(
            disk_gz_path,
            "cfff29e041c818881a58a5ac1ddc68f6fa05b02504485c327822d6df2e131fa5",
        )
    except PermissionError:
        pytest.skip()
    return dsk_anz


def test_init_analyzer(init_disk_analyzer):
    dsk_anz: DiskAnalyzer = init_disk_analyzer
    assert dsk_anz.decompress_path


def test_setup_disk(init_disk_analyzer):
    dsk_anz: DiskAnalyzer = init_disk_analyzer

    # Call each function called in DiskAnalyzer.setup()

    dsk_anz._setup_loop_device()
    dsk_anz.loop_device_path  # Asserts AttributeError not raised

    dsk_anz._identify_partitions()
    dsk_anz.partitions  # Asserts AttributeError not raised

    dsk_anz._mount_partitions()
    dsk_anz.mount_paths  # Asserts AttributeError not raised

    dsk_anz.cleanup()


def test_cleanup_disk(init_disk_analyzer):
    dsk_anz: DiskAnalyzer = init_disk_analyzer
    dsk_anz.setup()

    # Call each function called in DiskAnalyzer.cleanup()

    dsk_anz._unmount_partitions()
    for mp in dsk_anz.mount_paths:
        assert not mp.exists()

    dsk_anz._detach_loop_device()
