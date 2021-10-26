from fact.storage import Storage, Task, Artifact

from pathlib import Path
from tempfile import mkdtemp
from uuid import UUID
from shutil import rmtree


def test_init_storage():
    desired_path = Path(mkdtemp())
    # Let Storage create the directory structure
    desired_path.rmdir()

    id = str(UUID(int=0))
    artf1 = Artifact("sda.raw", "disk")
    artf1_contents = b"I am sda.raw"  # noqa: F841

    stg1 = Storage(desired_path)
    assert stg1.get_storage_path() == desired_path
    assert stg1.get_storage_info() == {"data_dir": str(desired_path), "tasks": []}
    stg1.add_task(Task(id))
    stg1.add_task_artifact(id, artf1)  # Use Session to add artifact

    # Storage should be able to run with the same folder
    stg2 = Storage(desired_path)  # noqa: F841
    # TODO: Fix the code to satisfy these tests
    # assert stg2.get_task(id) is not None
    # assert stg2.get_task_artifact_path(id, artf1) is not None

    # Cleanup
    rmtree(desired_path, ignore_errors=True)


# vim: set et ts=4 sw=4:
