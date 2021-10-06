from typing import Union, cast, Iterable, AsyncIterable


async def chain(*iterables: Union[Iterable, AsyncIterable]) -> AsyncIterable:
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
