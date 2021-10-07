from uuid import UUID
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from fact.controller.database import Base, Worker, Target


def test_database_create_schema():
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        # Perform entire test within a transaction
        with session.begin():
            rows_all_workers = session.execute(select(Worker))
            assert rows_all_workers.all() == []

            rows_all_targets = session.execute(select(Target))
            assert rows_all_targets.all() == []


def test_database_create_target():
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        # Perform entire test within a transaction
        with session.begin():
            target = Target(uuid=UUID(int=0), hostname="hello-world")
            session.add(target)

            rows_all_targets = session.execute(select(Target)).scalars()
            all_targets = rows_all_targets.all()
            assert len(all_targets) == 1
            assert all_targets[0].uuid == UUID(int=0)
            assert all_targets[0].hostname == "hello-world"


# vim: set et ts=4 sw=4:
