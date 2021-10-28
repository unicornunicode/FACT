"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Target(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UUID_FIELD_NUMBER: builtins.int
    SSH_FIELD_NUMBER: builtins.int
    uuid: builtins.bytes = ...
    @property
    def ssh(self) -> global___SSHAccess: ...
    def __init__(self,
        *,
        uuid : builtins.bytes = ...,
        ssh : typing.Optional[global___SSHAccess] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"access",b"access",u"ssh",b"ssh"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"access",b"access",u"ssh",b"ssh",u"uuid",b"uuid"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"access",b"access"]) -> typing.Optional[typing_extensions.Literal["ssh"]]: ...
global___Target = Target

class SSHAccess(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    HOST_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    PORT_FIELD_NUMBER: builtins.int
    PRIVATE_KEY_FIELD_NUMBER: builtins.int
    BECOME_FIELD_NUMBER: builtins.int
    BECOME_PASSWORD_FIELD_NUMBER: builtins.int
    host: typing.Text = ...
    user: typing.Text = ...
    port: builtins.int = ...
    private_key: typing.Text = ...
    become: builtins.bool = ...
    """sudo"""

    become_password: typing.Text = ...
    def __init__(self,
        *,
        host : typing.Text = ...,
        user : typing.Text = ...,
        port : builtins.int = ...,
        private_key : typing.Text = ...,
        become : builtins.bool = ...,
        become_password : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"become",b"become",u"become_password",b"become_password",u"host",b"host",u"port",b"port",u"private_key",b"private_key",u"user",b"user"]) -> None: ...
global___SSHAccess = SSHAccess

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
    SELECTOR_FIELD_NUMBER: builtins.int
    @property
    def selector(self) -> global___CollectDiskSelector: ...
    def __init__(self,
        *,
        selector : typing.Optional[global___CollectDiskSelector] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"selector",b"selector"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"selector",b"selector"]) -> None: ...
global___TaskCollectDisk = TaskCollectDisk

class TaskCollectDiskResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___TaskCollectDiskResult = TaskCollectDiskResult

class CollectDiskSelector(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PATH_FIELD_NUMBER: builtins.int
    path: typing.Text = ...
    def __init__(self,
        *,
        path : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"path",b"path"]) -> None: ...
global___CollectDiskSelector = CollectDiskSelector

class TaskCollectMemory(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___TaskCollectMemory = TaskCollectMemory

class TaskCollectMemoryResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___TaskCollectMemoryResult = TaskCollectMemoryResult

class TaskCollectLsblk(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___TaskCollectLsblk = TaskCollectLsblk

class LsblkResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEVICE_NAME_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    MOUNTPOINT_FIELD_NUMBER: builtins.int
    device_name: typing.Text = ...
    size: builtins.int = ...
    type: typing.Text = ...
    mountpoint: typing.Text = ...
    def __init__(self,
        *,
        device_name : typing.Text = ...,
        size : builtins.int = ...,
        type : typing.Text = ...,
        mountpoint : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"device_name",b"device_name",u"mountpoint",b"mountpoint",u"size",b"size",u"type",b"type"]) -> None: ...
global___LsblkResult = LsblkResult

class TaskCollectLsblkResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LSBLK_RESULTS_FIELD_NUMBER: builtins.int
    @property
    def lsblk_results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LsblkResult]: ...
    def __init__(self,
        *,
        lsblk_results : typing.Optional[typing.Iterable[global___LsblkResult]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"lsblk_results",b"lsblk_results"]) -> None: ...
global___TaskCollectLsblkResult = TaskCollectLsblkResult
