from typing import Optional
from sys import exit, stderr
from subprocess import run, CalledProcessError


def check(command: str, hide: bool = False, truncate: Optional[int] = None) -> None:
    show_command = command
    if truncate is not None and len(command) > truncate:
        show_command = command[:truncate] + "..."
    if not hide:
        print(f"> {show_command}", file=stderr)
    try:
        run(command, shell=True, check=True)
    except CalledProcessError as e:
        exit(e.returncode)


# vim: set et ts=4 sw=4:
