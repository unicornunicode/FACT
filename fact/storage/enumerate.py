from enum import Enum


class ArtifactType(Enum):
    """Types of Artifact"""

    unknown = 0
    disk = 1
    memory = 2


class DataType(Enum):
    """Sub type of Artifact"""

    unknown = 0
    full = 1
    partition = 2
    process = 3
