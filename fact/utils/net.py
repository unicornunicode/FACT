from typing import Tuple


def split_addr(addr: str) -> Tuple[str, int]:
    host, _, port = addr.rpartition(":")
    return host, int(port)


# vim: set et ts=4 sw=4:
