import pytest
from shutil import rmtree

from fact.storage import Storage, Task, Artifact
from fact.storage.types import ArtifactType, DataType
from fact.exceptions import (
    ArtifactNotFoundError,
    ArtifactExistsError,
    TaskExistsError,
    TaskNotFoundError,
)

from pathlib import Path
from tempfile import mkdtemp
from uuid import uuid4


@pytest.fixture
def init_artifacts():
    artf1 = Artifact("sda.raw", ArtifactType.disk.name, DataType.full.name)
    artf2 = Artifact("sdb1.raw", ArtifactType.disk.name, DataType.partition.name)
    artf3 = Artifact("1.mem", ArtifactType.memory.name, DataType.process.name)
    return [artf1, artf2, artf3]


@pytest.fixture
def init_tasks():
    tasks = []
    for _ in range(3):
        task_uuid = uuid4()
        task = Task(str(task_uuid))
        tasks.append(task)
    return tasks


@pytest.fixture
def init_storage(request):
    tmpdir = Path(mkdtemp())

    def cleanup():
        rmtree(tmpdir, ignore_errors=True)

    request.addfinalizer(cleanup)

    stg = Storage(tmpdir)
    return stg


def test_task_artifact(init_artifacts, init_tasks):
    tasks: list[Task] = init_tasks
    artifacts: list[Artifact] = init_artifacts

    # Add first 2 artifacts into first task
    tsk = tasks[0]
    for artifact in artifacts[:-1]:
        tsk.add_artifact(artifact)

    artf1, artf2, artf3 = artifacts
    artf1_info = artf1.get_artifact_info()
    artf3_info = artf3.get_artifact_info()

    assert type(tsk.get_artifact(artf1_info)) == Artifact
    assert tsk.get_artifact(artf3_info) is None
    assert tsk.is_artifact_exists(artf1_info)
    assert not tsk.is_artifact_exists(artf3_info)
    assert tsk.add_artifact(artf3) is None
    with pytest.raises(ArtifactExistsError):
        tsk.add_artifact(artf2)


def test_storage_task_artifact(init_artifacts, init_tasks, init_storage):
    tasks: list[Task] = init_tasks
    artifacts: list[Artifact] = init_artifacts
    storage: Storage = init_storage

    storage_path = storage.get_storage_path()
    tsk1, tsk2, tsk3 = tasks
    tsk1_uuid = tsk1.get_task_uuid()
    tsk2_uuid = tsk2.get_task_uuid()
    tsk3_uuid = tsk3.get_task_uuid()
    artf1, artf2, artf3 = artifacts

    # Add first 2 artifacts to first task, which is added to storage
    for artifact in artifacts[:-1]:
        tsk1.add_artifact(artifact)
    storage.add_task(tsk1)

    assert type(storage.get_task(tsk1_uuid)) == Task
    assert storage.get_task(tsk2_uuid) is None
    assert storage.is_task_uuid_exists(tsk1_uuid)
    assert not storage.is_task_uuid_exists(tsk2_uuid)
    assert storage.add_task(tsk2) is None
    with pytest.raises(TaskExistsError):
        storage.add_task(tsk1)

    tsk1_in_storage = storage.get_task(tsk1_uuid)
    tsk1_in_storage_path = tsk1_in_storage.get_task_path()
    artf3_info_path, artf3_name = artf3.get_artifact_path()
    artf3_path = artf3_info_path / artf3_name
    artf3_full_path = storage_path / tsk1_in_storage_path / artf3_path
    assert storage.add_task_artifact(tsk1_uuid, artf3) == artf3_full_path
    with pytest.raises(TaskNotFoundError):
        storage.add_task_artifact(tsk3_uuid, artf1)

    assert storage.get_task_artifact_path(tsk1_uuid, artf3) == artf3_full_path
    with pytest.raises(ArtifactNotFoundError):
        storage.get_task_artifact_path(tsk2_uuid, artf1)
    with pytest.raises(TaskNotFoundError):
        storage.get_task_artifact_path(tsk3_uuid, artf1)

    rmtree(storage_path)
