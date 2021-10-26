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


from fact import tasks_pb2 as fact_dot_tasks__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fact/controller.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15\x66\x61\x63t/controller.proto\x1a\x10\x66\x61\x63t/tasks.proto\"\x7f\n\x0eSessionResults\x12\x32\n\x13worker_registration\x18\x01 \x01(\x0b\x32\x13.WorkerRegistrationH\x00\x12/\n\x12worker_task_result\x18\x02 \x01(\x0b\x32\x11.WorkerTaskResultH\x00\x42\x08\n\x06result\"l\n\rSessionEvents\x12.\n\x11worker_acceptance\x18\x01 \x01(\x0b\x32\x11.WorkerAcceptanceH\x00\x12\"\n\x0bworker_task\x18\x02 \x01(\x0b\x32\x0b.WorkerTaskH\x00\x42\x07\n\x05\x65vent\"T\n\x12WorkerRegistration\x12\x1a\n\rprevious_uuid\x18\x01 \x01(\x0cH\x00\x88\x01\x01\x12\x10\n\x08hostname\x18\x02 \x01(\tB\x10\n\x0e_previous_uuid\" \n\x10WorkerAcceptance\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\"\xfe\x01\n\nWorkerTask\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\x12\x1c\n\x06target\x18\x02 \x01(\x0b\x32\x07.TargetH\x01\x88\x01\x01\x12\x1e\n\ttask_none\x18\x03 \x01(\x0b\x32\t.TaskNoneH\x00\x12-\n\x11task_collect_disk\x18\x04 \x01(\x0b\x32\x10.TaskCollectDiskH\x00\x12\x31\n\x13task_collect_memory\x18\x05 \x01(\x0b\x32\x12.TaskCollectMemoryH\x00\x12/\n\x12task_collect_lsblk\x18\x06 \x01(\x0b\x32\x11.TaskCollectLsblkH\x00\x42\x06\n\x04taskB\t\n\x07_target\"\xf3\x01\n\x10WorkerTaskResult\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\x12$\n\ttask_none\x18\x02 \x01(\x0b\x32\x0f.TaskNoneResultH\x00\x12\x33\n\x11task_collect_disk\x18\x03 \x01(\x0b\x32\x16.TaskCollectDiskResultH\x00\x12\x37\n\x13task_collect_memory\x18\x04 \x01(\x0b\x32\x18.TaskCollectMemoryResultH\x00\x12\x35\n\x12task_collect_lsblk\x18\x05 \x01(\x0b\x32\x17.TaskCollectLsblkResultH\x00\x42\x06\n\x04task2=\n\x0bWorkerTasks\x12.\n\x07Session\x12\x0f.SessionResults\x1a\x0e.SessionEvents(\x01\x30\x01\x62\x06proto3'
  ,
  dependencies=[fact_dot_tasks__pb2.DESCRIPTOR,])




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
  serialized_start=43,
  serialized_end=170,
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
  serialized_start=172,
  serialized_end=280,
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
    _descriptor.OneofDescriptor(
      name='_previous_uuid', full_name='WorkerRegistration._previous_uuid',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=282,
  serialized_end=366,
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
  serialized_start=368,
  serialized_end=400,
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
      name='uuid', full_name='WorkerTask.uuid', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='WorkerTask.target', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_none', full_name='WorkerTask.task_none', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_collect_disk', full_name='WorkerTask.task_collect_disk', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_collect_memory', full_name='WorkerTask.task_collect_memory', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_collect_lsblk', full_name='WorkerTask.task_collect_lsblk', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='_target', full_name='WorkerTask._target',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=403,
  serialized_end=657,
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
      name='uuid', full_name='WorkerTaskResult.uuid', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_none', full_name='WorkerTaskResult.task_none', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_collect_disk', full_name='WorkerTaskResult.task_collect_disk', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_collect_memory', full_name='WorkerTaskResult.task_collect_memory', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_collect_lsblk', full_name='WorkerTaskResult.task_collect_lsblk', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=660,
  serialized_end=903,
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
_WORKERREGISTRATION.oneofs_by_name['_previous_uuid'].fields.append(
  _WORKERREGISTRATION.fields_by_name['previous_uuid'])
_WORKERREGISTRATION.fields_by_name['previous_uuid'].containing_oneof = _WORKERREGISTRATION.oneofs_by_name['_previous_uuid']
_WORKERTASK.fields_by_name['target'].message_type = fact_dot_tasks__pb2._TARGET
_WORKERTASK.fields_by_name['task_none'].message_type = fact_dot_tasks__pb2._TASKNONE
_WORKERTASK.fields_by_name['task_collect_disk'].message_type = fact_dot_tasks__pb2._TASKCOLLECTDISK
_WORKERTASK.fields_by_name['task_collect_memory'].message_type = fact_dot_tasks__pb2._TASKCOLLECTMEMORY
_WORKERTASK.fields_by_name['task_collect_lsblk'].message_type = fact_dot_tasks__pb2._TASKCOLLECTLSBLK
_WORKERTASK.oneofs_by_name['task'].fields.append(
  _WORKERTASK.fields_by_name['task_none'])
_WORKERTASK.fields_by_name['task_none'].containing_oneof = _WORKERTASK.oneofs_by_name['task']
_WORKERTASK.oneofs_by_name['task'].fields.append(
  _WORKERTASK.fields_by_name['task_collect_disk'])
_WORKERTASK.fields_by_name['task_collect_disk'].containing_oneof = _WORKERTASK.oneofs_by_name['task']
_WORKERTASK.oneofs_by_name['task'].fields.append(
  _WORKERTASK.fields_by_name['task_collect_memory'])
_WORKERTASK.fields_by_name['task_collect_memory'].containing_oneof = _WORKERTASK.oneofs_by_name['task']
_WORKERTASK.oneofs_by_name['task'].fields.append(
  _WORKERTASK.fields_by_name['task_collect_lsblk'])
_WORKERTASK.fields_by_name['task_collect_lsblk'].containing_oneof = _WORKERTASK.oneofs_by_name['task']
_WORKERTASK.oneofs_by_name['_target'].fields.append(
  _WORKERTASK.fields_by_name['target'])
_WORKERTASK.fields_by_name['target'].containing_oneof = _WORKERTASK.oneofs_by_name['_target']
_WORKERTASKRESULT.fields_by_name['task_none'].message_type = fact_dot_tasks__pb2._TASKNONERESULT
_WORKERTASKRESULT.fields_by_name['task_collect_disk'].message_type = fact_dot_tasks__pb2._TASKCOLLECTDISKRESULT
_WORKERTASKRESULT.fields_by_name['task_collect_memory'].message_type = fact_dot_tasks__pb2._TASKCOLLECTMEMORYRESULT
_WORKERTASKRESULT.fields_by_name['task_collect_lsblk'].message_type = fact_dot_tasks__pb2._TASKCOLLECTLSBLKRESULT
_WORKERTASKRESULT.oneofs_by_name['task'].fields.append(
  _WORKERTASKRESULT.fields_by_name['task_none'])
_WORKERTASKRESULT.fields_by_name['task_none'].containing_oneof = _WORKERTASKRESULT.oneofs_by_name['task']
_WORKERTASKRESULT.oneofs_by_name['task'].fields.append(
  _WORKERTASKRESULT.fields_by_name['task_collect_disk'])
_WORKERTASKRESULT.fields_by_name['task_collect_disk'].containing_oneof = _WORKERTASKRESULT.oneofs_by_name['task']
_WORKERTASKRESULT.oneofs_by_name['task'].fields.append(
  _WORKERTASKRESULT.fields_by_name['task_collect_memory'])
_WORKERTASKRESULT.fields_by_name['task_collect_memory'].containing_oneof = _WORKERTASKRESULT.oneofs_by_name['task']
_WORKERTASKRESULT.oneofs_by_name['task'].fields.append(
  _WORKERTASKRESULT.fields_by_name['task_collect_lsblk'])
_WORKERTASKRESULT.fields_by_name['task_collect_lsblk'].containing_oneof = _WORKERTASKRESULT.oneofs_by_name['task']
DESCRIPTOR.message_types_by_name['SessionResults'] = _SESSIONRESULTS
DESCRIPTOR.message_types_by_name['SessionEvents'] = _SESSIONEVENTS
DESCRIPTOR.message_types_by_name['WorkerRegistration'] = _WORKERREGISTRATION
DESCRIPTOR.message_types_by_name['WorkerAcceptance'] = _WORKERACCEPTANCE
DESCRIPTOR.message_types_by_name['WorkerTask'] = _WORKERTASK
DESCRIPTOR.message_types_by_name['WorkerTaskResult'] = _WORKERTASKRESULT
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



_WORKERTASKS = _descriptor.ServiceDescriptor(
  name='WorkerTasks',
  full_name='WorkerTasks',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=905,
  serialized_end=966,
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
