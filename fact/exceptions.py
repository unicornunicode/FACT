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

class StorageModuleException(Exception):
    """Base class for Storage module exceptions"""

    def __init__(self, message: str, field: str):
        self.message = message
        self.field = field

    def __str__(self):
        return f"{self.field} -> {self.message}"


class DirectoryExistsError(StorageModuleException):
    def __init__(self, message: str, storage_path: str):
        """Exception if directory exists"""
        super().__init__(message, storage_path)


class StorageExistsError(StorageModuleException):
    def __init__(self, message: str, storage_path: str):
        """Exception if Storage exists"""
        super().__init__(message, storage_path)


class TaskExistsError(StorageModuleException):
    def __init__(self, message: str, task_uuid: str):
        """Exception if Task exists"""
        super().__init__(message, task_uuid)


class TaskNotFoundError(StorageModuleException):
    def __init__(self, message: str, task_uuid: str):
        """Exception if Task not found"""
        super().__init__(message, task_uuid)


class TaskInvalidUUID(StorageModuleException):
    def __init__(self, message: str, task_uuid: str):
        """Exception if Task has invalid UUID"""
        super().__init__(message, task_uuid)


class ArtifactExistsError(StorageModuleException):
    def __init__(self, message: str, artifact_info: dict):
        """Exception if Artifact exists"""
        super().__init__(message, str(artifact_info))


class ArtifactNotFoundError(StorageModuleException):
    def __init__(self, message: str, artifact_info: dict):
        """Exception if Artifact not found"""
        super().__init__(message, str(artifact_info))


class ArtifactInvalidName(StorageModuleException):
    def __init__(self, message: str, artifact_name: str):
        """Exception if Artifact has invalid name"""
        super().__init__(message, artifact_name)


class ArtifactInvalidType(StorageModuleException):
    def __init__(self, message: str, artifact_type: str):
        """Exception if Artifact has invalid type"""
        super().__init__(message, artifact_type)


class ArtifactInvalidSubType(StorageModuleException):
    def __init__(self, message: str, sub_type: str):
        """Exception if Artifact has invalid sub type"""
        super().__init__(message, sub_type)
