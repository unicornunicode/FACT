import gzip
import os

from fact.exceptions import GzipDecompressionError


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
