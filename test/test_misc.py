import os
import pytest

from pathlib import Path

from fact.utils.decompression import decompress_gzip
from fact.exceptions import GzipExtensionError, GzipDecompressionError
from fact.utils.hashing import calculate_sha256


def test_sha256sum_implementation():
    hashstring = calculate_sha256(Path("test/files/invalid_gzip.gz"))
    assert (
        hashstring.lower()
        == "5752c3c283912fb6cf27984849003e793cc6ce42f0416ecfcb91d24e5c60f7a8"
    )


def test_invalid_gunzip_extension():
    with pytest.raises(GzipExtensionError):
        decompress_gzip(Path("test/files/raw_data"))


def test_invalid_gunzip():
    with pytest.raises(GzipDecompressionError):
        decompress_gzip(Path("test/files/invalid_gzip.gz"))
    os.remove("test/files/invalid_gzip")


def test_gunzip():
    decompress_gzip(Path("test/files/test_data.gz"))
    assert calculate_sha256(Path("test/files/test_data")) == calculate_sha256(
        Path("test/files/raw_data")
    )
    os.remove("test/files/test_data")
