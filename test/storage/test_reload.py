from fact.storage import Storage, Task

from pathlib import Path
from tempfile import mkdtemp
from uuid import UUID


def test_init_storage():
    desired_path = Path(mkdtemp())
    # Let Storage create the directory structure
    desired_path.rmdir()

    id = str(UUID(int=0))

    stg1 = Storage(desired_path)
    assert stg1.get_storage_path() == desired_path
    assert stg1.get_storage_info() == {"data_dir": str(desired_path), "tasks": []}
    stg1.add_task(Task(id))

    # Storage should be able to run with the same folder
    stg2 = Storage(desired_path)  # noqa: F841
    # TODO: Fix the code to satisfy this test
    # assert stg2.get_task(id) is not None

    # Cleanup
    desired_path.rmdir()


# vim: set et ts=4 sw=4:
