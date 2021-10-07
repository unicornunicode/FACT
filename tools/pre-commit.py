#!/usr/bin/env python

from os import getenv
from utils import check


if __name__ == "__main__":
    skip_checks = getenv("SKIP_CHECKS", "").lower() == "y"

    check("poetry run black .")
    if not skip_checks:
        check("poetry run flake8 .")
        check("poetry run mypy .")
        check("poetry run python -m pytest")


# vim: set et ts=4 sw=4:
