from pathlib import Path
from uuid import uuid4

from fact.target import SSHTargetAccess
from fact.storage import FilesystemStorage

import logging

logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    username = "your_remote_username"
    host = "127.0.0.1"
    port = 22
    pkey = """
-----BEGIN OPENSSH PRIVATE KEY-----
...
-----END OPENSSH PRIVATE KEY-----
"""

    artefact_name = "name"
    storage_folder = Path("/path/to/folder")
    test_keywords = [""]

    s = FilesystemStorage(storage_folder)

    target = SSHTargetAccess(
        host=host, user=username, port=port, private_key=pkey, become=True
    )

    if "image" in test_keywords:
        with s.writer(uuid4(), artefact_name, "disk") as f:
            remote_image_path = "/dev/loop2"
            target.collect_image(remote_image_path, f)

    if "lsblk" in test_keywords:
        dic = target.get_all_available_disk()
        print(dic)
