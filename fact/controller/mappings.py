from __future__ import annotations

from google.protobuf.timestamp_pb2 import Timestamp

from ..management_pb2 import ListTask, ListTarget
from ..tasks_pb2 import (
    SSHAccess,
    TaskCollectDisk,
    TaskCollectMemory,
    TaskCollectDiskinfo,
    TaskIngest,
)
from .database import TaskStatus, TaskType, Task, Target


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


def task_from_db(task: Task) -> ListTask:
    assert task.uuid is not None
    assert task.status is not None
    assert task.created_at is not None
    created_at = Timestamp(seconds=int(task.created_at.timestamp()))
    assigned_at = (
        Timestamp(seconds=int(task.assigned_at.timestamp()))
        if task.assigned_at is not None
        else None
    )
    completed_at = (
        Timestamp(seconds=int(task.completed_at.timestamp()))
        if task.completed_at is not None
        else None
    )
    target = task.target.bytes if task.target is not None else None
    task_collect_disk = (
        TaskCollectDisk(device_name=task.task_collect_disk_device_name)
        if task.type == TaskType.task_collect_disk
        and task.task_collect_disk_device_name is not None
        else None
    )
    task_collect_memory = (
        TaskCollectMemory() if task.type == TaskType.task_collect_memory else None
    )
    task_collect_diskinfo = (
        TaskCollectDiskinfo() if task.type == TaskType.task_collect_diskinfo else None
    )
    task_ingest = (
        TaskIngest(collected_uuid=task.task_ingest_collected_uuid.bytes)
        if task.type == TaskType.task_ingest
        and task.task_ingest_collected_uuid is not None
        else None
    )
    worker = task.worker.bytes if task.worker is not None else None
    return ListTask(
        uuid=task.uuid.bytes,
        status=task_status_from_db(task.status),
        created_at=created_at,
        assigned_at=assigned_at,
        completed_at=completed_at,
        target=target,
        task_collect_disk=task_collect_disk,
        task_collect_memory=task_collect_memory,
        task_collect_diskinfo=task_collect_diskinfo,
        task_ingest=task_ingest,
        worker=worker,
    )


def target_from_db(target: Target) -> ListTarget:
    assert target.uuid is not None
    ssh = (
        SSHAccess(
            host=target.ssh_host or "",
            user=target.ssh_user or "",
            port=target.ssh_port or 0,
            private_key=target.ssh_private_key or "",
            become=target.ssh_become or False,
            become_password=target.ssh_become_password or "",
        )
        if target.ssh_host is not None
        else None
    )
    return ListTarget(
        uuid=target.uuid.bytes,
        name=target.name or "",
        ssh=ssh,
    )


# vim: set et ts=4 sw=4:
