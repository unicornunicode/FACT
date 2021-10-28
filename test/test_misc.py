import os

from pathlib import Path

from fact.utils.decompression import decompress_gzip
from fact.exceptions import GzipDecompressionError
from fact.utils.hashing import calculate_sha256


def test_sha256sum_implementation():
    hashstring = calculate_sha256(Path("test/files/invalid_gzip.gz"))
    assert (
        hashstring.lower()
        == "5752c3c283912fb6cf27984849003e793cc6ce42f0416ecfcb91d24e5c60f7a8"
    )


def test_invalid_gunzip():
    assert_list = []

    try:
        decompress_gzip(Path("test/files/raw_data"))
    except GzipDecompressionError as e:
        if "no .gz extension" in e.message:
            assert_list.append(1)

    try:
        decompress_gzip(Path("test/files/invalid_gzip.gz"))
    except GzipDecompressionError as e:
        if "Error reading/processing" in e.message:
            assert_list.append(2)
        # Cleanup
        os.remove("test/files/invalid_gzip")

    assert assert_list == [1, 2]


def test_gunzip():
    decompress_gzip(Path("test/files/test_data.gz"))
    assert calculate_sha256(Path("test/files/test_data")) == calculate_sha256(
        Path("test/files/raw_data")
    )
    # cleanup
    os.remove("test/files/test_data")
