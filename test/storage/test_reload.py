import pytest
import logging

from fact.storage import Session, Storage, Task, Artifact

from pathlib import Path
from tempfile import mkdtemp
from uuid import UUID, uuid4
from shutil import rmtree


@pytest.fixture
def setup_storage(request):
    tmpdir = Path(mkdtemp())

    def cleanup():
        rmtree(tmpdir, ignore_errors=True)

    request.addfinalizer(cleanup)

    # Let Storage create the directory structure
    tmpdir.rmdir()

    id = str(UUID(int=0))
    tsk = Task(id)
    artf1 = Artifact("sda.raw", "disk")
    artf1_contents = b"I am sda.raw"

    stg1 = Storage(tmpdir)
    with Session(stg1, tsk, artf1) as sess:
        sess.write(artf1_contents)

    return tmpdir


def test_init_storage():
    desired_path = Path(mkdtemp())
    # Let Storage create the directory structure
    desired_path.rmdir()

    id = str(UUID(int=0))
    tsk = Task(id)
    artf1 = Artifact("sda.raw", "disk")
    artf1_contents = b"I am sda.raw"

    stg1 = Storage(desired_path)
    assert stg1.get_storage_path() == desired_path
    assert stg1.get_storage_info() == {"data_dir": str(desired_path), "tasks": []}

    with Session(stg1, tsk, artf1) as sess:
        sess.write(artf1_contents)

    # Storage should be able to run with the same folder
    stg2 = Storage(desired_path)
    assert stg2.get_task(id) is not None
    assert stg2.get_task_artifact_path(id, artf1) is not None

    # Cleanup
    rmtree(desired_path, ignore_errors=True)


def test_unknown_folder_structure(caplog, setup_storage):
    desired_path = setup_storage

    unknown_folder_struct = Path("a/a/a/a/")
    full_unknown_folder_struct = desired_path / unknown_folder_struct
    full_unknown_folder_struct.mkdir(parents=True, exist_ok=False)
    with caplog.at_level(logging.WARNING):
        Storage(desired_path)
        assert (
            caplog.records[-1].msg
            == "Unknown folder structure. "
            + f"Skipping reconstruction of {unknown_folder_struct}."
        )


def test_invalid_artifact_(caplog, setup_storage):
    desired_path = setup_storage

    tsk_uuid = uuid4()
    unknown_artifact_type = "docs"
    unknown_artifact_path = Path(f"{tsk_uuid}/{unknown_artifact_type}/a.docx")
    full_unknown_folder_struct = desired_path / unknown_artifact_path
    full_unknown_folder_struct.mkdir(parents=True, exist_ok=False)
    with caplog.at_level(logging.WARNING):
        Storage(desired_path)
        assert (
            caplog.records[-1].msg
            == f"Invalid artifact type: {unknown_artifact_type}. "
            + f"Skipping reconstruction of {unknown_artifact_path}."
        )
