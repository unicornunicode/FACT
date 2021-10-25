import pytest

from fact.storage import Storage, Task, Artifact, SessionManager
from fact.storage.types import ArtifactType, DataType

from pathlib import Path
from tempfile import mkdtemp
from shutil import rmtree
from uuid import uuid4


def verify_contents(file_path, actual_file_contents):
    with open(file_path, "rb") as f:
        file_contents = f.read()
    return file_contents == actual_file_contents


@pytest.fixture
def init_storage_task_artifact(request):
    tmpdir = Path(mkdtemp())

    def cleanup():
        rmtree(tmpdir, ignore_errors=True)

    request.addfinalizer(cleanup)

    stg = Storage(tmpdir)
    tsk_uuid = uuid4()
    tsk = Task(str(tsk_uuid))
    artf1 = Artifact("sda.raw", ArtifactType.disk.name, DataType.full.name)
    artf2 = Artifact("sdb1.raw", ArtifactType.disk.name, DataType.partition.name)

    return stg, tsk, artf1, artf2


@pytest.mark.asyncio
async def test_session(event_loop, init_storage_task_artifact):
    stg, tsk, artf1, artf2 = init_storage_task_artifact
    tsk_uuid = tsk.get_task_uuid()
    artf1_contents = b"I am sda.raw data"
    artf2_contents = b"I am sdb1.raw data"

    sm = SessionManager(stg)
    sess1 = sm.new_session(tsk, artf1)
    sess2 = sm.new_session(tsk, artf2)
    sess1.file_io.write(artf1_contents)
    sess2.file_io.write(artf2_contents)
    sm.end_session(sess1)
    sm.end_session(sess2)
    sm.terminate()

    artf1_path = stg.get_task_artifact_path(str(tsk_uuid), artf1)
    assert verify_contents(artf1_path, artf1_contents)

    artf2_path = stg.get_task_artifact_path(str(tsk_uuid), artf2)
    assert verify_contents(artf2_path, artf2_contents)
