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


class TaskExistsError(FACTError, Exception):
    def __init__(self, message: str, task_uuid: str):
        """Exception if Task exists"""
        super().__init__(f"{task_uuid} -> {message}")


class TaskNotFoundError(FACTError, Exception):
    def __init__(self, message: str, task_uuid: str):
        """Exception if Task not found"""
        super().__init__(f"{task_uuid} -> {message}")


class TaskInvalidUUID(FACTError, Exception):
    def __init__(self, message: str, task_uuid: str):
        """Exception if Task has invalid UUID"""
        super().__init__(f"{task_uuid} -> {message}")


class ArtifactExistsError(FACTError, Exception):
    def __init__(self, message: str, artifact_info: dict):
        """Exception if Artifact exists"""
        super().__init__(f"{str(artifact_info)} -> {message}")


class ArtifactNotFoundError(FACTError, Exception):
    def __init__(self, message: str, artifact_info: dict):
        """Exception if Artifact not found"""
        super().__init__(f"{str(artifact_info)} -> {message}")


class ArtifactInvalidName(FACTError, Exception):
    def __init__(self, message: str, artifact_name: str):
        """Exception if Artifact has invalid name"""
        super().__init__(f"{artifact_name} -> {message}")


class ArtifactInvalidType(FACTError, Exception):
    def __init__(self, message: str, artifact_type: str):
        """Exception if Artifact has invalid type"""
        super().__init__(f"{artifact_type} -> {message}")


class LoopDeviceSetupError(FACTError, Exception):
    """Exception if loop device fails to setup"""

    pass


class LoopDeviceDetachError(FACTError, Exception):
    """Exception if loop device fails to detach"""

    pass


class UnmountPartitionError(FACTError, Exception):
    """Exception if partition fails to unmount"""

    pass
