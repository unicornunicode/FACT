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
