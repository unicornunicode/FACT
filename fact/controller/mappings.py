from ..controller_pb2 import CollectDiskSelector
from .database import CollectDiskSelectorGroup


# cdsg: CollectDiskSelector.Group
def collect_disk_selector_group_proto(cdsg) -> CollectDiskSelectorGroup:
    """
    >>> from ..controller_pb2 import CollectDiskSelector
    >>> from .database import CollectDiskSelectorGroup
    >>> assert (
    ...     collect_disk_selector_group_proto(CollectDiskSelector.Group.ALL_DISKS)
    ...     == CollectDiskSelectorGroup.ALL_DISKS
    ... )
    """
    if cdsg == CollectDiskSelector.Group.ALL_DISKS:
        return CollectDiskSelectorGroup.ALL_DISKS
    elif cdsg == CollectDiskSelector.Group.ROOT_DISK:
        return CollectDiskSelectorGroup.ROOT_DISK
    elif cdsg == CollectDiskSelector.Group.ROOT_PARTITION:
        return CollectDiskSelectorGroup.ROOT_PARTITION
    raise Exception("Unreachable: Invalid CollectDiskSelector.Group type")


# vim: set et ts=4 sw=4:
