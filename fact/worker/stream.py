import asyncio
from typing import TypeVar, Generic

T = TypeVar("T")


class Stream(Generic[T]):
    def __init__(self):
        self.queue = asyncio.Queue()

    async def add(self, item: T):
        await self.queue.put(item)

    def __aiter__(self):
        return self

    async def __anext__(self) -> T:
        return await self.queue.get()


# vim: set et ts=4 sw=4:
