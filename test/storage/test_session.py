from fact.storage import Storage, Task, Artifact, SessionManager
from fact.storage.types import ArtifactType, DataType

from pathlib import Path
from uuid import uuid4


def test_synchronous_session():
    stg_path = Path("/tmp/fact")
    stg = Storage(stg_path)
    tsk_uuid = uuid4()
    tsk = Task(str(tsk_uuid))
    artf1 = Artifact("sda.raw", ArtifactType.disk.name, DataType.full.name)
    artf1_contents = b"I am sda.raw data"
    artf2 = Artifact("sdb1.raw", ArtifactType.disk.name, DataType.partition.name)
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
    with open(artf1_path, "rb") as f:
        asrtf1_actual_contents = f.read()
    assert artf1_contents == asrtf1_actual_contents

    artf2_path = stg.get_task_artifact_path(str(tsk_uuid), artf2)
    with open(artf2_path, "rb") as f:
        asrtf2_actual_contents = f.read()
    assert artf2_contents == asrtf2_actual_contents


def test_asynchronous_session():
    pass
