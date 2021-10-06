# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fact/controller.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fact/controller.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15\x66\x61\x63t/controller.proto\"\x7f\n\x0eSessionResults\x12\x32\n\x13worker_registration\x18\x01 \x01(\x0b\x32\x13.WorkerRegistrationH\x00\x12/\n\x12worker_task_result\x18\x02 \x01(\x0b\x32\x11.WorkerTaskResultH\x00\x42\x08\n\x06result\"l\n\rSessionEvents\x12.\n\x11worker_acceptance\x18\x01 \x01(\x0b\x32\x11.WorkerAcceptanceH\x00\x12\"\n\x0bworker_task\x18\x02 \x01(\x0b\x32\x0b.WorkerTaskH\x00\x42\x07\n\x05\x65vent\"=\n\x12WorkerRegistration\x12\x15\n\rprevious_uuid\x18\x01 \x01(\x0c\x12\x10\n\x08hostname\x18\x02 \x01(\t\" \n\x10WorkerAcceptance\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\"\x96\x01\n\nWorkerTask\x12\x1e\n\ttask_none\x18\x01 \x01(\x0b\x32\t.TaskNoneH\x00\x12-\n\x11task_collect_disk\x18\x02 \x01(\x0b\x32\x10.TaskCollectDiskH\x00\x12\x31\n\x13task_collect_memory\x18\x03 \x01(\x0b\x32\x12.TaskCollectMemoryH\x00\x42\x06\n\x04task\"\xae\x01\n\x10WorkerTaskResult\x12$\n\ttask_none\x18\x01 \x01(\x0b\x32\x0f.TaskNoneResultH\x00\x12\x33\n\x11task_collect_disk\x18\x02 \x01(\x0b\x32\x16.TaskCollectDiskResultH\x00\x12\x37\n\x13task_collect_memory\x18\x03 \x01(\x0b\x32\x18.TaskCollectMemoryResultH\x00\x42\x06\n\x04task\"\n\n\x08TaskNone\"\x10\n\x0eTaskNoneResult\"P\n\x0fTaskCollectDisk\x12\x17\n\x06target\x18\x01 \x01(\x0b\x32\x07.Target\x12$\n\rdisk_selector\x18\x02 \x01(\x0b\x32\r.DiskSelector\"\x17\n\x15TaskCollectDiskResult\"m\n\x0c\x44iskSelector\x12\"\n\x05group\x18\x01 \x01(\x0e\x32\x13.DiskSelector.Group\"9\n\x05Group\x12\r\n\tALL_DISKS\x10\x00\x12\r\n\tROOT_DISK\x10\x01\x12\x12\n\x0eROOT_PARTITION\x10\x02\",\n\x11TaskCollectMemory\x12\x17\n\x06target\x18\x01 \x01(\x0b\x32\x07.Target\"\x19\n\x17TaskCollectMemoryResult\";\n\x06Target\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x03ssh\x18\x02 \x01(\x0b\x32\n.SSHAccessH\x00\x42\x08\n\x06\x61\x63\x63\x65ss\"I\n\tSSHAccess\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\r\x12\x12\n\nprivateKey\x18\x04 \x01(\t2=\n\x0bWorkerTasks\x12.\n\x07Session\x12\x0f.SessionResults\x1a\x0e.SessionEvents(\x01\x30\x01\x62\x06proto3'
)



_DISKSELECTOR_GROUP = _descriptor.EnumDescriptor(
  name='Group',
  full_name='DiskSelector.Group',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALL_DISKS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROOT_DISK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROOT_PARTITION', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=880,
  serialized_end=937,
)
_sym_db.RegisterEnumDescriptor(_DISKSELECTOR_GROUP)


_SESSIONRESULTS = _descriptor.Descriptor(
  name='SessionResults',
  full_name='SessionResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='worker_registration', full_name='SessionResults.worker_registration', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='worker_task_result', full_name='SessionResults.worker_task_result', index=1,
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
      name='result', full_name='SessionResults.result',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=25,
  serialized_end=152,
)


_SESSIONEVENTS = _descriptor.Descriptor(
  name='SessionEvents',
  full_name='SessionEvents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='worker_acceptance', full_name='SessionEvents.worker_acceptance', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='worker_task', full_name='SessionEvents.worker_task', index=1,
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
      name='event', full_name='SessionEvents.event',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=154,
  serialized_end=262,
)


_WORKERREGISTRATION = _descriptor.Descriptor(
  name='WorkerRegistration',
  full_name='WorkerRegistration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='previous_uuid', full_name='WorkerRegistration.previous_uuid', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='WorkerRegistration.hostname', index=1,
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
  serialized_start=264,
  serialized_end=325,
)


_WORKERACCEPTANCE = _descriptor.Descriptor(
  name='WorkerAcceptance',
  full_name='WorkerAcceptance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='WorkerAcceptance.uuid', index=0,
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
  serialized_start=327,
  serialized_end=359,
)


_WORKERTASK = _descriptor.Descriptor(
  name='WorkerTask',
  full_name='WorkerTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_none', full_name='WorkerTask.task_none', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_collect_disk', full_name='WorkerTask.task_collect_disk', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_collect_memory', full_name='WorkerTask.task_collect_memory', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
      name='task', full_name='WorkerTask.task',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=362,
  serialized_end=512,
)


_WORKERTASKRESULT = _descriptor.Descriptor(
  name='WorkerTaskResult',
  full_name='WorkerTaskResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_none', full_name='WorkerTaskResult.task_none', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_collect_disk', full_name='WorkerTaskResult.task_collect_disk', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_collect_memory', full_name='WorkerTaskResult.task_collect_memory', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
      name='task', full_name='WorkerTaskResult.task',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=515,
  serialized_end=689,
)


_TASKNONE = _descriptor.Descriptor(
  name='TaskNone',
  full_name='TaskNone',
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
  serialized_start=691,
  serialized_end=701,
)


_TASKNONERESULT = _descriptor.Descriptor(
  name='TaskNoneResult',
  full_name='TaskNoneResult',
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
  serialized_start=703,
  serialized_end=719,
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
      name='target', full_name='TaskCollectDisk.target', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='disk_selector', full_name='TaskCollectDisk.disk_selector', index=1,
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
  ],
  serialized_start=721,
  serialized_end=801,
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
  serialized_start=803,
  serialized_end=826,
)


_DISKSELECTOR = _descriptor.Descriptor(
  name='DiskSelector',
  full_name='DiskSelector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='group', full_name='DiskSelector.group', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DISKSELECTOR_GROUP,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=828,
  serialized_end=937,
)


_TASKCOLLECTMEMORY = _descriptor.Descriptor(
  name='TaskCollectMemory',
  full_name='TaskCollectMemory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='TaskCollectMemory.target', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=939,
  serialized_end=983,
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
  serialized_start=985,
  serialized_end=1010,
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
      name='name', full_name='Target.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1012,
  serialized_end=1071,
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
      name='privateKey', full_name='SSHAccess.privateKey', index=3,
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
  serialized_start=1073,
  serialized_end=1146,
)

_SESSIONRESULTS.fields_by_name['worker_registration'].message_type = _WORKERREGISTRATION
_SESSIONRESULTS.fields_by_name['worker_task_result'].message_type = _WORKERTASKRESULT
_SESSIONRESULTS.oneofs_by_name['result'].fields.append(
  _SESSIONRESULTS.fields_by_name['worker_registration'])
_SESSIONRESULTS.fields_by_name['worker_registration'].containing_oneof = _SESSIONRESULTS.oneofs_by_name['result']
_SESSIONRESULTS.oneofs_by_name['result'].fields.append(
  _SESSIONRESULTS.fields_by_name['worker_task_result'])
_SESSIONRESULTS.fields_by_name['worker_task_result'].containing_oneof = _SESSIONRESULTS.oneofs_by_name['result']
_SESSIONEVENTS.fields_by_name['worker_acceptance'].message_type = _WORKERACCEPTANCE
_SESSIONEVENTS.fields_by_name['worker_task'].message_type = _WORKERTASK
_SESSIONEVENTS.oneofs_by_name['event'].fields.append(
  _SESSIONEVENTS.fields_by_name['worker_acceptance'])
_SESSIONEVENTS.fields_by_name['worker_acceptance'].containing_oneof = _SESSIONEVENTS.oneofs_by_name['event']
_SESSIONEVENTS.oneofs_by_name['event'].fields.append(
  _SESSIONEVENTS.fields_by_name['worker_task'])
_SESSIONEVENTS.fields_by_name['worker_task'].containing_oneof = _SESSIONEVENTS.oneofs_by_name['event']
_WORKERTASK.fields_by_name['task_none'].message_type = _TASKNONE
_WORKERTASK.fields_by_name['task_collect_disk'].message_type = _TASKCOLLECTDISK
_WORKERTASK.fields_by_name['task_collect_memory'].message_type = _TASKCOLLECTMEMORY
_WORKERTASK.oneofs_by_name['task'].fields.append(
  _WORKERTASK.fields_by_name['task_none'])
_WORKERTASK.fields_by_name['task_none'].containing_oneof = _WORKERTASK.oneofs_by_name['task']
_WORKERTASK.oneofs_by_name['task'].fields.append(
  _WORKERTASK.fields_by_name['task_collect_disk'])
_WORKERTASK.fields_by_name['task_collect_disk'].containing_oneof = _WORKERTASK.oneofs_by_name['task']
_WORKERTASK.oneofs_by_name['task'].fields.append(
  _WORKERTASK.fields_by_name['task_collect_memory'])
_WORKERTASK.fields_by_name['task_collect_memory'].containing_oneof = _WORKERTASK.oneofs_by_name['task']
_WORKERTASKRESULT.fields_by_name['task_none'].message_type = _TASKNONERESULT
_WORKERTASKRESULT.fields_by_name['task_collect_disk'].message_type = _TASKCOLLECTDISKRESULT
_WORKERTASKRESULT.fields_by_name['task_collect_memory'].message_type = _TASKCOLLECTMEMORYRESULT
_WORKERTASKRESULT.oneofs_by_name['task'].fields.append(
  _WORKERTASKRESULT.fields_by_name['task_none'])
_WORKERTASKRESULT.fields_by_name['task_none'].containing_oneof = _WORKERTASKRESULT.oneofs_by_name['task']
_WORKERTASKRESULT.oneofs_by_name['task'].fields.append(
  _WORKERTASKRESULT.fields_by_name['task_collect_disk'])
_WORKERTASKRESULT.fields_by_name['task_collect_disk'].containing_oneof = _WORKERTASKRESULT.oneofs_by_name['task']
_WORKERTASKRESULT.oneofs_by_name['task'].fields.append(
  _WORKERTASKRESULT.fields_by_name['task_collect_memory'])
_WORKERTASKRESULT.fields_by_name['task_collect_memory'].containing_oneof = _WORKERTASKRESULT.oneofs_by_name['task']
_TASKCOLLECTDISK.fields_by_name['target'].message_type = _TARGET
_TASKCOLLECTDISK.fields_by_name['disk_selector'].message_type = _DISKSELECTOR
_DISKSELECTOR.fields_by_name['group'].enum_type = _DISKSELECTOR_GROUP
_DISKSELECTOR_GROUP.containing_type = _DISKSELECTOR
_TASKCOLLECTMEMORY.fields_by_name['target'].message_type = _TARGET
_TARGET.fields_by_name['ssh'].message_type = _SSHACCESS
_TARGET.oneofs_by_name['access'].fields.append(
  _TARGET.fields_by_name['ssh'])
_TARGET.fields_by_name['ssh'].containing_oneof = _TARGET.oneofs_by_name['access']
DESCRIPTOR.message_types_by_name['SessionResults'] = _SESSIONRESULTS
DESCRIPTOR.message_types_by_name['SessionEvents'] = _SESSIONEVENTS
DESCRIPTOR.message_types_by_name['WorkerRegistration'] = _WORKERREGISTRATION
DESCRIPTOR.message_types_by_name['WorkerAcceptance'] = _WORKERACCEPTANCE
DESCRIPTOR.message_types_by_name['WorkerTask'] = _WORKERTASK
DESCRIPTOR.message_types_by_name['WorkerTaskResult'] = _WORKERTASKRESULT
DESCRIPTOR.message_types_by_name['TaskNone'] = _TASKNONE
DESCRIPTOR.message_types_by_name['TaskNoneResult'] = _TASKNONERESULT
DESCRIPTOR.message_types_by_name['TaskCollectDisk'] = _TASKCOLLECTDISK
DESCRIPTOR.message_types_by_name['TaskCollectDiskResult'] = _TASKCOLLECTDISKRESULT
DESCRIPTOR.message_types_by_name['DiskSelector'] = _DISKSELECTOR
DESCRIPTOR.message_types_by_name['TaskCollectMemory'] = _TASKCOLLECTMEMORY
DESCRIPTOR.message_types_by_name['TaskCollectMemoryResult'] = _TASKCOLLECTMEMORYRESULT
DESCRIPTOR.message_types_by_name['Target'] = _TARGET
DESCRIPTOR.message_types_by_name['SSHAccess'] = _SSHACCESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SessionResults = _reflection.GeneratedProtocolMessageType('SessionResults', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONRESULTS,
  '__module__' : 'fact.controller_pb2'
  # @@protoc_insertion_point(class_scope:SessionResults)
  })
_sym_db.RegisterMessage(SessionResults)

SessionEvents = _reflection.GeneratedProtocolMessageType('SessionEvents', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONEVENTS,
  '__module__' : 'fact.controller_pb2'
  # @@protoc_insertion_point(class_scope:SessionEvents)
  })
_sym_db.RegisterMessage(SessionEvents)

WorkerRegistration = _reflection.GeneratedProtocolMessageType('WorkerRegistration', (_message.Message,), {
  'DESCRIPTOR' : _WORKERREGISTRATION,
  '__module__' : 'fact.controller_pb2'
  # @@protoc_insertion_point(class_scope:WorkerRegistration)
  })
_sym_db.RegisterMessage(WorkerRegistration)

WorkerAcceptance = _reflection.GeneratedProtocolMessageType('WorkerAcceptance', (_message.Message,), {
  'DESCRIPTOR' : _WORKERACCEPTANCE,
  '__module__' : 'fact.controller_pb2'
  # @@protoc_insertion_point(class_scope:WorkerAcceptance)
  })
_sym_db.RegisterMessage(WorkerAcceptance)

WorkerTask = _reflection.GeneratedProtocolMessageType('WorkerTask', (_message.Message,), {
  'DESCRIPTOR' : _WORKERTASK,
  '__module__' : 'fact.controller_pb2'
  # @@protoc_insertion_point(class_scope:WorkerTask)
  })
_sym_db.RegisterMessage(WorkerTask)

WorkerTaskResult = _reflection.GeneratedProtocolMessageType('WorkerTaskResult', (_message.Message,), {
  'DESCRIPTOR' : _WORKERTASKRESULT,
  '__module__' : 'fact.controller_pb2'
  # @@protoc_insertion_point(class_scope:WorkerTaskResult)
  })
_sym_db.RegisterMessage(WorkerTaskResult)

TaskNone = _reflection.GeneratedProtocolMessageType('TaskNone', (_message.Message,), {
  'DESCRIPTOR' : _TASKNONE,
  '__module__' : 'fact.controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskNone)
  })
_sym_db.RegisterMessage(TaskNone)

TaskNoneResult = _reflection.GeneratedProtocolMessageType('TaskNoneResult', (_message.Message,), {
  'DESCRIPTOR' : _TASKNONERESULT,
  '__module__' : 'fact.controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskNoneResult)
  })
_sym_db.RegisterMessage(TaskNoneResult)

TaskCollectDisk = _reflection.GeneratedProtocolMessageType('TaskCollectDisk', (_message.Message,), {
  'DESCRIPTOR' : _TASKCOLLECTDISK,
  '__module__' : 'fact.controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskCollectDisk)
  })
_sym_db.RegisterMessage(TaskCollectDisk)

TaskCollectDiskResult = _reflection.GeneratedProtocolMessageType('TaskCollectDiskResult', (_message.Message,), {
  'DESCRIPTOR' : _TASKCOLLECTDISKRESULT,
  '__module__' : 'fact.controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskCollectDiskResult)
  })
_sym_db.RegisterMessage(TaskCollectDiskResult)

DiskSelector = _reflection.GeneratedProtocolMessageType('DiskSelector', (_message.Message,), {
  'DESCRIPTOR' : _DISKSELECTOR,
  '__module__' : 'fact.controller_pb2'
  # @@protoc_insertion_point(class_scope:DiskSelector)
  })
_sym_db.RegisterMessage(DiskSelector)

TaskCollectMemory = _reflection.GeneratedProtocolMessageType('TaskCollectMemory', (_message.Message,), {
  'DESCRIPTOR' : _TASKCOLLECTMEMORY,
  '__module__' : 'fact.controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskCollectMemory)
  })
_sym_db.RegisterMessage(TaskCollectMemory)

TaskCollectMemoryResult = _reflection.GeneratedProtocolMessageType('TaskCollectMemoryResult', (_message.Message,), {
  'DESCRIPTOR' : _TASKCOLLECTMEMORYRESULT,
  '__module__' : 'fact.controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskCollectMemoryResult)
  })
_sym_db.RegisterMessage(TaskCollectMemoryResult)

Target = _reflection.GeneratedProtocolMessageType('Target', (_message.Message,), {
  'DESCRIPTOR' : _TARGET,
  '__module__' : 'fact.controller_pb2'
  # @@protoc_insertion_point(class_scope:Target)
  })
_sym_db.RegisterMessage(Target)

SSHAccess = _reflection.GeneratedProtocolMessageType('SSHAccess', (_message.Message,), {
  'DESCRIPTOR' : _SSHACCESS,
  '__module__' : 'fact.controller_pb2'
  # @@protoc_insertion_point(class_scope:SSHAccess)
  })
_sym_db.RegisterMessage(SSHAccess)



_WORKERTASKS = _descriptor.ServiceDescriptor(
  name='WorkerTasks',
  full_name='WorkerTasks',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1148,
  serialized_end=1209,
  methods=[
  _descriptor.MethodDescriptor(
    name='Session',
    full_name='WorkerTasks.Session',
    index=0,
    containing_service=None,
    input_type=_SESSIONRESULTS,
    output_type=_SESSIONEVENTS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WORKERTASKS)

DESCRIPTOR.services_by_name['WorkerTasks'] = _WORKERTASKS

# @@protoc_insertion_point(module_scope)
