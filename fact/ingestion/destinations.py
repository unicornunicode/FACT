from uuid import UUID
from typing import Iterable
from dataclasses import asdict

from .record import Record


class DestinationElasticsearch:
    def __init__(self, hosts: Iterable[str]):
        from elasticsearch import AsyncElasticsearch

        self._es = AsyncElasticsearch(hosts=list(hosts))

    async def index(self, task: UUID, target: str, artifact: str, record: Record):
        document = asdict(record)
        document["fact_task"] = str(task)
        document["fact_target"] = target
        document["fact_artifact"] = artifact
        await self._es.index(
            index=f"fact-{target}-{record.fact_type}",
            document=document,
            doc_type=record.fact_type,
        )


# vim: set et ts=4 sw=4:
