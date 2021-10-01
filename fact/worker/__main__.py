import asyncio
import logging
from argparse import ArgumentParser

from . import Worker


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = ArgumentParser(description="FACT worker")
    parser.add_argument(
        "--controller-addr",
        default="localhost:5123",
        help="Address and port of the controller for the worker to connect to "
        "(Default: localhost:5123)",
    )
    args = parser.parse_args()

    loop = asyncio.get_event_loop()

    w = Worker(controller_addr=args.controller_addr)
    try:
        loop.run_until_complete(w.start())
    except KeyboardInterrupt:
        loop.run_until_complete(w.stop())


# vim: set et ts=4 sw=4:
