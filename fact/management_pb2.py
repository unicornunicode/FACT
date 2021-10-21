# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fact/management.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from fact import tasks_pb2 as fact_dot_tasks__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fact/management.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15\x66\x61\x63t/management.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x10\x66\x61\x63t/tasks.proto\"\xad\x01\n\x11\x43reateTaskRequest\x12\x1e\n\ttask_none\x18\x01 \x01(\x0b\x32\t.TaskNoneH\x00\x12-\n\x11task_collect_disk\x18\x02 \x01(\x0b\x32\x10.TaskCollectDiskH\x00\x12\x31\n\x13task_collect_memory\x18\x03 \x01(\x0b\x32\x12.TaskCollectMemoryH\x00\x12\x0e\n\x06target\x18\x04 \x01(\x0c\x42\x06\n\x04task\" \n\x10\x43reateTaskResult\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\"\x11\n\x0fListTaskRequest\"*\n\x0eListTaskResult\x12\x18\n\x05tasks\x18\x01 \x03(\x0b\x32\t.ListTask\"\xa9\x03\n\x08ListTask\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\x12 \n\x06status\x18\x02 \x01(\x0e\x32\x10.ListTask.Status\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x61ssigned_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0c\x63ompleted_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06target\x18\x06 \x01(\x0c\x12\x1e\n\ttask_none\x18\x07 \x01(\x0b\x32\t.TaskNoneH\x00\x12-\n\x11task_collect_disk\x18\x08 \x01(\x0b\x32\x10.TaskCollectDiskH\x00\x12\x31\n\x13task_collect_memory\x18\t \x01(\x0b\x32\x12.TaskCollectMemoryH\x00\x12\x0e\n\x06worker\x18\n \x01(\x0c\"0\n\x06Status\x12\x0b\n\x07WAITING\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\x0c\n\x08\x43OMPLETE\x10\x02\x42\x06\n\x04task\"H\n\x13\x43reateTargetRequest\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x19\n\x03ssh\x18\x02 \x01(\x0b\x32\n.SSHAccessH\x00\x42\x08\n\x06\x61\x63\x63\x65ss\"\"\n\x12\x43reateTargetResult\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\"\x13\n\x11ListTargetRequest\"0\n\x10ListTargetResult\x12\x1c\n\x07targets\x18\x01 \x03(\x0b\x32\x0b.ListTarget\"M\n\nListTarget\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x19\n\x03ssh\x18\x02 \x01(\x0b\x32\n.SSHAccessH\x00\x42\x08\n\x06\x61\x63\x63\x65ss\"\x13\n\x11ListWorkerRequest\"2\n\x10ListWorkerResult\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\x12\x10\n\x08hostname\x18\x02 \x01(\t2\x95\x02\n\nManagement\x12\x33\n\nCreateTask\x12\x12.CreateTaskRequest\x1a\x11.CreateTaskResult\x12-\n\x08ListTask\x12\x10.ListTaskRequest\x1a\x0f.ListTaskResult\x12\x39\n\x0c\x43reateTarget\x12\x14.CreateTargetRequest\x1a\x13.CreateTargetResult\x12\x33\n\nListTarget\x12\x12.ListTargetRequest\x1a\x11.ListTargetResult\x12\x33\n\nListWorker\x12\x12.ListWorkerRequest\x1a\x11.ListWorkerResultb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,fact_dot_tasks__pb2.DESCRIPTOR,])



_LISTTASK_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='ListTask.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WAITING', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPLETE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=719,
  serialized_end=767,
)
_sym_db.RegisterEnumDescriptor(_LISTTASK_STATUS)


_CREATETASKREQUEST = _descriptor.Descriptor(
  name='CreateTaskRequest',
  full_name='CreateTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_none', full_name='CreateTaskRequest.task_none', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_collect_disk', full_name='CreateTaskRequest.task_collect_disk', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_collect_memory', full_name='CreateTaskRequest.task_collect_memory', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='CreateTaskRequest.target', index=3,
      number=4, type=12, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='task', full_name='CreateTaskRequest.task',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=77,
  serialized_end=250,
)


_CREATETASKRESULT = _descriptor.Descriptor(
  name='CreateTaskResult',
  full_name='CreateTaskResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='CreateTaskResult.uuid', index=0,
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
  serialized_start=252,
  serialized_end=284,
)


