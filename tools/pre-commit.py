#!/usr/bin/env python

from pathlib import Path
from shutil import which
from os import getenv
from utils import check


if __name__ == "__main__":
    skip_checks = getenv("SKIP_CHECKS", "").lower() == "y"

    check("poetry run black .")
    if not skip_checks:
        check("poetry run flake8 .")
        check("poetry run mypy .")
        check("poetry run python -m pytest")

    ui = Path("ui")
    if which("npm") is not None:
        check("npm run format", cwd=ui)
        check("npm run type-check", cwd=ui)


# vim: set et ts=4 sw=4:
