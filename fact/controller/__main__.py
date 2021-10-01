import asyncio
import logging
from argparse import ArgumentParser

from . import Controller


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = ArgumentParser(description="FACT controller")
    parser.add_argument(
        "--listen-addr",
        default="localhost:5123",
        help="Address and port for the controller to listen on (Set to [::]:5123 to listen on all interfaces and families) (Default: localhost:5123)",
    )
    args = parser.parse_args()

    loop = asyncio.get_event_loop()

    c = Controller()
    try:
        loop.run_until_complete(c.start(args.listen_addr))
    except KeyboardInterrupt:
        loop.run_until_complete(c.stop(10))


# vim: set et ts=4 sw=4:
