import pytest
from datetime import datetime, timedelta
from uuid import UUID

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from fact.controller.database import Base, Worker, Task, Target


@pytest.fixture
def engine():
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
    Base.metadata.create_all(engine)
    return engine


def test_database_create_schema(engine):
    with Session(engine) as session:
        # Perform entire test within a transaction
        with session.begin():
            rows_all_workers = session.execute(select(Worker))
            assert rows_all_workers.all() == []

            rows_all_targets = session.execute(select(Target))
            assert rows_all_targets.all() == []


def test_database_create_task(engine):
    with Session(engine) as session:
        # Perform entire test within a transaction
        with session.begin():
            now = datetime.utcnow()
            task = Task(uuid=UUID(int=0))
            session.add(task)

            rows_all_tasks = session.execute(select(Task)).scalars()
            all_tasks = rows_all_tasks.all()
            assert len(all_tasks) == 1
            assert all_tasks[0].uuid == UUID(int=0)
            assert all_tasks[0].created_at - now < timedelta(seconds=10)
            assert all_tasks[0].completed_at is None

        with session.begin():
            # Test again after closing the transaction. This ensures that the
            # object goes through a full decode and encode.
            rows_all_tasks = session.execute(select(Task)).scalars()
            all_tasks = rows_all_tasks.all()
            assert len(all_tasks) == 1
            assert all_tasks[0].created_at - now < timedelta(seconds=10)


def test_database_create_target(engine):
    with Session(engine) as session:
        # Perform entire test within a transaction
        with session.begin():
            target = Target(uuid=UUID(int=0), name="hello-world")
            session.add(target)

            rows_all_targets = session.execute(select(Target)).scalars()
            all_targets = rows_all_targets.all()
            assert len(all_targets) == 1
            assert all_targets[0].uuid == UUID(int=0)
            assert all_targets[0].name == "hello-world"


# vim: set et ts=4 sw=4:
