#!/usr/bin/env python

from sys import argv
from shlex import quote
from utils import check


if __name__ == "__main__":
    with open(argv[1], "r") as f:
        commit_msg = quote(f.read())
    check(f"poetry run mkcommit -x {commit_msg} --autoselect", truncate=19)


# vim: set et ts=4 sw=4:
