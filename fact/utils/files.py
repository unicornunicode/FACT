import random
import time
import hashlib
import gzip
import os

from fact.exceptions import GzipDecompressionError


def create_random_file(output_path: str, filesize: int = 100000):
    """Creates a random bytefile of specified filesize, default 100000 bytes"""

    try:
        with open(output_path, "wb") as f:
            random.seed(time.time())
            b = random.randbytes(filesize)
            f.write(b)
            f.close()
    except OSError:
        raise


def calculatesha256sum(filepath: str) -> str:
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(8192), b""):
            sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()


def decompress_gzip(gz_path: str, output_filepath: str = None, keep_gz: bool = True):
    """
    :param gz_path: path of the gzip file. Requires the .gz extension
    :param output_filepath: Path+filename to save the file as.
        Defaults to the same directory and the same name (without .gz extension)
    :param keep_gz: Whether to keep the original gzip file. Defaults to True
    """
    if ".gz" not in gz_path:
        raise GzipDecompressionError(
            "Input file has no .gz extension (required)", gz_path
        )

    if output_filepath is None:
        output_filepath = os.path.splitext(gz_path)[0]

    try:
        inf = open(gz_path, mode="rb")
        outf = open(output_filepath, "wb")

        data = inf.read()
        outf.write(gzip.decompress(data))
        inf.close()
        outf.close()
    except gzip.BadGzipFile as e:
        raise GzipDecompressionError(
            "Error reading/processing gzip file", gz_path
        ) from e

    if not keep_gz:
        os.remove(gz_path)
