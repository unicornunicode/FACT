from typing import Any


class FACTError(Exception):
    def __init__(self, message: str, affected_field: Any = ""):
        self.message = message
        self.affected_field = affected_field

    def __str__(self):
        return f"{self.message}: {self.affected_field}"


# Target related errors
class TargetError(Exception):
    pass


class SSHInfoError(FACTError, TargetError):
    """Raised when SSH-related input fields are not supported or invalid"""

    pass


class TargetRuntimeError(FACTError, TargetError):
    """Raised when Errors occured during interaction or collection from target machines"""

    pass


# Misc related errors
class MiscError(Exception):
    pass


class GzipDecompressionError(FACTError, MiscError):
    """Raised when there is a problem with trying to decompress .gz files"""

    pass


class FileExistsError(FACTError, MiscError):
    """Raised when a file already exists and should not be overwritten"""

    pass
