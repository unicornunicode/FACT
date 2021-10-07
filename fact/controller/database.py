from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

from .database_types import UUID

Base = declarative_base()


class Worker(Base):
    __tablename__ = "worker"

    uuid = Column(UUID, primary_key=True, nullable=False)
    hostname = Column(String, nullable=False)


class Target(Base):
    __tablename__ = "target"

    uuid = Column(UUID, primary_key=True, nullable=False)
    hostname = Column(String, nullable=False)


# vim: set et ts=4 sw=4:
