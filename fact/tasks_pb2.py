# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fact/tasks.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fact/tasks.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x66\x61\x63t/tasks.proto\";\n\x06Target\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\x12\x19\n\x03ssh\x18\x02 \x01(\x0b\x32\n.SSHAccessH\x00\x42\x08\n\x06\x61\x63\x63\x65ss\"s\n\tSSHAccess\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\r\x12\x13\n\x0bprivate_key\x18\x04 \x01(\t\x12\x0e\n\x06\x62\x65\x63ome\x18\x05 \x01(\x08\x12\x17\n\x0f\x62\x65\x63ome_password\x18\x06 \x01(\t\"&\n\x0fTaskCollectDisk\x12\x13\n\x0b\x64\x65vice_name\x18\x02 \x01(\t\"\x17\n\x15TaskCollectDiskResult\"\x13\n\x11TaskCollectMemory\"\x19\n\x17TaskCollectMemoryResult\"\x15\n\x13TaskCollectDiskinfo\"U\n\x0eTargetDiskinfo\x12\x13\n\x0b\x64\x65vice_name\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\x04\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x12\n\nmountpoint\x18\x04 \x01(\t\"?\n\x19TaskCollectDiskinfoResult\x12\"\n\tdiskinfos\x18\x01 \x03(\x0b\x32\x0f.TargetDiskinfo\"\'\n\rTaskIngestion\x12\x16\n\x0e\x63ollected_uuid\x18\x01 \x01(\x0c\"\x15\n\x13TaskIngestionResultb\x06proto3'
)




_TARGET = _descriptor.Descriptor(
  name='Target',
  full_name='Target',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='Target.uuid', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ssh', full_name='Target.ssh', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='access', full_name='Target.access',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=20,
  serialized_end=79,
)


_SSHACCESS = _descriptor.Descriptor(
  name='SSHAccess',
  full_name='SSHAccess',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='SSHAccess.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='SSHAccess.user', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='SSHAccess.port', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='private_key', full_name='SSHAccess.private_key', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='become', full_name='SSHAccess.become', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='become_password', full_name='SSHAccess.become_password', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=196,
)


_TASKCOLLECTDISK = _descriptor.Descriptor(
  name='TaskCollectDisk',
  full_name='TaskCollectDisk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_name', full_name='TaskCollectDisk.device_name', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=236,
)


_TASKCOLLECTDISKRESULT = _descriptor.Descriptor(
  name='TaskCollectDiskResult',
  full_name='TaskCollectDiskResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=238,
  serialized_end=261,
)


_TASKCOLLECTMEMORY = _descriptor.Descriptor(
  name='TaskCollectMemory',
  full_name='TaskCollectMemory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=263,
  serialized_end=282,
)


_TASKCOLLECTMEMORYRESULT = _descriptor.Descriptor(
  name='TaskCollectMemoryResult',
  full_name='TaskCollectMemoryResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=284,
  serialized_end=309,
)


_TASKCOLLECTDISKINFO = _descriptor.Descriptor(
  name='TaskCollectDiskinfo',
  full_name='TaskCollectDiskinfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=311,
  serialized_end=332,
)


_TARGETDISKINFO = _descriptor.Descriptor(
  name='TargetDiskinfo',
  full_name='TargetDiskinfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_name', full_name='TargetDiskinfo.device_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size', full_name='TargetDiskinfo.size', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='TargetDiskinfo.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mountpoint', full_name='TargetDiskinfo.mountpoint', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=334,
  serialized_end=419,
)


_TASKCOLLECTDISKINFORESULT = _descriptor.Descriptor(
  name='TaskCollectDiskinfoResult',
  full_name='TaskCollectDiskinfoResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='diskinfos', full_name='TaskCollectDiskinfoResult.diskinfos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=421,
  serialized_end=484,
)


_TASKINGESTION = _descriptor.Descriptor(
  name='TaskIngestion',
  full_name='TaskIngestion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='collected_uuid', full_name='TaskIngestion.collected_uuid', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=486,
  serialized_end=525,
)


_TASKINGESTIONRESULT = _descriptor.Descriptor(
  name='TaskIngestionResult',
  full_name='TaskIngestionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=527,
  serialized_end=548,
)

_TARGET.fields_by_name['ssh'].message_type = _SSHACCESS
_TARGET.oneofs_by_name['access'].fields.append(
  _TARGET.fields_by_name['ssh'])
_TARGET.fields_by_name['ssh'].containing_oneof = _TARGET.oneofs_by_name['access']
_TASKCOLLECTDISKINFORESULT.fields_by_name['diskinfos'].message_type = _TARGETDISKINFO
DESCRIPTOR.message_types_by_name['Target'] = _TARGET
DESCRIPTOR.message_types_by_name['SSHAccess'] = _SSHACCESS
DESCRIPTOR.message_types_by_name['TaskCollectDisk'] = _TASKCOLLECTDISK
DESCRIPTOR.message_types_by_name['TaskCollectDiskResult'] = _TASKCOLLECTDISKRESULT
DESCRIPTOR.message_types_by_name['TaskCollectMemory'] = _TASKCOLLECTMEMORY
DESCRIPTOR.message_types_by_name['TaskCollectMemoryResult'] = _TASKCOLLECTMEMORYRESULT
DESCRIPTOR.message_types_by_name['TaskCollectDiskinfo'] = _TASKCOLLECTDISKINFO
DESCRIPTOR.message_types_by_name['TargetDiskinfo'] = _TARGETDISKINFO
DESCRIPTOR.message_types_by_name['TaskCollectDiskinfoResult'] = _TASKCOLLECTDISKINFORESULT
DESCRIPTOR.message_types_by_name['TaskIngestion'] = _TASKINGESTION
DESCRIPTOR.message_types_by_name['TaskIngestionResult'] = _TASKINGESTIONRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Target = _reflection.GeneratedProtocolMessageType('Target', (_message.Message,), {
  'DESCRIPTOR' : _TARGET,
  '__module__' : 'fact.tasks_pb2'
  # @@protoc_insertion_point(class_scope:Target)
  })
_sym_db.RegisterMessage(Target)

SSHAccess = _reflection.GeneratedProtocolMessageType('SSHAccess', (_message.Message,), {
  'DESCRIPTOR' : _SSHACCESS,
  '__module__' : 'fact.tasks_pb2'
  # @@protoc_insertion_point(class_scope:SSHAccess)
  })
_sym_db.RegisterMessage(SSHAccess)

TaskCollectDisk = _reflection.GeneratedProtocolMessageType('TaskCollectDisk', (_message.Message,), {
  'DESCRIPTOR' : _TASKCOLLECTDISK,
  '__module__' : 'fact.tasks_pb2'
  # @@protoc_insertion_point(class_scope:TaskCollectDisk)
  })
_sym_db.RegisterMessage(TaskCollectDisk)

TaskCollectDiskResult = _reflection.GeneratedProtocolMessageType('TaskCollectDiskResult', (_message.Message,), {
  'DESCRIPTOR' : _TASKCOLLECTDISKRESULT,
  '__module__' : 'fact.tasks_pb2'
  # @@protoc_insertion_point(class_scope:TaskCollectDiskResult)
  })
_sym_db.RegisterMessage(TaskCollectDiskResult)

TaskCollectMemory = _reflection.GeneratedProtocolMessageType('TaskCollectMemory', (_message.Message,), {
  'DESCRIPTOR' : _TASKCOLLECTMEMORY,
  '__module__' : 'fact.tasks_pb2'
  # @@protoc_insertion_point(class_scope:TaskCollectMemory)
  })
_sym_db.RegisterMessage(TaskCollectMemory)

TaskCollectMemoryResult = _reflection.GeneratedProtocolMessageType('TaskCollectMemoryResult', (_message.Message,), {
  'DESCRIPTOR' : _TASKCOLLECTMEMORYRESULT,
  '__module__' : 'fact.tasks_pb2'
  # @@protoc_insertion_point(class_scope:TaskCollectMemoryResult)
  })
_sym_db.RegisterMessage(TaskCollectMemoryResult)

TaskCollectDiskinfo = _reflection.GeneratedProtocolMessageType('TaskCollectDiskinfo', (_message.Message,), {
  'DESCRIPTOR' : _TASKCOLLECTDISKINFO,
  '__module__' : 'fact.tasks_pb2'
  # @@protoc_insertion_point(class_scope:TaskCollectDiskinfo)
  })
_sym_db.RegisterMessage(TaskCollectDiskinfo)

TargetDiskinfo = _reflection.GeneratedProtocolMessageType('TargetDiskinfo', (_message.Message,), {
  'DESCRIPTOR' : _TARGETDISKINFO,
  '__module__' : 'fact.tasks_pb2'
  # @@protoc_insertion_point(class_scope:TargetDiskinfo)
  })
_sym_db.RegisterMessage(TargetDiskinfo)

TaskCollectDiskinfoResult = _reflection.GeneratedProtocolMessageType('TaskCollectDiskinfoResult', (_message.Message,), {
  'DESCRIPTOR' : _TASKCOLLECTDISKINFORESULT,
  '__module__' : 'fact.tasks_pb2'
  # @@protoc_insertion_point(class_scope:TaskCollectDiskinfoResult)
  })
_sym_db.RegisterMessage(TaskCollectDiskinfoResult)

TaskIngestion = _reflection.GeneratedProtocolMessageType('TaskIngestion', (_message.Message,), {
  'DESCRIPTOR' : _TASKINGESTION,
  '__module__' : 'fact.tasks_pb2'
  # @@protoc_insertion_point(class_scope:TaskIngestion)
  })
_sym_db.RegisterMessage(TaskIngestion)

TaskIngestionResult = _reflection.GeneratedProtocolMessageType('TaskIngestionResult', (_message.Message,), {
  'DESCRIPTOR' : _TASKINGESTIONRESULT,
  '__module__' : 'fact.tasks_pb2'
  # @@protoc_insertion_point(class_scope:TaskIngestionResult)
  })
_sym_db.RegisterMessage(TaskIngestionResult)


# @@protoc_insertion_point(module_scope)
