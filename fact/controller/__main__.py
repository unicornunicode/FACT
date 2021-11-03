import asyncio
import logging
from argparse import ArgumentParser

from . import Controller


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = ArgumentParser(prog="fact.controller", description="FACT controller")
    parser.add_argument(
        "--debug",
        action="store_true",
    )
    parser.add_argument(
        "--listen-addr",
        default="localhost:5123",
        help="Address and port for the controller to listen on (Set to [::]:5123 to "
        "listen on all interfaces and families) "
        "(Default: localhost:5123)",
    )
    parser.add_argument(
        "--database-addr",
        default="sqlite+aiosqlite:///file:/var/lib/fact/controller.db?mode=rwc&uri=true",
        help="Database address (SQLAlchemy URL) to store the workers and tasks "
        "(Default: sqlite+aiosqlite:///file:/var/lib/fact/controller.db?mode=rwc&uri=true)",
    )
    parser.add_argument(
        "--elasticsearch-host",
        nargs="+",
        default=["http://elasticsearch:9200"],
        help="Elasticsearch hosts for search indexing "
        "(Default: http://elasticsearch:9200)",
    )
    args = parser.parse_args()
    print(args.elasticsearch_host)

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    loop = asyncio.get_event_loop()

    c = Controller(
        listen_addr=args.listen_addr,
        database_addr=args.database_addr,
        elasticsearch_hosts=args.elasticsearch_host,
    )
    try:
        loop.run_until_complete(c.start())
    except KeyboardInterrupt:
        loop.run_until_complete(c.stop(10))


# vim: set et ts=4 sw=4:
