class StorageModuleException(Exception):
    def __init__(self, message: str, field: str):
        self.message = message
        self.field = field

    def __str__(self):
        return f"{self.field} -> {self.message}"


class DirectoryExistsError(StorageModuleException):
    def __init__(self, message: str, storage_path: str):
        super().__init__(message, storage_path)


class StorageExistsError(StorageModuleException):
    def __init__(self, message: str, storage_path: str):
        super().__init__(message, storage_path)


class TaskExistsError(StorageModuleException):
    def __init__(self, message: str, task_uuid: str):
        super().__init__(message, task_uuid)


class TaskNotFoundError(StorageModuleException):
    def __init__(self, message: str, task_uuid: str):
        super().__init__(message, task_uuid)


class TaskInvalidUUID(StorageModuleException):
    def __init__(self, message: str, task_uuid: str):
        super().__init__(message, task_uuid)


class ArtifactExistsError(StorageModuleException):
    def __init__(self, message: str, artifact_info: dict):
        super().__init__(message, str(artifact_info))


class ArtifactNotFoundError(StorageModuleException):
    def __init__(self, message: str, artifact_info: dict):
        super().__init__(message, str(artifact_info))


class ArtifactInvalidName(StorageModuleException):
    def __init__(self, message: str, artifact_name: str):
        super().__init__(message, artifact_name)


class ArtifactInvalidType(StorageModuleException):
    def __init__(self, message: str, artifact_type: str):
        super().__init__(message, artifact_type)


class ArtifactInvalidSubType(StorageModuleException):
    def __init__(self, message: str, sub_type: str):
        super().__init__(message, sub_type)
