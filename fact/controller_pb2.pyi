"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class SessionResults(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WORKER_REGISTRATION_FIELD_NUMBER: builtins.int
    WORKER_TASK_RESULT_FIELD_NUMBER: builtins.int
    @property
    def worker_registration(self) -> global___WorkerRegistration: ...
    @property
    def worker_task_result(self) -> global___WorkerTaskResult: ...
    def __init__(self,
        *,
        worker_registration : typing.Optional[global___WorkerRegistration] = ...,
        worker_task_result : typing.Optional[global___WorkerTaskResult] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"result",b"result",u"worker_registration",b"worker_registration",u"worker_task_result",b"worker_task_result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"result",b"result",u"worker_registration",b"worker_registration",u"worker_task_result",b"worker_task_result"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"result",b"result"]) -> typing.Optional[typing_extensions.Literal["worker_registration","worker_task_result"]]: ...
global___SessionResults = SessionResults

class SessionEvents(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WORKER_ACCEPTANCE_FIELD_NUMBER: builtins.int
    WORKER_TASK_FIELD_NUMBER: builtins.int
    @property
    def worker_acceptance(self) -> global___WorkerAcceptance: ...
    @property
    def worker_task(self) -> global___WorkerTask: ...
    def __init__(self,
        *,
        worker_acceptance : typing.Optional[global___WorkerAcceptance] = ...,
        worker_task : typing.Optional[global___WorkerTask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"event",b"event",u"worker_acceptance",b"worker_acceptance",u"worker_task",b"worker_task"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"event",b"event",u"worker_acceptance",b"worker_acceptance",u"worker_task",b"worker_task"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"event",b"event"]) -> typing.Optional[typing_extensions.Literal["worker_acceptance","worker_task"]]: ...
global___SessionEvents = SessionEvents

class WorkerRegistration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PREVIOUS_UUID_FIELD_NUMBER: builtins.int
    HOSTNAME_FIELD_NUMBER: builtins.int
    previous_uuid: builtins.bytes = ...
    hostname: typing.Text = ...
    def __init__(self,
        *,
        previous_uuid : builtins.bytes = ...,
        hostname : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"hostname",b"hostname",u"previous_uuid",b"previous_uuid"]) -> None: ...
global___WorkerRegistration = WorkerRegistration

class WorkerAcceptance(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UUID_FIELD_NUMBER: builtins.int
    uuid: builtins.bytes = ...
    def __init__(self,
        *,
        uuid : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"uuid",b"uuid"]) -> None: ...
global___WorkerAcceptance = WorkerAcceptance

class WorkerTask(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TASK_NONE_FIELD_NUMBER: builtins.int
    TASK_COLLECT_DISK_FIELD_NUMBER: builtins.int
    TASK_COLLECT_MEMORY_FIELD_NUMBER: builtins.int
    @property
    def task_none(self) -> global___TaskNone: ...
    @property
    def task_collect_disk(self) -> global___TaskCollectDisk: ...
    @property
    def task_collect_memory(self) -> global___TaskCollectMemory: ...
    def __init__(self,
        *,
        task_none : typing.Optional[global___TaskNone] = ...,
        task_collect_disk : typing.Optional[global___TaskCollectDisk] = ...,
        task_collect_memory : typing.Optional[global___TaskCollectMemory] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"task",b"task",u"task_collect_disk",b"task_collect_disk",u"task_collect_memory",b"task_collect_memory",u"task_none",b"task_none"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"task",b"task",u"task_collect_disk",b"task_collect_disk",u"task_collect_memory",b"task_collect_memory",u"task_none",b"task_none"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"task",b"task"]) -> typing.Optional[typing_extensions.Literal["task_none","task_collect_disk","task_collect_memory"]]: ...
global___WorkerTask = WorkerTask

class WorkerTaskResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TASK_NONE_FIELD_NUMBER: builtins.int
    TASK_COLLECT_DISK_FIELD_NUMBER: builtins.int
    TASK_COLLECT_MEMORY_FIELD_NUMBER: builtins.int
    @property
    def task_none(self) -> global___TaskNoneResult: ...
    @property
    def task_collect_disk(self) -> global___TaskCollectDiskResult: ...
    @property
    def task_collect_memory(self) -> global___TaskCollectMemoryResult: ...
    def __init__(self,
        *,
        task_none : typing.Optional[global___TaskNoneResult] = ...,
        task_collect_disk : typing.Optional[global___TaskCollectDiskResult] = ...,
        task_collect_memory : typing.Optional[global___TaskCollectMemoryResult] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"task",b"task",u"task_collect_disk",b"task_collect_disk",u"task_collect_memory",b"task_collect_memory",u"task_none",b"task_none"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"task",b"task",u"task_collect_disk",b"task_collect_disk",u"task_collect_memory",b"task_collect_memory",u"task_none",b"task_none"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"task",b"task"]) -> typing.Optional[typing_extensions.Literal["task_none","task_collect_disk","task_collect_memory"]]: ...
global___WorkerTaskResult = WorkerTaskResult

class TaskNone(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___TaskNone = TaskNone

class TaskNoneResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___TaskNoneResult = TaskNoneResult

class TaskCollectDisk(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TARGET_FIELD_NUMBER: builtins.int
    DISK_SELECTOR_FIELD_NUMBER: builtins.int
    @property
    def target(self) -> global___Target: ...
    @property
    def disk_selector(self) -> global___DiskSelector: ...
    def __init__(self,
        *,
        target : typing.Optional[global___Target] = ...,
        disk_selector : typing.Optional[global___DiskSelector] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"disk_selector",b"disk_selector",u"target",b"target"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"disk_selector",b"disk_selector",u"target",b"target"]) -> None: ...
global___TaskCollectDisk = TaskCollectDisk

class TaskCollectDiskResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___TaskCollectDiskResult = TaskCollectDiskResult

class DiskSelector(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Group(_Group, metaclass=_GroupEnumTypeWrapper):
        pass
    class _Group:
        V = typing.NewType('V', builtins.int)
    class _GroupEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Group.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        ALL_DISKS = DiskSelector.Group.V(0)
        ROOT_DISK = DiskSelector.Group.V(1)
        ROOT_PARTITION = DiskSelector.Group.V(2)

    ALL_DISKS = DiskSelector.Group.V(0)
    ROOT_DISK = DiskSelector.Group.V(1)
    ROOT_PARTITION = DiskSelector.Group.V(2)

    GROUP_FIELD_NUMBER: builtins.int
    group: global___DiskSelector.Group.V = ...
    def __init__(self,
        *,
        group : global___DiskSelector.Group.V = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"group",b"group"]) -> None: ...
global___DiskSelector = DiskSelector

class TaskCollectMemory(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TARGET_FIELD_NUMBER: builtins.int
    @property
    def target(self) -> global___Target: ...
    def __init__(self,
        *,
        target : typing.Optional[global___Target] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"target",b"target"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"target",b"target"]) -> None: ...
global___TaskCollectMemory = TaskCollectMemory

class TaskCollectMemoryResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___TaskCollectMemoryResult = TaskCollectMemoryResult

class Target(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    SSH_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    @property
    def ssh(self) -> global___SSHAccess: ...
    def __init__(self,
        *,
        name : typing.Text = ...,
        ssh : typing.Optional[global___SSHAccess] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"access",b"access",u"ssh",b"ssh"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"access",b"access",u"name",b"name",u"ssh",b"ssh"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"access",b"access"]) -> typing.Optional[typing_extensions.Literal["ssh"]]: ...
global___Target = Target

class SSHAccess(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    HOST_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    PORT_FIELD_NUMBER: builtins.int
    PRIVATEKEY_FIELD_NUMBER: builtins.int
    BECOME_FIELD_NUMBER: builtins.int
    BECOMEPASSWORD_FIELD_NUMBER: builtins.int
    host: typing.Text = ...
    user: typing.Text = ...
    port: builtins.int = ...
    privateKey: typing.Text = ...
    become: builtins.bool = ...
    """sudo"""

    becomePassword: typing.Text = ...
    def __init__(self,
        *,
        host : typing.Text = ...,
        user : typing.Text = ...,
        port : builtins.int = ...,
        privateKey : typing.Text = ...,
        become : builtins.bool = ...,
        becomePassword : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"become",b"become",u"becomePassword",b"becomePassword",u"host",b"host",u"port",b"port",u"privateKey",b"privateKey",u"user",b"user"]) -> None: ...
global___SSHAccess = SSHAccess
