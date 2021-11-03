from dataclasses import asdict
from pathlib import Path

from fact.ingestion.record import RecordBase, FileRecord


def test_asdict_base():
    r = RecordBase("test")
    assert asdict(r) == {"fact_type": "test"}


def test_asdict_file():
    os_stat = Path("/").lstat()
    r = FileRecord.from_stat_result("0", "/path", os_stat)
    d = asdict(r)
    assert d["fact_type"] == "file"
    assert d["path"] == "/path"
    assert "st_mode" in d
    assert "st_atime" in d


# vim: set et ts=4 sw=4:
