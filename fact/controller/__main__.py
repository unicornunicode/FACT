import asyncio
import logging

from . import Controller


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    loop = asyncio.get_event_loop()

    c = Controller()
    try:
        loop.run_until_complete(c.start("[::]:50051"))
    except KeyboardInterrupt:
        loop.run_until_complete(c.stop(10))


# vim: set et ts=4 sw=4:
