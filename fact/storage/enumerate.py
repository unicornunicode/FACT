from enum import Enum


class ArtifactType(Enum):
    unknown = 0
    disk = 1
    memory = 2


class DataType(Enum):
    unknown = 0
    full = 1
    partition = 2
    process = 3
