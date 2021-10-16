from typing import Any


# Target related errors
class TargetError(Exception):
    pass


class SSHInfoError(TargetError):
    """Raised when SSH-related input fields are not supported or invalid"""

    def __init__(self, message: str, field: Any = ""):
        self.message = message
        self.field = field

    def __str__(self):
        return f"{self.message}: {self.field}"


class TargetRuntimeError(TargetError):
    """Raised when Errors occured during interaction or collection from target machines"""

    def __init__(self, message: str, field: Any = ""):
        self.message = message
        self.field = field

    def __str__(self):
        return f"{self.message}: {self.field}"


# Misc related errors
class MiscError(Exception):
    pass


class GzipDecompressionError(MiscError):
    """Raised when there is a problem with trying to decompress .gz files"""

    def __init__(self, message: str, field: Any = ""):
        self.message = message
        self.field = field

    def __str__(self):
        return f"{self.message}: {self.field}"