_LISTTASKREQUEST = _descriptor.Descriptor(
  name='ListTaskRequest',
  full_name='ListTaskRequest',
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
  serialized_start=286,
  serialized_end=303,
)


_LISTTASKRESULT = _descriptor.Descriptor(
  name='ListTaskResult',
  full_name='ListTaskResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tasks', full_name='ListTaskResult.tasks', index=0,
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
  serialized_start=305,
  serialized_end=347,
)


_LISTTASK = _descriptor.Descriptor(
  name='ListTask',
  full_name='ListTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='ListTask.uuid', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='ListTask.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='ListTask.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='assigned_at', full_name='ListTask.assigned_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='completed_at', full_name='ListTask.completed_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='ListTask.target', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_none', full_name='ListTask.task_none', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_collect_disk', full_name='ListTask.task_collect_disk', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_collect_memory', full_name='ListTask.task_collect_memory', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='worker', full_name='ListTask.worker', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LISTTASK_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='task', full_name='ListTask.task',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=350,
  serialized_end=775,
)


_CREATETARGETREQUEST = _descriptor.Descriptor(
  name='CreateTargetRequest',
  full_name='CreateTargetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='CreateTargetRequest.name', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ssh', full_name='CreateTargetRequest.ssh', index=1,
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
      name='access', full_name='CreateTargetRequest.access',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=777,
  serialized_end=849,
)


_CREATETARGETRESULT = _descriptor.Descriptor(
  name='CreateTargetResult',
  full_name='CreateTargetResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='CreateTargetResult.uuid', index=0,
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
  serialized_start=851,
  serialized_end=885,
)


_LISTTARGETREQUEST = _descriptor.Descriptor(
  name='ListTargetRequest',
  full_name='ListTargetRequest',
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
  serialized_start=887,
  serialized_end=906,
)


_LISTTARGETRESULT = _descriptor.Descriptor(
  name='ListTargetResult',
  full_name='ListTargetResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='targets', full_name='ListTargetResult.targets', index=0,
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
  serialized_start=908,
  serialized_end=956,
)


_LISTTARGET = _descriptor.Descriptor(
  name='ListTarget',
  full_name='ListTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='ListTarget.uuid', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='ListTarget.name', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ssh', full_name='ListTarget.ssh', index=2,
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
      name='access', full_name='ListTarget.access',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=958,
  serialized_end=1035,
)


_LISTWORKERREQUEST = _descriptor.Descriptor(
  name='ListWorkerRequest',
  full_name='ListWorkerRequest',
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
  serialized_start=1037,
  serialized_end=1056,
)


_LISTWORKERRESULT = _descriptor.Descriptor(
  name='ListWorkerResult',
  full_name='ListWorkerResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='ListWorkerResult.uuid', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='ListWorkerResult.hostname', index=1,
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
  serialized_start=1058,
  serialized_end=1108,
)

_CREATETASKREQUEST.fields_by_name['task_none'].message_type = fact_dot_tasks__pb2._TASKNONE
_CREATETASKREQUEST.fields_by_name['task_collect_disk'].message_type = fact_dot_tasks__pb2._TASKCOLLECTDISK
_CREATETASKREQUEST.fields_by_name['task_collect_memory'].message_type = fact_dot_tasks__pb2._TASKCOLLECTMEMORY
_CREATETASKREQUEST.oneofs_by_name['task'].fields.append(
  _CREATETASKREQUEST.fields_by_name['task_none'])
_CREATETASKREQUEST.fields_by_name['task_none'].containing_oneof = _CREATETASKREQUEST.oneofs_by_name['task']
_CREATETASKREQUEST.oneofs_by_name['task'].fields.append(
  _CREATETASKREQUEST.fields_by_name['task_collect_disk'])
_CREATETASKREQUEST.fields_by_name['task_collect_disk'].containing_oneof = _CREATETASKREQUEST.oneofs_by_name['task']
_CREATETASKREQUEST.oneofs_by_name['task'].fields.append(
  _CREATETASKREQUEST.fields_by_name['task_collect_memory'])
_CREATETASKREQUEST.fields_by_name['task_collect_memory'].containing_oneof = _CREATETASKREQUEST.oneofs_by_name['task']
_LISTTASKRESULT.fields_by_name['tasks'].message_type = _LISTTASK
_LISTTASK.fields_by_name['status'].enum_type = _LISTTASK_STATUS
_LISTTASK.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTTASK.fields_by_name['assigned_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTTASK.fields_by_name['completed_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTTASK.fields_by_name['task_none'].message_type = fact_dot_tasks__pb2._TASKNONE
_LISTTASK.fields_by_name['task_collect_disk'].message_type = fact_dot_tasks__pb2._TASKCOLLECTDISK
_LISTTASK.fields_by_name['task_collect_memory'].message_type = fact_dot_tasks__pb2._TASKCOLLECTMEMORY
_LISTTASK_STATUS.containing_type = _LISTTASK
_LISTTASK.oneofs_by_name['task'].fields.append(
  _LISTTASK.fields_by_name['task_none'])
_LISTTASK.fields_by_name['task_none'].containing_oneof = _LISTTASK.oneofs_by_name['task']
_LISTTASK.oneofs_by_name['task'].fields.append(
  _LISTTASK.fields_by_name['task_collect_disk'])
_LISTTASK.fields_by_name['task_collect_disk'].containing_oneof = _LISTTASK.oneofs_by_name['task']
_LISTTASK.oneofs_by_name['task'].fields.append(
  _LISTTASK.fields_by_name['task_collect_memory'])
_LISTTASK.fields_by_name['task_collect_memory'].containing_oneof = _LISTTASK.oneofs_by_name['task']
_CREATETARGETREQUEST.fields_by_name['ssh'].message_type = fact_dot_tasks__pb2._SSHACCESS
_CREATETARGETREQUEST.oneofs_by_name['access'].fields.append(
  _CREATETARGETREQUEST.fields_by_name['ssh'])
_CREATETARGETREQUEST.fields_by_name['ssh'].containing_oneof = _CREATETARGETREQUEST.oneofs_by_name['access']
_LISTTARGETRESULT.fields_by_name['targets'].message_type = _LISTTARGET
_LISTTARGET.fields_by_name['ssh'].message_type = fact_dot_tasks__pb2._SSHACCESS
_LISTTARGET.oneofs_by_name['access'].fields.append(
  _LISTTARGET.fields_by_name['ssh'])
_LISTTARGET.fields_by_name['ssh'].containing_oneof = _LISTTARGET.oneofs_by_name['access']
DESCRIPTOR.message_types_by_name['CreateTaskRequest'] = _CREATETASKREQUEST
DESCRIPTOR.message_types_by_name['CreateTaskResult'] = _CREATETASKRESULT
DESCRIPTOR.message_types_by_name['ListTaskRequest'] = _LISTTASKREQUEST
DESCRIPTOR.message_types_by_name['ListTaskResult'] = _LISTTASKRESULT
DESCRIPTOR.message_types_by_name['ListTask'] = _LISTTASK
DESCRIPTOR.message_types_by_name['CreateTargetRequest'] = _CREATETARGETREQUEST
DESCRIPTOR.message_types_by_name['CreateTargetResult'] = _CREATETARGETRESULT
DESCRIPTOR.message_types_by_name['ListTargetRequest'] = _LISTTARGETREQUEST
DESCRIPTOR.message_types_by_name['ListTargetResult'] = _LISTTARGETRESULT
DESCRIPTOR.message_types_by_name['ListTarget'] = _LISTTARGET
DESCRIPTOR.message_types_by_name['ListWorkerRequest'] = _LISTWORKERREQUEST
DESCRIPTOR.message_types_by_name['ListWorkerResult'] = _LISTWORKERRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateTaskRequest = _reflection.GeneratedProtocolMessageType('CreateTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATETASKREQUEST,
  '__module__' : 'fact.management_pb2'
  # @@protoc_insertion_point(class_scope:CreateTaskRequest)
  })
_sym_db.RegisterMessage(CreateTaskRequest)

CreateTaskResult = _reflection.GeneratedProtocolMessageType('CreateTaskResult', (_message.Message,), {
  'DESCRIPTOR' : _CREATETASKRESULT,
  '__module__' : 'fact.management_pb2'
  # @@protoc_insertion_point(class_scope:CreateTaskResult)
  })
_sym_db.RegisterMessage(CreateTaskResult)

ListTaskRequest = _reflection.GeneratedProtocolMessageType('ListTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTASKREQUEST,
  '__module__' : 'fact.management_pb2'
  # @@protoc_insertion_point(class_scope:ListTaskRequest)
  })
_sym_db.RegisterMessage(ListTaskRequest)

ListTaskResult = _reflection.GeneratedProtocolMessageType('ListTaskResult', (_message.Message,), {
  'DESCRIPTOR' : _LISTTASKRESULT,
  '__module__' : 'fact.management_pb2'
  # @@protoc_insertion_point(class_scope:ListTaskResult)
  })
_sym_db.RegisterMessage(ListTaskResult)

ListTask = _reflection.GeneratedProtocolMessageType('ListTask', (_message.Message,), {
  'DESCRIPTOR' : _LISTTASK,
  '__module__' : 'fact.management_pb2'
  # @@protoc_insertion_point(class_scope:ListTask)
  })
_sym_db.RegisterMessage(ListTask)

CreateTargetRequest = _reflection.GeneratedProtocolMessageType('CreateTargetRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATETARGETREQUEST,
  '__module__' : 'fact.management_pb2'
  # @@protoc_insertion_point(class_scope:CreateTargetRequest)
  })
_sym_db.RegisterMessage(CreateTargetRequest)

CreateTargetResult = _reflection.GeneratedProtocolMessageType('CreateTargetResult', (_message.Message,), {
  'DESCRIPTOR' : _CREATETARGETRESULT,
  '__module__' : 'fact.management_pb2'
  # @@protoc_insertion_point(class_scope:CreateTargetResult)
  })
_sym_db.RegisterMessage(CreateTargetResult)

ListTargetRequest = _reflection.GeneratedProtocolMessageType('ListTargetRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTARGETREQUEST,
  '__module__' : 'fact.management_pb2'
  # @@protoc_insertion_point(class_scope:ListTargetRequest)
  })
_sym_db.RegisterMessage(ListTargetRequest)

ListTargetResult = _reflection.GeneratedProtocolMessageType('ListTargetResult', (_message.Message,), {
  'DESCRIPTOR' : _LISTTARGETRESULT,
  '__module__' : 'fact.management_pb2'
  # @@protoc_insertion_point(class_scope:ListTargetResult)
  })
_sym_db.RegisterMessage(ListTargetResult)

ListTarget = _reflection.GeneratedProtocolMessageType('ListTarget', (_message.Message,), {
  'DESCRIPTOR' : _LISTTARGET,
  '__module__' : 'fact.management_pb2'
  # @@protoc_insertion_point(class_scope:ListTarget)
  })
_sym_db.RegisterMessage(ListTarget)

ListWorkerRequest = _reflection.GeneratedProtocolMessageType('ListWorkerRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTWORKERREQUEST,
  '__module__' : 'fact.management_pb2'
  # @@protoc_insertion_point(class_scope:ListWorkerRequest)
  })
_sym_db.RegisterMessage(ListWorkerRequest)

ListWorkerResult = _reflection.GeneratedProtocolMessageType('ListWorkerResult', (_message.Message,), {
  'DESCRIPTOR' : _LISTWORKERRESULT,
  '__module__' : 'fact.management_pb2'
  # @@protoc_insertion_point(class_scope:ListWorkerResult)
  })
_sym_db.RegisterMessage(ListWorkerResult)



_MANAGEMENT = _descriptor.ServiceDescriptor(
  name='Management',
  full_name='Management',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1111,
  serialized_end=1388,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateTask',
    full_name='Management.CreateTask',
    index=0,
    containing_service=None,
    input_type=_CREATETASKREQUEST,
    output_type=_CREATETASKRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListTask',
    full_name='Management.ListTask',
    index=1,
    containing_service=None,
    input_type=_LISTTASKREQUEST,
    output_type=_LISTTASKRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateTarget',
    full_name='Management.CreateTarget',
    index=2,
    containing_service=None,
    input_type=_CREATETARGETREQUEST,
    output_type=_CREATETARGETRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListTarget',
    full_name='Management.ListTarget',
    index=3,
    containing_service=None,
    input_type=_LISTTARGETREQUEST,
    output_type=_LISTTARGETRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListWorker',
    full_name='Management.ListWorker',
    index=4,
    containing_service=None,
    input_type=_LISTWORKERREQUEST,
    output_type=_LISTWORKERRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MANAGEMENT)

DESCRIPTOR.services_by_name['Management'] = _MANAGEMENT

# @@protoc_insertion_point(module_scope)
