import asyncio
import logging
from pathlib import Path
from argparse import ArgumentParser

from . import Worker


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = ArgumentParser(prog="fact.worker", description="FACT worker")
    parser.add_argument(
        "--debug",
        action="store_true",
    )
    parser.add_argument(
        "--controller-addr",
        default="localhost:5123",
        help="Address and port of the controller for the worker to connect to "
        "(Default: localhost:5123)",
    )
    parser.add_argument(
        "--storage-dir",
        default=Path("/var/lib/fact"),
        type=Path,
        help="Folder to store collected disk images, memory snapshots and other data "
        "(Default: /var/lib/fact)",
    )
    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    loop = asyncio.get_event_loop()

    w = Worker(controller_addr=args.controller_addr, storage_dir=args.storage_dir)
    try:
        loop.run_until_complete(w.start())
    except KeyboardInterrupt:
        loop.run_until_complete(w.stop())


# vim: set et ts=4 sw=4:
