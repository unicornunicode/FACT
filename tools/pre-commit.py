#!/usr/bin/env python

from pathlib import Path
from shutil import which
from os import getenv
from utils import check, args, git_staged


if __name__ == "__main__":
    skip_checks = getenv("SKIP_CHECKS", "").lower() == "y"
    staged = git_staged()

    staged_py = [f for f in staged if f.endswith(".py")]

    if staged_py:
        check(f"poetry run black {args(staged_py)}")
    if not skip_checks:
        if staged_py:
            check(f"poetry run flake8 {args(staged_py)}")
            check(f"poetry run mypy {args(staged_py)}")
        check("poetry run python -m pytest")

    ui = Path("ui")

    if which("npm") is not None and (ui / "node_modules").exists():
        check("npm run format", cwd=ui, check=not skip_checks)
        if not skip_checks:
            check("npm run type-check", cwd=ui)

    if staged:
        check(f"git add {args(staged)}")


# vim: set et ts=4 sw=4:
