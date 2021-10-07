from typing import Optional, List
from pathlib import Path
from shlex import quote
from sys import exit, stderr
from subprocess import run, CalledProcessError


def check(
    command: str,
    cwd: Path = None,
    check: bool = True,
    hide: bool = False,
    truncate: Optional[int] = None,
) -> None:
    show_command = command
    if truncate is not None and len(command) > truncate:
        show_command = command[:truncate] + "..."
    if not hide:
        print(f"> {show_command}", file=stderr)
    try:
        run(command, cwd=cwd, shell=True, check=check)
    except CalledProcessError as e:
        exit(e.returncode)


def args(files: List[str]) -> str:
    return " ".join(map(quote, files))


def git_staged() -> List[str]:
    git_diff = run(
        "git diff --staged --diff-filter=ACMR --name-only -z",
        shell=True,
        check=True,
        capture_output=True,
        encoding="utf8",
    )
    return git_diff.stdout.rstrip("\00").split("\00")


# vim: set et ts=4 sw=4:
