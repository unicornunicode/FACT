from __future__ import annotations

from ..management_pb2 import ListTask
from .database import TaskStatus


def task_status_from_db(ts: TaskStatus) -> ListTask.Status.V:
    """
    >>> from ..management_pb2 import ListTask
    >>> from .database import TaskStatus
    >>> assert (
    ...     task_status_from_db(TaskStatus.COMPLETE)
    ...     == ListTask.Status.COMPLETE
    ... )
    """
    if ts == TaskStatus.WAITING:
        return ListTask.Status.WAITING
    if ts == TaskStatus.RUNNING:
        return ListTask.Status.RUNNING
    if ts == TaskStatus.COMPLETE:
        return ListTask.Status.COMPLETE
    raise Exception("Unreachable: Invalid TaskStatus type")


# vim: set et ts=4 sw=4:
