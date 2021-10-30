from uuid import UUID


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


class ArtifactExistsError(FACTError, Exception):
    def __init__(self, task_uuid: UUID, artifact_name: str, artifact_type: str):
        super().__init__(f"{task_uuid}: {artifact_type} {artifact_name}")


class ArtifactNotFoundError(FACTError, Exception):
    def __init__(self, task_uuid: UUID, artifact_name: str, artifact_type: str):
        super().__init__(f"{task_uuid}: {artifact_type} {artifact_name}")


class LoopDeviceSetupError(FACTError, Exception):
    """Exception if loop device fails to setup"""

    pass


class LoopDeviceDetachError(FACTError, Exception):
    """Exception if loop device fails to detach"""

    pass


class UnmountPartitionError(FACTError, Exception):
    """Exception if partition fails to unmount"""

    pass
