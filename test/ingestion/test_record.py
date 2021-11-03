from dataclasses import asdict
from pathlib import Path

from fact.ingestion.record import RecordBase, FileRecord


def test_asdict_base():
    r = RecordBase("test_artifact", "test")
    assert asdict(r) == {"fact_artifact": "test_artifact", "fact_type": "test"}

    os_stat = Path("/").lstat()
    r = FileRecord.from_stat_result("test_artifact", "0", "/path", os_stat)
    d = asdict(r)
    assert d["fact_artifact"] == "test_artifact"
    assert d["fact_type"] == "file"
    assert d["path"] == "/path"
    assert "st_mode" in d
    assert "st_atime" in d


# vim: set et ts=4 sw=4:
