import asyncio
from uuid import UUID
from dataclasses import asdict
from typing import Iterable

from .record import Record


class DestinationElasticsearch:
    def __init__(self, hosts: Iterable[str], max_simultaneous: int = 6):
        from elasticsearch import AsyncElasticsearch

        self._es = AsyncElasticsearch(hosts=list(hosts))
        self._submit_semaphore = asyncio.Semaphore(max_simultaneous)

    async def index(self, task: UUID, target: str, artifact: str, record: Record):
        await self._submit_semaphore.acquire()
        asyncio.create_task(self._index(task, target, artifact, record))

    async def _index(self, task: UUID, target: str, artifact: str, record: Record):
        document = asdict(record)
        document["fact_task"] = str(task)
        document["fact_target"] = target
        document["fact_artifact"] = artifact
        name = f"fact-{target}-{record.fact_type}"

        await self._es.index(
            index=name,
            document=document,
            doc_type=record.fact_type,
        )
        self._submit_semaphore.release()


# vim: set et ts=4 sw=4:
