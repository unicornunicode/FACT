from __future__ import annotations

from ..controller_pb2 import CollectDiskSelector, ListTask
from .database import CollectDiskSelectorGroup, TaskStatus


def collect_disk_selector_group_from_proto(
    cdsg: CollectDiskSelector.Group.V,
) -> CollectDiskSelectorGroup:
    """
    >>> from ..controller_pb2 import CollectDiskSelector
    >>> from .database import CollectDiskSelectorGroup
    >>> assert (
    ...     collect_disk_selector_group_from_proto(CollectDiskSelector.Group.ALL_DISKS)
    ...     == CollectDiskSelectorGroup.ALL_DISKS
    ... )
    """
    if cdsg == CollectDiskSelector.Group.ALL_DISKS:
        return CollectDiskSelectorGroup.ALL_DISKS
    if cdsg == CollectDiskSelector.Group.ROOT_DISK:
        return CollectDiskSelectorGroup.ROOT_DISK
    if cdsg == CollectDiskSelector.Group.ROOT_PARTITION:
        return CollectDiskSelectorGroup.ROOT_PARTITION
    raise Exception("Unreachable: Invalid CollectDiskSelector.Group type")


def collect_disk_selector_group_from_db(
    cdsg: CollectDiskSelectorGroup,
) -> CollectDiskSelector.Group.V:
    """
    >>> from ..controller_pb2 import CollectDiskSelector
    >>> from .database import CollectDiskSelectorGroup
    >>> assert (
    ...     collect_disk_selector_group_from_db(CollectDiskSelectorGroup.ALL_DISKS)
    ...     == CollectDiskSelector.Group.ALL_DISKS
    ... )
    """
    if cdsg == CollectDiskSelectorGroup.ALL_DISKS:
        return CollectDiskSelector.Group.ALL_DISKS
    if cdsg == CollectDiskSelectorGroup.ROOT_DISK:
        return CollectDiskSelector.Group.ROOT_DISK
    if cdsg == CollectDiskSelectorGroup.ROOT_PARTITION:
        return CollectDiskSelector.Group.ROOT_PARTITION
    raise Exception("Unreachable: Invalid CollectDiskSelectorGroup type")


def task_status_from_db(ts: TaskStatus) -> ListTask.Status.V:
    """
    >>> from ..controller_pb2 import ListTask
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
