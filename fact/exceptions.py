from pathlib import Path


class FACTError:
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f"FACT error: {self.message}"


class UnreachableError(FACTError, AssertionError):
    pass


class LsblkParseError(FACTError, ValueError):
    def __init__(self, raw_data: bytes):
        super().__init__("Failed to parse lsblk data")
        self.raw_data = raw_data


class GzipExtensionError(FACTError, AssertionError):
    def __init__(self, path: Path):
        super().__init__(f"Path {path} should end with .gz")


class GzipDecompressionError(FACTError, ValueError):
    def __init__(self, path: Path):
        super().__init__(f"Failed to decompress gzipped data at {path}")


class StorageModuleException(Exception):
    """Base class for Storage module exceptions"""

    def __init__(self, message: str, field: str):
        self.message = message
        self.field = field

    def __str__(self):
        return f"{self.field} -> {self.message}"


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
