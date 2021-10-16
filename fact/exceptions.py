class StorageExistsError(Exception):
    def __init__(self, message: str, storage_path: str):
        self.message = message
        self.storage_path = storage_path

    def __str__(self):
        return f"{self.storage_path} -> {self.message}"


class TaskExistsError(Exception):
    def __init__(self, message: str, task_id: str):
        self.message = message
        self.task_id = task_id

    def __str__(self):
        return f"{self.task_id} -> {self.message}"


class TaskInvalidUUID(Exception):
    def __init__(self, message: str, task_uuid: str):
        self.message = message
        self.task_uuid = task_uuid

    def __str__(self):
        return f"{self.task_uuid} -> {self.message}"
