import logging
import re
import os
from subprocess import Popen, DEVNULL, PIPE
from contextlib import contextmanager
from tempfile import NamedTemporaryFile
from typing import IO, Tuple, List, Sequence, Generator

from ..exceptions import UnreachableError, LsblkParseError
from ..storage import Session
from .types import TargetAccess

log = logging.getLogger(__name__)


def _parse_lsblk_output(raw_lsblk_data: bytes) -> List[Tuple[str, int, str, str]]:
    """
    Converts the lsblk_data from commandline and save relevant info in a dict
    Assumes the "lsblk -lb" returns in the following format:
        NAME  MAJ:MIN  RM  SIZE  RO  TYPE  MOUNTPOINT

    Output in the following format:
    [
        ("dev_name", size, "type", "mountpoint"),
    ]

    eg: [("sda2", 200000, "part", "/"),(...)]
    """

    lsblk_data = raw_lsblk_data.decode("utf-8")
    # Remove header
    split_lsblk_data = lsblk_data.split("\n")[1:]

    entries = []
    for entry in split_lsblk_data:
        if entry == "":
            continue
        cleaned_entry = re.split("[ ]+", entry)
        entries.append(
            (
                cleaned_entry[0],  # Device name
                int(cleaned_entry[3]),  # Size
                cleaned_entry[5],  # Type
                cleaned_entry[6],  # Mountpoint
            )
        )
    return entries


class SSHTargetAccess(TargetAccess):
    def __init__(self, host: str, user: str, port: int, private_key: str):
        self.host = host
        self.user = user
        self.port = port
        self.private_key = private_key

    @contextmanager
    def do_ssh(
        self, command: Sequence[str], bufsize: int = 65535
    ) -> Generator[IO[bytes], None, None]:
        with NamedTemporaryFile("w") as f:
            f.write(self.private_key)
            if not self.private_key.endswith("\n"):
                f.write("\n")
            f.flush()
            private_key_file = f.name
            os.chmod(private_key_file, 0o600)

            args = [
                "ssh",
                "-o",
                "StrictHostKeyChecking=no",
                "-i",
                private_key_file,
                "-l",
                self.user,
                "-p",
                str(self.port),
                self.host,
            ]
            args.extend(command)

            with Popen(
                args, stdin=DEVNULL, stdout=PIPE, stderr=None, bufsize=bufsize
            ) as process:
                if process.stdout is None:
                    raise UnreachableError("process stdout is None")
                yield process.stdout

    def collect_image(
        self, remote_path_of_image: str, storage_session: Session, bufsize: int = 65535
    ) -> None:
        """
        Collects the image of a file. Can be a disk, or process, or file in general.
            The remote user must have root priv.
        :param remote_path_to_image: Path of the remote image to copy out
        :param storage_session: Storage Session
        """

        command = ("dd", f"if=/dev/{remote_path_of_image}", " | gzip -1 -")
        with self.do_ssh(command, bufsize=bufsize) as stdout:
            while buf := stdout.read(bufsize):
                storage_session.write(buf)

    def get_all_available_disk(self) -> List[Tuple[str, int, str, str]]:
        """
        Gets a list of availale disks on the remote machine
        :return: lsblk information as list of tuple
        """

        command = ("lsblk -lb",)
        with self.do_ssh(command) as stdout:
            raw_lsblk_data = stdout.read()

        try:
            return _parse_lsblk_output(raw_lsblk_data)
        except Exception as e:
            raise LsblkParseError(raw_lsblk_data) from e


# vim: set et ts=4 sw=4:
