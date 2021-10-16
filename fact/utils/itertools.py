from typing import Union, cast, Iterable, AsyncIterable


async def chain(*iterables: Union[Iterable, AsyncIterable]) -> AsyncIterable:
    """
    Chain Iterables or AsyncIterables after each other

    >>> from typing import List
    >>> from asyncio import run
    >>> async def read_all(i: AsyncIterable) -> List:
    ...     l = []
    ...     async for a in i:
    ...         l.append(a)
    ...     return l
    >>> run(read_all(chain([1, 2], [3])))
    [1, 2, 3]
    >>> run(read_all(chain([1, 2], chain([3, 4], [5]))))
    [1, 2, 3, 4, 5]
    """
    for i in iterables:
        if hasattr(i, "__aiter__"):
            i = cast(AsyncIterable, i)
            async for v in i:
                yield v
        else:
            i = cast(Iterable, i)
            for v in i:
                yield v


# vim: set et ts=4 sw=4:
