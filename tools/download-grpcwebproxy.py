#!/usr/bin/env python

from typing import Generator
from urllib.request import urlopen
from tempfile import TemporaryDirectory
from zipfile import ZipFile
from pathlib import Path

VERSION = "0.14.1"
PLATFORM = "linux-x86_64"
URL = (
    "https://github.com/improbable-eng/grpc-web"
    f"/releases/download/v{VERSION}/grpcwebproxy-v{VERSION}-{PLATFORM}.zip"
)
BIN = Path("fact", "grpcwebproxy", "grpcwebproxy")


def copy(dst, src) -> Generator[int, None, None]:
    counter = 0
    while buf := src.read(8192):
        counter += len(buf)
        dst.write(buf)
        yield counter


if __name__ == "__main__":
    try:
        with TemporaryDirectory() as tmpdir:
            zippath = Path(tmpdir, "grpcwebproxy.zip")
            with open(zippath, "wb") as downloadfile, urlopen(URL) as request:
                size = request.headers["Content-Length"]
                for counter in copy(downloadfile, request):
                    print(f"\rdownload: {counter} / {size}", end="")
                print()
            with ZipFile(zippath) as zipfile:
                for info in zipfile.infolist():
                    if "grpcwebproxy" in info.filename:
                        break
                with zipfile.open(info.filename) as zipbin, open(BIN, "wb") as file:
                    size = info.file_size
                    for counter in copy(file, zipbin):
                        print(f"\rextract: {counter} / {size}", end="")
                    print()
        BIN.chmod(0o755)
    except Exception as e:
        print(e)
        exit(1)


# vim: set et ts=4 sw=4:
