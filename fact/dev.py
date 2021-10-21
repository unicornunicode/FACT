import asyncio
import logging
from pathlib import Path
from argparse import ArgumentParser
from typing import TypeVar, Awaitable

from .controller import Controller
from .worker import Worker
from .grpcwebproxy import GRPCWebProxy


T = TypeVar("T")


async def delay(t: Awaitable[T], delay: float) -> T:
    await asyncio.sleep(delay)
    return await t


async def start_all(c: Controller, w: Worker, p: GRPCWebProxy) -> None:
    tasks = [
        asyncio.create_task(t)
        for t in (c.start(), delay(w.start(), 1), delay(p.start(), 1))
    ]
    await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    logging.warning("One or more tasks ended")
    await stop_all(c, w, p)


async def stop_all(c: Controller, w: Worker, p: GRPCWebProxy) -> None:
    await asyncio.gather(c.stop(10), w.stop(), p.stop())


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    parser = ArgumentParser(description="FACT development server")
    args = parser.parse_args()

    loop = asyncio.get_event_loop()

    # Ensure /tmp/fact is created
    Path("/tmp/fact").mkdir(exist_ok=True)

    c = Controller(
        listen_addr="localhost:5123",
        database_addr="sqlite+aiosqlite:///file:/tmp/fact/controller.db?mode=rwc&uri=true",
        database_echo=True,
    )
    w = Worker(controller_addr=c.listen_addr, storage_dir=Path("/tmp/fact"))
    p = GRPCWebProxy(listen_addr="0.0.0.0:5124", controller_addr=c.listen_addr)
    try:
        loop.run_until_complete(start_all(c, w, p))
    except KeyboardInterrupt:
        loop.run_until_complete(stop_all(c, w, p))


# vim: set et ts=4 sw=4:
