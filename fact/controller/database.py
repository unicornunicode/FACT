from datetime import datetime
import enum

from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import declarative_base

from .database_types import UUID

Base = declarative_base()


class Worker(Base):
    __tablename__ = "worker"

    uuid = Column(UUID, primary_key=True, nullable=False)
    hostname = Column(String, nullable=False)


class CollectDiskSelectorGroup(enum.Enum):
    ALL_DISKS = 0
    ROOT_DISK = 1
    ROOT_PARTITION = 2


class Task(Base):
    __tablename__ = "task"

    uuid = Column(UUID, primary_key=True, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.utcnow(), nullable=False)
    completed_at = Column(DateTime, default=None, nullable=True)

    none = Column(Boolean, nullable=True)
    collect_disk_target = Column(UUID, ForeignKey("target.uuid"), nullable=True)
    collect_disk_selector_group = Column(Enum(CollectDiskSelectorGroup), nullable=True)
    collect_memory_target = Column(UUID, ForeignKey("target.uuid"), nullable=True)

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
