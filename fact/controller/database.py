from datetime import datetime
from uuid import uuid4
import enum

from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import declarative_base

from .database_types import UUID

Base = declarative_base()


class Worker(Base):
    __tablename__ = "worker"

    uuid = Column(UUID, primary_key=True, nullable=False)
    hostname = Column(String, nullable=False)


class TaskStatus(enum.Enum):
    WAITING = "WAITING"
    RUNNING = "RUNNING"
    COMPLETE = "COMPLETE"


class TaskType(enum.Enum):
    task_none = "task_none"
    task_collect_disk = "task_collect_disk"
    task_collect_memory = "task_collect_memory"


class Task(Base):
    __tablename__ = "task"

    uuid = Column(UUID, default=uuid4, primary_key=True, nullable=False)
    status = Column(Enum(TaskStatus), default=TaskStatus.WAITING, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    assigned_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)

    type = Column(Enum(TaskType), nullable=False)
    target = Column(UUID, ForeignKey("target.uuid"), nullable=True)
    task_collect_disk_selector_path = Column(String, nullable=True)

    worker = Column(UUID, ForeignKey("worker.uuid"), nullable=True)


class Target(Base):
    __tablename__ = "target"

    uuid = Column(UUID, primary_key=True, nullable=False)
    name = Column(String, nullable=False)

    ssh_host = Column(String, nullable=True)
    ssh_user = Column(String, nullable=True)
    ssh_port = Column(Integer, nullable=True)
    ssh_private_key = Column(String, nullable=True)
    # sudo
    ssh_become = Column(Boolean, nullable=True)
    ssh_become_password = Column(String, nullable=True)


# vim: set et ts=4 sw=4:
