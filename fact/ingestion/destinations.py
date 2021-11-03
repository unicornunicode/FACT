from uuid import UUID
from typing import Iterable
from dataclasses import asdict

from .record import Record


class DestinationElasticsearch:
    def __init__(self, hosts: Iterable[str]):
        from elasticsearch import AsyncElasticsearch

        self._es = AsyncElasticsearch(hosts=list(hosts))

    async def index(self, task: UUID, record: Record):
        document = asdict(record)
        document["task"] = str(task)
        # TODO: Include Target in document
        await self._es.index(
            index="fact",
            document=document,
            doc_type=record.fact_type,
        )


# vim: set et ts=4 sw=4:
