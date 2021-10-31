#!/usr/bin/env python

from zipfile import ZipFile

from utils import root, download_temporary, copy

VERSION = "0.14.1"
PLATFORM = "linux-x86_64"
URL = (
    "https://github.com/improbable-eng/grpc-web"
    f"/releases/download/v{VERSION}/grpcwebproxy-v{VERSION}-{PLATFORM}.zip"
)
BIN = root / "fact" / "grpcwebproxy" / "grpcwebproxy"


if __name__ == "__main__":
    with download_temporary(URL) as archivepath:
        with ZipFile(archivepath) as archive:
            for info in archive.infolist():
                if "grpcwebproxy" in info.filename:
                    break
            with archive.open(info.filename) as zipbin, open(BIN, "wb") as file:
                size = info.file_size
                for counter in copy(file, zipbin):
                    print(f"\rextract: {counter} / {size}", end="")
                print()
    BIN.chmod(0o755)


# vim: set et ts=4 sw=4:
