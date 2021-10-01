import asyncio
import logging

from . import Worker


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    loop = asyncio.get_event_loop()

    w = Worker("localhost:50051")
    try:
        loop.run_until_complete(w.start())
    except KeyboardInterrupt:
        loop.run_until_complete(w.stop())


# vim: set et ts=4 sw=4:
