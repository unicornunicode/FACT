from uuid import uuid4
from pathlib import Path
from tempfile import TemporaryDirectory

from fact.storage import FilesystemStorage


def test_filesystem():
    with TemporaryDirectory() as d:
        uuid = uuid4()
        s = FilesystemStorage(Path(d))
        with s.writer(uuid, "device1", "disk") as f:
            f.write(b"hello")
        with s.reader(uuid, "device1", "disk") as f:
            assert f.read() == b"hello"


# vim: set et ts=4 sw=4:
