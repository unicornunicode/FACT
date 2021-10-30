import gzip

from pathlib import Path

from fact.exceptions import GzipExtensionError, GzipDecompressionError


def decompress_gzip(gz_path: Path, output_filepath: Path = None, keep_gz: bool = True):
    """
    :param gz_path: path of the gzip file. Requires the .gz extension
    :param output_filepath: Path+filename to save the file as.
        Defaults to the same directory and the same name (without .gz extension)
    :param keep_gz: Whether to keep the original gzip file. Defaults to True
    """

    if ".gz" not in gz_path.suffix:
        raise GzipExtensionError(gz_path)

    if output_filepath is None:
        output_filepath = gz_path.with_suffix("")

    try:
        inf = open(gz_path, mode="rb")
        outf = open(output_filepath, "wb")

        data = inf.read()
        outf.write(gzip.decompress(data))
        inf.close()
        outf.close()
    except gzip.BadGzipFile as e:
        raise GzipDecompressionError(gz_path) from e

    if not keep_gz:
        gz_path.unlink()
