import pytest

from fact.storage import Session, Storage, Task, Artifact
from fact.storage.types import ArtifactType

from pathlib import Path
from tempfile import mkdtemp
from shutil import rmtree
from uuid import uuid4


def verify_contents(file_path, actual_file_contents):
    with open(file_path, "rb") as f:
        file_contents = f.read()
    return file_contents == actual_file_contents


@pytest.fixture
def init_storage(request):
    tmpdir = Path(mkdtemp())

    def cleanup():
        rmtree(tmpdir, ignore_errors=True)

    request.addfinalizer(cleanup)

    stg = Storage(tmpdir)
    return stg


@pytest.fixture
def init_task_artifact():
    tsk_uuid = uuid4()
    tsk = Task(str(tsk_uuid))
    artf1 = Artifact("sda.raw", ArtifactType.disk.name)
    artf2 = Artifact("sdb1.raw", ArtifactType.disk.name)

    return tsk, artf1, artf2


def test_session(init_storage, init_task_artifact):
    stg = init_storage
    tsk, artf1, artf2 = init_task_artifact
    tsk_uuid = tsk.get_task_uuid()
    artf1_contents = b"I am sda.raw data"
    artf2_contents = b"I am sdb1.raw data"

    # First way to initialise and interact with Session
    with Session(stg, tsk, artf1) as sess:
        sess.write(artf1_contents)

    # Second way to initialise and interact with Session
    sess2 = Session(stg, tsk, artf2)
    with pytest.raises(AttributeError):
        sess2.write(artf2_contents)
    with pytest.raises(AttributeError):
        sess2.close()
    sess2.setup()
    sess2.write(artf2_contents)
    sess2.close()

    artf1_path = stg.get_task_artifact_path(str(tsk_uuid), artf1)
    assert verify_contents(artf1_path, artf1_contents)

    artf2_path = stg.get_task_artifact_path(str(tsk_uuid), artf2)
    assert verify_contents(artf2_path, artf2_contents)
