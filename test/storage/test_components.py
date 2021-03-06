import pytest

from fact.storage import Storage, Task, Artifact
from fact.storage.types import ArtifactType
from fact.exceptions import (
    TaskInvalidUUID,
    ArtifactInvalidName,
    ArtifactInvalidType,
)

from pathlib import Path
from tempfile import mkdtemp
from uuid import uuid4


def test_init_storage():
    desired_path = Path(mkdtemp())
    # Let Storage create the directory structure
    desired_path.rmdir()

    stg1 = Storage(desired_path)
    assert stg1.get_storage_path() == desired_path
    assert stg1.get_storage_info() == {"data_dir": str(desired_path), "tasks": []}

    # Storage should be able to run with the same folder
    Storage(desired_path)

    # Cleanup
    desired_path.rmdir()


def test_init_task():
    with pytest.raises(TaskInvalidUUID):
        Task()

    tsk2_uuid = uuid4()
    tsk2_uuid_str = str(tsk2_uuid)
    tsk2 = Task(tsk2_uuid_str)
    assert tsk2.get_task_uuid() == tsk2_uuid_str
    assert tsk2.get_task_path() == Path(tsk2_uuid_str)
    assert tsk2.get_task_info() == {"task_uuid": tsk2_uuid_str, "artifacts": []}

    tsk3_uuid_str = "deadbeef"
    with pytest.raises(TaskInvalidUUID):
        Task(tsk3_uuid_str)


def test_init_artifact():
    with pytest.raises(ArtifactInvalidName):
        Artifact()

    artf2_artifact_name = "test.docx"
    artf2 = Artifact(artf2_artifact_name)
    artf2_artifact_type = artf2.get_artifact_type()
    artf2_type_path, artf2_name = artf2.get_artifact_path()
    artf2_artifact_path = artf2_type_path / artf2_name
    assert artf2.artifact_name == artf2_artifact_name
    assert type(artf2.artifact_type) == ArtifactType
    assert artf2_artifact_type == ArtifactType.unknown.name
    expected_path = Path(artf2_artifact_type) / Path(artf2_artifact_name)
    assert artf2_artifact_path == expected_path

    artf3_artifact_name = "test2.raw"
    artf3_artifact_type = "DISK"
    with pytest.raises(ArtifactInvalidType):
        Artifact(artf3_artifact_name, artf3_artifact_type)
