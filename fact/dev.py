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
    await asyncio.gather(c.stop(1), w.stop(), p.stop())


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    parser = ArgumentParser(description="FACT development server")
    parser.add_argument(
        "--storage-dir",
        default=Path("/tmp/fact"),
        type=Path,
        help="Folder to store SQLite database, collected disk images, memory "
        "snapshots and other data (Default: /tmp/fact)",
    )
    parser.add_argument(
        "--elasticsearch-host",
        nargs="+",
        default=["http://elasticsearch:9200"],
        help="Elasticsearch hosts for search indexing "
        "(Default: http://elasticsearch:9200)",
    )
    args = parser.parse_args()
    storage_dir: Path = args.storage_dir.absolute()
    database: Path = storage_dir / "controller.db"

    loop = asyncio.get_event_loop()

    # Ensure /tmp/fact is created for the database
    storage_dir.mkdir(exist_ok=True)

    c = Controller(
        listen_addr="localhost:5123",
        database_addr=f"sqlite+aiosqlite:///file:{database}?mode=rwc&uri=true",
        database_echo=True,
        elasticsearch_hosts=args.elasticsearch_host,
    )
    w = Worker(controller_addr=c.listen_addr, storage_dir=storage_dir)
    p = GRPCWebProxy(listen_addr="0.0.0.0:5124", controller_addr=c.listen_addr)
    try:
        loop.run_until_complete(start_all(c, w, p))
    except KeyboardInterrupt:
        loop.run_until_complete(stop_all(c, w, p))


# vim: set et ts=4 sw=4:
