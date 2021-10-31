from typing import Optional, Iterable, Generator
from pathlib import Path
from contextlib import contextmanager
from tempfile import NamedTemporaryFile
from urllib.request import urlopen
from shlex import quote
from sys import exit, stderr
from subprocess import run, CalledProcessError


root = Path(__file__).parent.parent


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


def args(files: Iterable[str]) -> str:
    return " ".join(map(quote, files))


def git_staged() -> Iterable[str]:
    git_diff = run(
        "git diff --staged --diff-filter=ACMR --name-only -z",
        shell=True,
        check=True,
        capture_output=True,
        encoding="utf8",
    )
    return filter(bool, git_diff.stdout.split("\00"))


def copy(dst, src, bufsize=1024 * 16) -> Generator[int, None, None]:
    counter = 0
    while buf := src.read(bufsize):
        counter += len(buf)
        dst.write(buf)
        yield counter


@contextmanager
def download_temporary(url: str) -> Generator[Path, None, None]:
    with NamedTemporaryFile() as tmpfile:
        with urlopen(url) as request:
            size = request.headers["Content-Length"]
            for counter in copy(tmpfile, request):
                print(f"\rdownload: {counter} / {size}", end="")
            print()
        yield Path(tmpfile.name)


# vim: set et ts=4 sw=4:
