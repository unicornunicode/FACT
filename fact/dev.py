import asyncio
import logging
from argparse import ArgumentParser

from .controller import Controller
from .worker import Worker


async def start_all(c: Controller, w: Worker) -> None:
    tasks = [asyncio.create_task(t) for t in (c.start(), w.start())]
    await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    logging.warning("One or more tasks ended")
    await stop_all(c, w)


async def stop_all(c: Controller, w: Worker) -> None:
    await asyncio.gather(c.stop(10), w.stop())


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    parser = ArgumentParser(description="FACT development server")
    args = parser.parse_args()

    loop = asyncio.get_event_loop()

    c = Controller(listen_addr="localhost:5123")
    w = Worker(controller_addr="localhost:5123")
    try:
        loop.run_until_complete(start_all(c, w))
    except KeyboardInterrupt:
        loop.run_until_complete(stop_all(c, w))


# vim: set et ts=4 sw=4:
