from tempfile import NamedTemporaryFile
from pathlib import Path
import gzip

from fact.utils.hashing import calculate_sha256


def test_sha256sum_implementation():
    hashstring = calculate_sha256(Path("test/files/invalid_gzip.gz"))
    assert (
        hashstring.lower()
        == "5752c3c283912fb6cf27984849003e793cc6ce42f0416ecfcb91d24e5c60f7a8"
    )


def test_gunzip():
    with NamedTemporaryFile("wb") as disk_f:
        with gzip.open(Path("test/files/test_data.gz"), "rb") as f:
            while buf := f.read(65535):
                disk_f.write(buf)
        disk_f.flush()
        assert calculate_sha256(Path(disk_f.name)) == calculate_sha256(
            Path("test/files/raw_data")
        )
