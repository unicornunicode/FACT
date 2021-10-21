import asyncio
from typing import TypeVar, Generic, AsyncIterator, AsyncIterable

T = TypeVar("T")


class Stream(AsyncIterator[T], AsyncIterable[T], Generic[T]):
    """
    AsyncIterator for elements of type T, implemented using asyncio.Queue

    >>> from typing import AsyncIterable, List, Tuple
    >>> from asyncio import run
    >>> async def read_n(n: int, i: AsyncIterable) -> List:
    ...     l = []
    ...     async for a in i:
    ...         l.append(a)
    ...         if len(l) >= n:
    ...             break
    ...     return l
    >>> async def example_1() -> List:
    ...     s = Stream()
    ...     await s.add(1)
    ...     await s.add(2)
    ...     await s.add(3)
    ...     return await read_n(3, s)
    >>> run(example_1())
    [1, 2, 3]
    >>> async def example_2() -> Tuple:
    ...     s = Stream()
    ...     await s.add(1)
    ...     a = await read_n(1, s)
    ...     await s.add(2)
    ...     await s.add(3)
    ...     b = await read_n(2, s)
    ...     return a, b
    >>> run(example_2())
    ([1], [2, 3])
    """

    def __init__(self):
        self.queue = asyncio.Queue()

    async def add(self, item: T):
        """
        Add elements to the stream

        >>> from asyncio import run
        >>> async def example_1():
        ...     s = Stream()
        ...     await s.add(1)
        >>> run(example_1())
        """
        await self.queue.put(item)

    def __aiter__(self):
        return self

    async def __anext__(self) -> T:
        return await self.queue.get()


# vim: set et ts=4 sw=4:
