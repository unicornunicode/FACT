import logging
import re
from typing import Tuple, List
import subprocess

from fact.storage import Session

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


class SSHAccessInfo:
    """Core information needed for SSH connection to the target."""

    __slots__ = "user", "host", "port", "privateKey_path"

    def __init__(
        self,
        user: str,
        host: str,
        port: str,
        privateKey_path: str,
    ):
        self.user = user
        self.host = host
        self.port = port
        self.privateKey_path = privateKey_path


class TargetEndpoint:
    def __init__(self, SSHAccessInfo: SSHAccessInfo):
        self.SSHAccessInfo = SSHAccessInfo

    def collect_image(
        self, remote_path_of_image: str, storage_session: Session
    ) -> None:
        """
        Collects the image of a file. Can be a disk, or process, or file in general.
            The remote user must have root priv.
        :param remote_path_to_image: Path of the remote image to copy out
        :param storage_session: Storage Session
        """

        dd_if = "if=" + remote_path_of_image

        # This assumes that the remote sudo does not require further password authentication
        # This also requires that the user has the private key (compulsory)
        with subprocess.Popen(
            [
                "ssh",
                "-i",
                self.SSHAccessInfo.privateKey_path,
                "-l",
                self.SSHAccessInfo.user,
                "-p",
                self.SSHAccessInfo.port,
                self.SSHAccessInfo.host,
                "sudo dd",
                dd_if,
                "| gzip -1 -",
            ],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        ) as p:
            if p.stdout is None:
                raise Exception("Unreachable: Process stdout is None")

            while True:
                res = p.stdout.read()
                if not res:
                    break
                storage_session.write(res)

    def get_all_available_disk(self) -> List[Tuple[str, int, str, str]]:
        """
        Gets a list of availale disks on the remote machine
        :return: lsblk information as list of tuple
        """
        lsblk_command = "lsblk -lb"
        raw_lsblk_data = b""
        with subprocess.Popen(
            [
                "ssh",
                "-i",
                self.SSHAccessInfo.privateKey_path,
                "-l",
                self.SSHAccessInfo.user,
                "-p",
                self.SSHAccessInfo.port,
                self.SSHAccessInfo.host,
                lsblk_command,
            ],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        ) as p:
            if p.stdout is None:
                raise Exception("Unreachable: Process stdout is None")

            while True:
                res = p.stdout.read()
                if not res:
                    break
                raw_lsblk_data += res

        lsblk_list = _parse_lsblk_output(raw_lsblk_data)
        return lsblk_list
