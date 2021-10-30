from pathlib import Path
from uuid import uuid4

from fact.target import (
    SSHTargetAccess,
)
from fact.storage import Session, Artifact, Task, Storage

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
    artefact_type = "disk"
    storage_folder = "/path/to/folder"
    test_keywords = [""]

    a = Artifact(artefact_name, artefact_type)
    t = Task(str(uuid4()))
    s = Storage(Path(storage_folder))

    target = SSHTargetAccess(host=host, user=username, port=port, private_key=pkey)

    if "image" in test_keywords:
        with Session(s, t, a) as sess:
            remote_image_path = "/dev/loop2"
            target.collect_image(remote_image_path, sess)

    if "lsblk" in test_keywords:
        dic = target.get_all_available_disk()
        print(dic)
