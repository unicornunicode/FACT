/* eslint-disable */
import Long from "long";
import { grpc } from "@improbable-eng/grpc-web";
import _m0 from "protobufjs/minimal";
import { BrowserHeaders } from "browser-headers";
import { Timestamp } from "../google/protobuf/timestamp";
import {
  TaskNone,
  TaskCollectDisk,
  TaskCollectMemory,
  TaskCollectLsblk,
  SSHAccess,
  LsblkResult,
} from "../fact/tasks";

export const protobufPackage = "";

export interface CreateTaskRequest {
  /** TODO: Shorten these */
  taskNone: TaskNone | undefined;
  taskCollectDisk: TaskCollectDisk | undefined;
  taskCollectMemory: TaskCollectMemory | undefined;
  taskCollectLsblk: TaskCollectLsblk | undefined;
  target: Uint8Array;
}

export interface CreateTaskResult {
  uuid: Uint8Array;
}

export interface ListTaskRequest {
  limit: number;
}

export interface ListTaskResult {
  tasks: ListTask[];
}

export interface ListTask {
  uuid: Uint8Array;
  status: ListTask_Status;
  createdAt: Date | undefined;
  assignedAt: Date | undefined;
  completedAt: Date | undefined;
  /** Target UUID */
  target: Uint8Array;
  taskNone: TaskNone | undefined;
  taskCollectDisk: TaskCollectDisk | undefined;
  taskCollectMemory: TaskCollectMemory | undefined;
  taskCollectLsblk: TaskCollectLsblk | undefined;
  /** Worker UUID */
  worker: Uint8Array;
}

export enum ListTask_Status {
  WAITING = 0,
  RUNNING = 1,
  COMPLETE = 2,
  UNRECOGNIZED = -1,
}

export function listTask_StatusFromJSON(object: any): ListTask_Status {
  switch (object) {
    case 0:
    case "WAITING":
      return ListTask_Status.WAITING;
    case 1:
    case "RUNNING":
      return ListTask_Status.RUNNING;
    case 2:
    case "COMPLETE":
      return ListTask_Status.COMPLETE;
    case -1:
    case "UNRECOGNIZED":
    default:
      return ListTask_Status.UNRECOGNIZED;
  }
}

export function listTask_StatusToJSON(object: ListTask_Status): string {
  switch (object) {
    case ListTask_Status.WAITING:
      return "WAITING";
    case ListTask_Status.RUNNING:
      return "RUNNING";
    case ListTask_Status.COMPLETE:
      return "COMPLETE";
    default:
      return "UNKNOWN";
  }
}

export interface CreateTargetRequest {
  name: string;
  ssh: SSHAccess | undefined;
}

export interface CreateTargetResult {
  uuid: Uint8Array;
}

export interface ListTargetRequest {}

export interface ListTargetResult {
  targets: ListTarget[];
}

export interface GetTargetRequest {
  uuid: Uint8Array;
}

export interface GetTargetResult {
  target: ListTarget | undefined;
}

export interface ListTargetLsblkRequest {
  uuid: Uint8Array;
}

export interface ListTargetLsblkResult {
  lsblkResults: LsblkResult[];
}

export interface ListTarget {
  uuid: Uint8Array;
  name: string;
  ssh: SSHAccess | undefined;
}

export interface ListWorkerRequest {}

export interface ListWorkerResult {
  workers: ListWorker[];
}

export interface ListWorker {
  uuid: Uint8Array;
  hostname: string;
}

const baseCreateTaskRequest: object = {};

export const CreateTaskRequest = {
  encode(
    message: CreateTaskRequest,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    if (message.taskNone !== undefined) {
      TaskNone.encode(message.taskNone, writer.uint32(10).fork()).ldelim();
    }
    if (message.taskCollectDisk !== undefined) {
      TaskCollectDisk.encode(
        message.taskCollectDisk,
        writer.uint32(18).fork()
      ).ldelim();
    }
    if (message.taskCollectMemory !== undefined) {
      TaskCollectMemory.encode(
        message.taskCollectMemory,
        writer.uint32(26).fork()
      ).ldelim();
    }
    if (message.taskCollectLsblk !== undefined) {
      TaskCollectLsblk.encode(
        message.taskCollectLsblk,
        writer.uint32(42).fork()
      ).ldelim();
    }
    if (message.target.length !== 0) {
      writer.uint32(34).bytes(message.target);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateTaskRequest {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseCreateTaskRequest } as CreateTaskRequest;
    message.target = new Uint8Array();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.taskNone = TaskNone.decode(reader, reader.uint32());
          break;
        case 2:
          message.taskCollectDisk = TaskCollectDisk.decode(
            reader,
            reader.uint32()
          );
          break;
        case 3:
          message.taskCollectMemory = TaskCollectMemory.decode(
            reader,
            reader.uint32()
          );
          break;
        case 5:
          message.taskCollectLsblk = TaskCollectLsblk.decode(
            reader,
            reader.uint32()
          );
          break;
        case 4:
          message.target = reader.bytes();
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): CreateTaskRequest {
    const message = { ...baseCreateTaskRequest } as CreateTaskRequest;
    message.target = new Uint8Array();
    if (object.taskNone !== undefined && object.taskNone !== null) {
      message.taskNone = TaskNone.fromJSON(object.taskNone);
    } else {
      message.taskNone = undefined;
    }
    if (
      object.taskCollectDisk !== undefined &&
      object.taskCollectDisk !== null
    ) {
      message.taskCollectDisk = TaskCollectDisk.fromJSON(
        object.taskCollectDisk
      );
    } else {
      message.taskCollectDisk = undefined;
    }
    if (
      object.taskCollectMemory !== undefined &&
      object.taskCollectMemory !== null
    ) {
      message.taskCollectMemory = TaskCollectMemory.fromJSON(
        object.taskCollectMemory
      );
    } else {
      message.taskCollectMemory = undefined;
    }
    if (
      object.taskCollectLsblk !== undefined &&
      object.taskCollectLsblk !== null
    ) {
      message.taskCollectLsblk = TaskCollectLsblk.fromJSON(
        object.taskCollectLsblk
      );
    } else {
      message.taskCollectLsblk = undefined;
    }
    if (object.target !== undefined && object.target !== null) {
      message.target = bytesFromBase64(object.target);
    }
    return message;
  },

  toJSON(message: CreateTaskRequest): unknown {
    const obj: any = {};
    message.taskNone !== undefined &&
      (obj.taskNone = message.taskNone
        ? TaskNone.toJSON(message.taskNone)
        : undefined);
    message.taskCollectDisk !== undefined &&
      (obj.taskCollectDisk = message.taskCollectDisk
        ? TaskCollectDisk.toJSON(message.taskCollectDisk)
        : undefined);
    message.taskCollectMemory !== undefined &&
      (obj.taskCollectMemory = message.taskCollectMemory
        ? TaskCollectMemory.toJSON(message.taskCollectMemory)
        : undefined);
    message.taskCollectLsblk !== undefined &&
      (obj.taskCollectLsblk = message.taskCollectLsblk
        ? TaskCollectLsblk.toJSON(message.taskCollectLsblk)
        : undefined);
    message.target !== undefined &&
      (obj.target = base64FromBytes(
        message.target !== undefined ? message.target : new Uint8Array()
      ));
    return obj;
  },

  fromPartial(object: DeepPartial<CreateTaskRequest>): CreateTaskRequest {
    const message = { ...baseCreateTaskRequest } as CreateTaskRequest;
    if (object.taskNone !== undefined && object.taskNone !== null) {
      message.taskNone = TaskNone.fromPartial(object.taskNone);
    } else {
      message.taskNone = undefined;
    }
    if (
      object.taskCollectDisk !== undefined &&
      object.taskCollectDisk !== null
    ) {
      message.taskCollectDisk = TaskCollectDisk.fromPartial(
        object.taskCollectDisk
      );
    } else {
      message.taskCollectDisk = undefined;
    }
    if (
      object.taskCollectMemory !== undefined &&
      object.taskCollectMemory !== null
    ) {
      message.taskCollectMemory = TaskCollectMemory.fromPartial(
        object.taskCollectMemory
      );
    } else {
      message.taskCollectMemory = undefined;
    }
    if (
      object.taskCollectLsblk !== undefined &&
      object.taskCollectLsblk !== null
    ) {
      message.taskCollectLsblk = TaskCollectLsblk.fromPartial(
        object.taskCollectLsblk
      );
    } else {
      message.taskCollectLsblk = undefined;
    }
    if (object.target !== undefined && object.target !== null) {
      message.target = object.target;
    } else {
      message.target = new Uint8Array();
    }
    return message;
  },
};

const baseCreateTaskResult: object = {};

export const CreateTaskResult = {
  encode(
    message: CreateTaskResult,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    if (message.uuid.length !== 0) {
      writer.uint32(10).bytes(message.uuid);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateTaskResult {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseCreateTaskResult } as CreateTaskResult;
    message.uuid = new Uint8Array();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.uuid = reader.bytes();
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): CreateTaskResult {
    const message = { ...baseCreateTaskResult } as CreateTaskResult;
    message.uuid = new Uint8Array();
    if (object.uuid !== undefined && object.uuid !== null) {
      message.uuid = bytesFromBase64(object.uuid);
    }
    return message;
  },

  toJSON(message: CreateTaskResult): unknown {
    const obj: any = {};
    message.uuid !== undefined &&
      (obj.uuid = base64FromBytes(
        message.uuid !== undefined ? message.uuid : new Uint8Array()
      ));
    return obj;
  },

  fromPartial(object: DeepPartial<CreateTaskResult>): CreateTaskResult {
    const message = { ...baseCreateTaskResult } as CreateTaskResult;
    if (object.uuid !== undefined && object.uuid !== null) {
      message.uuid = object.uuid;
    } else {
      message.uuid = new Uint8Array();
    }
    return message;
  },
};

const baseListTaskRequest: object = { limit: 0 };

export const ListTaskRequest = {
  encode(
    message: ListTaskRequest,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    if (message.limit !== 0) {
      writer.uint32(8).uint64(message.limit);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): ListTaskRequest {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseListTaskRequest } as ListTaskRequest;
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.limit = longToNumber(reader.uint64() as Long);
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): ListTaskRequest {
    const message = { ...baseListTaskRequest } as ListTaskRequest;
    if (object.limit !== undefined && object.limit !== null) {
      message.limit = Number(object.limit);
    } else {
      message.limit = 0;
    }
    return message;
  },

  toJSON(message: ListTaskRequest): unknown {
    const obj: any = {};
    message.limit !== undefined && (obj.limit = message.limit);
    return obj;
  },

  fromPartial(object: DeepPartial<ListTaskRequest>): ListTaskRequest {
    const message = { ...baseListTaskRequest } as ListTaskRequest;
    if (object.limit !== undefined && object.limit !== null) {
      message.limit = object.limit;
    } else {
      message.limit = 0;
    }
    return message;
  },
};

const baseListTaskResult: object = {};

export const ListTaskResult = {
  encode(
    message: ListTaskResult,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    for (const v of message.tasks) {
      ListTask.encode(v!, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): ListTaskResult {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseListTaskResult } as ListTaskResult;
    message.tasks = [];
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.tasks.push(ListTask.decode(reader, reader.uint32()));
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): ListTaskResult {
    const message = { ...baseListTaskResult } as ListTaskResult;
    message.tasks = [];
    if (object.tasks !== undefined && object.tasks !== null) {
      for (const e of object.tasks) {
        message.tasks.push(ListTask.fromJSON(e));
      }
    }
    return message;
  },

  toJSON(message: ListTaskResult): unknown {
    const obj: any = {};
    if (message.tasks) {
      obj.tasks = message.tasks.map((e) =>
        e ? ListTask.toJSON(e) : undefined
      );
    } else {
      obj.tasks = [];
    }
    return obj;
  },

  fromPartial(object: DeepPartial<ListTaskResult>): ListTaskResult {
    const message = { ...baseListTaskResult } as ListTaskResult;
    message.tasks = [];
    if (object.tasks !== undefined && object.tasks !== null) {
      for (const e of object.tasks) {
        message.tasks.push(ListTask.fromPartial(e));
      }
    }
    return message;
  },
};

const baseListTask: object = { status: 0 };

export const ListTask = {
  encode(
    message: ListTask,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    if (message.uuid.length !== 0) {
      writer.uint32(10).bytes(message.uuid);
    }
    if (message.status !== 0) {
      writer.uint32(16).int32(message.status);
    }
    if (message.createdAt !== undefined) {
      Timestamp.encode(
        toTimestamp(message.createdAt),
        writer.uint32(26).fork()
      ).ldelim();
    }
    if (message.assignedAt !== undefined) {
      Timestamp.encode(
        toTimestamp(message.assignedAt),
        writer.uint32(34).fork()
      ).ldelim();
    }
    if (message.completedAt !== undefined) {
      Timestamp.encode(
        toTimestamp(message.completedAt),
        writer.uint32(42).fork()
      ).ldelim();
    }
    if (message.target.length !== 0) {
      writer.uint32(50).bytes(message.target);
    }
    if (message.taskNone !== undefined) {
      TaskNone.encode(message.taskNone, writer.uint32(58).fork()).ldelim();
    }
    if (message.taskCollectDisk !== undefined) {
      TaskCollectDisk.encode(
        message.taskCollectDisk,
        writer.uint32(66).fork()
      ).ldelim();
    }
    if (message.taskCollectMemory !== undefined) {
      TaskCollectMemory.encode(
        message.taskCollectMemory,
        writer.uint32(74).fork()
      ).ldelim();
    }
    if (message.taskCollectLsblk !== undefined) {
      TaskCollectLsblk.encode(
        message.taskCollectLsblk,
        writer.uint32(90).fork()
      ).ldelim();
    }
    if (message.worker.length !== 0) {
      writer.uint32(82).bytes(message.worker);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): ListTask {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseListTask } as ListTask;
    message.uuid = new Uint8Array();
    message.target = new Uint8Array();
    message.worker = new Uint8Array();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.uuid = reader.bytes();
          break;
        case 2:
          message.status = reader.int32() as any;
          break;
        case 3:
          message.createdAt = fromTimestamp(
            Timestamp.decode(reader, reader.uint32())
          );
          break;
        case 4:
          message.assignedAt = fromTimestamp(
            Timestamp.decode(reader, reader.uint32())
          );
          break;
        case 5:
          message.completedAt = fromTimestamp(
            Timestamp.decode(reader, reader.uint32())
          );
          break;
        case 6:
          message.target = reader.bytes();
          break;
        case 7:
          message.taskNone = TaskNone.decode(reader, reader.uint32());
          break;
        case 8:
          message.taskCollectDisk = TaskCollectDisk.decode(
            reader,
            reader.uint32()
          );
          break;
        case 9:
          message.taskCollectMemory = TaskCollectMemory.decode(
            reader,
            reader.uint32()
          );
          break;
        case 11:
          message.taskCollectLsblk = TaskCollectLsblk.decode(
            reader,
            reader.uint32()
          );
          break;
        case 10:
          message.worker = reader.bytes();
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): ListTask {
    const message = { ...baseListTask } as ListTask;
    message.uuid = new Uint8Array();
    message.target = new Uint8Array();
    message.worker = new Uint8Array();
    if (object.uuid !== undefined && object.uuid !== null) {
      message.uuid = bytesFromBase64(object.uuid);
    }
    if (object.status !== undefined && object.status !== null) {
      message.status = listTask_StatusFromJSON(object.status);
    } else {
      message.status = 0;
    }
    if (object.createdAt !== undefined && object.createdAt !== null) {
      message.createdAt = fromJsonTimestamp(object.createdAt);
    } else {
      message.createdAt = undefined;
    }
    if (object.assignedAt !== undefined && object.assignedAt !== null) {
      message.assignedAt = fromJsonTimestamp(object.assignedAt);
    } else {
      message.assignedAt = undefined;
    }
    if (object.completedAt !== undefined && object.completedAt !== null) {
      message.completedAt = fromJsonTimestamp(object.completedAt);
    } else {
      message.completedAt = undefined;
    }
    if (object.target !== undefined && object.target !== null) {
      message.target = bytesFromBase64(object.target);
    }
    if (object.taskNone !== undefined && object.taskNone !== null) {
      message.taskNone = TaskNone.fromJSON(object.taskNone);
    } else {
      message.taskNone = undefined;
    }
    if (
      object.taskCollectDisk !== undefined &&
      object.taskCollectDisk !== null
    ) {
      message.taskCollectDisk = TaskCollectDisk.fromJSON(
        object.taskCollectDisk
      );
    } else {
      message.taskCollectDisk = undefined;
    }
    if (
      object.taskCollectMemory !== undefined &&
      object.taskCollectMemory !== null
    ) {
      message.taskCollectMemory = TaskCollectMemory.fromJSON(
        object.taskCollectMemory
      );
    } else {
      message.taskCollectMemory = undefined;
    }
    if (
      object.taskCollectLsblk !== undefined &&
      object.taskCollectLsblk !== null
    ) {
      message.taskCollectLsblk = TaskCollectLsblk.fromJSON(
        object.taskCollectLsblk
      );
    } else {
      message.taskCollectLsblk = undefined;
    }
    if (object.worker !== undefined && object.worker !== null) {
      message.worker = bytesFromBase64(object.worker);
    }
    return message;
  },

  toJSON(message: ListTask): unknown {
    const obj: any = {};
    message.uuid !== undefined &&
      (obj.uuid = base64FromBytes(
        message.uuid !== undefined ? message.uuid : new Uint8Array()
      ));
    message.status !== undefined &&
      (obj.status = listTask_StatusToJSON(message.status));
    message.createdAt !== undefined &&
      (obj.createdAt = message.createdAt.toISOString());
    message.assignedAt !== undefined &&
      (obj.assignedAt = message.assignedAt.toISOString());
    message.completedAt !== undefined &&
      (obj.completedAt = message.completedAt.toISOString());
    message.target !== undefined &&
      (obj.target = base64FromBytes(
        message.target !== undefined ? message.target : new Uint8Array()
      ));
    message.taskNone !== undefined &&
      (obj.taskNone = message.taskNone
        ? TaskNone.toJSON(message.taskNone)
        : undefined);
    message.taskCollectDisk !== undefined &&
      (obj.taskCollectDisk = message.taskCollectDisk
        ? TaskCollectDisk.toJSON(message.taskCollectDisk)
        : undefined);
    message.taskCollectMemory !== undefined &&
      (obj.taskCollectMemory = message.taskCollectMemory
        ? TaskCollectMemory.toJSON(message.taskCollectMemory)
        : undefined);
    message.taskCollectLsblk !== undefined &&
      (obj.taskCollectLsblk = message.taskCollectLsblk
        ? TaskCollectLsblk.toJSON(message.taskCollectLsblk)
        : undefined);
    message.worker !== undefined &&
      (obj.worker = base64FromBytes(
        message.worker !== undefined ? message.worker : new Uint8Array()
      ));
    return obj;
  },

  fromPartial(object: DeepPartial<ListTask>): ListTask {
    const message = { ...baseListTask } as ListTask;
    if (object.uuid !== undefined && object.uuid !== null) {
      message.uuid = object.uuid;
    } else {
      message.uuid = new Uint8Array();
    }
    if (object.status !== undefined && object.status !== null) {
      message.status = object.status;
    } else {
      message.status = 0;
    }
    if (object.createdAt !== undefined && object.createdAt !== null) {
      message.createdAt = object.createdAt;
    } else {
      message.createdAt = undefined;
    }
    if (object.assignedAt !== undefined && object.assignedAt !== null) {
      message.assignedAt = object.assignedAt;
    } else {
      message.assignedAt = undefined;
    }
    if (object.completedAt !== undefined && object.completedAt !== null) {
      message.completedAt = object.completedAt;
    } else {
      message.completedAt = undefined;
    }
    if (object.target !== undefined && object.target !== null) {
      message.target = object.target;
    } else {
      message.target = new Uint8Array();
    }
    if (object.taskNone !== undefined && object.taskNone !== null) {
      message.taskNone = TaskNone.fromPartial(object.taskNone);
    } else {
      message.taskNone = undefined;
    }
    if (
      object.taskCollectDisk !== undefined &&
      object.taskCollectDisk !== null
    ) {
      message.taskCollectDisk = TaskCollectDisk.fromPartial(
        object.taskCollectDisk
      );
    } else {
      message.taskCollectDisk = undefined;
    }
    if (
      object.taskCollectMemory !== undefined &&
      object.taskCollectMemory !== null
    ) {
      message.taskCollectMemory = TaskCollectMemory.fromPartial(
        object.taskCollectMemory
      );
    } else {
      message.taskCollectMemory = undefined;
    }
    if (
      object.taskCollectLsblk !== undefined &&
      object.taskCollectLsblk !== null
    ) {
      message.taskCollectLsblk = TaskCollectLsblk.fromPartial(
        object.taskCollectLsblk
      );
    } else {
      message.taskCollectLsblk = undefined;
    }
    if (object.worker !== undefined && object.worker !== null) {
      message.worker = object.worker;
    } else {
      message.worker = new Uint8Array();
    }
    return message;
  },
};

const baseCreateTargetRequest: object = { name: "" };

export const CreateTargetRequest = {
  encode(
    message: CreateTargetRequest,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    if (message.name !== "") {
      writer.uint32(26).string(message.name);
    }
    if (message.ssh !== undefined) {
      SSHAccess.encode(message.ssh, writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateTargetRequest {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseCreateTargetRequest } as CreateTargetRequest;
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 3:
          message.name = reader.string();
          break;
        case 2:
          message.ssh = SSHAccess.decode(reader, reader.uint32());
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): CreateTargetRequest {
    const message = { ...baseCreateTargetRequest } as CreateTargetRequest;
    if (object.name !== undefined && object.name !== null) {
      message.name = String(object.name);
    } else {
      message.name = "";
    }
    if (object.ssh !== undefined && object.ssh !== null) {
      message.ssh = SSHAccess.fromJSON(object.ssh);
    } else {
      message.ssh = undefined;
    }
    return message;
  },

  toJSON(message: CreateTargetRequest): unknown {
    const obj: any = {};
    message.name !== undefined && (obj.name = message.name);
    message.ssh !== undefined &&
      (obj.ssh = message.ssh ? SSHAccess.toJSON(message.ssh) : undefined);
    return obj;
  },

  fromPartial(object: DeepPartial<CreateTargetRequest>): CreateTargetRequest {
    const message = { ...baseCreateTargetRequest } as CreateTargetRequest;
    if (object.name !== undefined && object.name !== null) {
      message.name = object.name;
    } else {
      message.name = "";
    }
    if (object.ssh !== undefined && object.ssh !== null) {
      message.ssh = SSHAccess.fromPartial(object.ssh);
    } else {
      message.ssh = undefined;
    }
    return message;
  },
};

const baseCreateTargetResult: object = {};

export const CreateTargetResult = {
  encode(
    message: CreateTargetResult,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    if (message.uuid.length !== 0) {
      writer.uint32(10).bytes(message.uuid);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateTargetResult {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseCreateTargetResult } as CreateTargetResult;
    message.uuid = new Uint8Array();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.uuid = reader.bytes();
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): CreateTargetResult {
    const message = { ...baseCreateTargetResult } as CreateTargetResult;
    message.uuid = new Uint8Array();
    if (object.uuid !== undefined && object.uuid !== null) {
      message.uuid = bytesFromBase64(object.uuid);
    }
    return message;
  },

  toJSON(message: CreateTargetResult): unknown {
    const obj: any = {};
    message.uuid !== undefined &&
      (obj.uuid = base64FromBytes(
        message.uuid !== undefined ? message.uuid : new Uint8Array()
      ));
    return obj;
  },

  fromPartial(object: DeepPartial<CreateTargetResult>): CreateTargetResult {
    const message = { ...baseCreateTargetResult } as CreateTargetResult;
    if (object.uuid !== undefined && object.uuid !== null) {
      message.uuid = object.uuid;
    } else {
      message.uuid = new Uint8Array();
    }
    return message;
  },
};

const baseListTargetRequest: object = {};

export const ListTargetRequest = {
  encode(
    _: ListTargetRequest,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): ListTargetRequest {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseListTargetRequest } as ListTargetRequest;
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(_: any): ListTargetRequest {
    const message = { ...baseListTargetRequest } as ListTargetRequest;
    return message;
  },

  toJSON(_: ListTargetRequest): unknown {
    const obj: any = {};
    return obj;
  },

  fromPartial(_: DeepPartial<ListTargetRequest>): ListTargetRequest {
    const message = { ...baseListTargetRequest } as ListTargetRequest;
    return message;
  },
};

const baseListTargetResult: object = {};

export const ListTargetResult = {
  encode(
    message: ListTargetResult,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    for (const v of message.targets) {
      ListTarget.encode(v!, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): ListTargetResult {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseListTargetResult } as ListTargetResult;
    message.targets = [];
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.targets.push(ListTarget.decode(reader, reader.uint32()));
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): ListTargetResult {
    const message = { ...baseListTargetResult } as ListTargetResult;
    message.targets = [];
    if (object.targets !== undefined && object.targets !== null) {
      for (const e of object.targets) {
        message.targets.push(ListTarget.fromJSON(e));
      }
    }
    return message;
  },

  toJSON(message: ListTargetResult): unknown {
    const obj: any = {};
    if (message.targets) {
      obj.targets = message.targets.map((e) =>
        e ? ListTarget.toJSON(e) : undefined
      );
    } else {
      obj.targets = [];
    }
    return obj;
  },

  fromPartial(object: DeepPartial<ListTargetResult>): ListTargetResult {
    const message = { ...baseListTargetResult } as ListTargetResult;
    message.targets = [];
    if (object.targets !== undefined && object.targets !== null) {
      for (const e of object.targets) {
        message.targets.push(ListTarget.fromPartial(e));
      }
    }
    return message;
  },
};

const baseGetTargetRequest: object = {};

export const GetTargetRequest = {
  encode(
    message: GetTargetRequest,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    if (message.uuid.length !== 0) {
      writer.uint32(10).bytes(message.uuid);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetTargetRequest {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseGetTargetRequest } as GetTargetRequest;
    message.uuid = new Uint8Array();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.uuid = reader.bytes();
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): GetTargetRequest {
    const message = { ...baseGetTargetRequest } as GetTargetRequest;
    message.uuid = new Uint8Array();
    if (object.uuid !== undefined && object.uuid !== null) {
      message.uuid = bytesFromBase64(object.uuid);
    }
    return message;
  },

  toJSON(message: GetTargetRequest): unknown {
    const obj: any = {};
    message.uuid !== undefined &&
      (obj.uuid = base64FromBytes(
        message.uuid !== undefined ? message.uuid : new Uint8Array()
      ));
    return obj;
  },

  fromPartial(object: DeepPartial<GetTargetRequest>): GetTargetRequest {
    const message = { ...baseGetTargetRequest } as GetTargetRequest;
    if (object.uuid !== undefined && object.uuid !== null) {
      message.uuid = object.uuid;
    } else {
      message.uuid = new Uint8Array();
    }
    return message;
  },
};

const baseGetTargetResult: object = {};

export const GetTargetResult = {
  encode(
    message: GetTargetResult,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    if (message.target !== undefined) {
      ListTarget.encode(message.target, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetTargetResult {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseGetTargetResult } as GetTargetResult;
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.target = ListTarget.decode(reader, reader.uint32());
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): GetTargetResult {
    const message = { ...baseGetTargetResult } as GetTargetResult;
    if (object.target !== undefined && object.target !== null) {
      message.target = ListTarget.fromJSON(object.target);
    } else {
      message.target = undefined;
    }
    return message;
  },

  toJSON(message: GetTargetResult): unknown {
    const obj: any = {};
    message.target !== undefined &&
      (obj.target = message.target
        ? ListTarget.toJSON(message.target)
        : undefined);
    return obj;
  },

  fromPartial(object: DeepPartial<GetTargetResult>): GetTargetResult {
    const message = { ...baseGetTargetResult } as GetTargetResult;
    if (object.target !== undefined && object.target !== null) {
      message.target = ListTarget.fromPartial(object.target);
    } else {
      message.target = undefined;
    }
    return message;
  },
};

const baseListTargetLsblkRequest: object = {};

export const ListTargetLsblkRequest = {
  encode(
    message: ListTargetLsblkRequest,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    if (message.uuid.length !== 0) {
      writer.uint32(10).bytes(message.uuid);
    }
    return writer;
  },

  decode(
    input: _m0.Reader | Uint8Array,
    length?: number
  ): ListTargetLsblkRequest {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseListTargetLsblkRequest } as ListTargetLsblkRequest;
    message.uuid = new Uint8Array();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.uuid = reader.bytes();
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): ListTargetLsblkRequest {
    const message = { ...baseListTargetLsblkRequest } as ListTargetLsblkRequest;
    message.uuid = new Uint8Array();
    if (object.uuid !== undefined && object.uuid !== null) {
      message.uuid = bytesFromBase64(object.uuid);
    }
    return message;
  },

  toJSON(message: ListTargetLsblkRequest): unknown {
    const obj: any = {};
    message.uuid !== undefined &&
      (obj.uuid = base64FromBytes(
        message.uuid !== undefined ? message.uuid : new Uint8Array()
      ));
    return obj;
  },

  fromPartial(
    object: DeepPartial<ListTargetLsblkRequest>
  ): ListTargetLsblkRequest {
    const message = { ...baseListTargetLsblkRequest } as ListTargetLsblkRequest;
    if (object.uuid !== undefined && object.uuid !== null) {
      message.uuid = object.uuid;
    } else {
      message.uuid = new Uint8Array();
    }
    return message;
  },
};

const baseListTargetLsblkResult: object = {};

export const ListTargetLsblkResult = {
  encode(
    message: ListTargetLsblkResult,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    for (const v of message.lsblkResults) {
      LsblkResult.encode(v!, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(
    input: _m0.Reader | Uint8Array,
    length?: number
  ): ListTargetLsblkResult {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseListTargetLsblkResult } as ListTargetLsblkResult;
    message.lsblkResults = [];
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.lsblkResults.push(
            LsblkResult.decode(reader, reader.uint32())
          );
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): ListTargetLsblkResult {
    const message = { ...baseListTargetLsblkResult } as ListTargetLsblkResult;
    message.lsblkResults = [];
    if (object.lsblkResults !== undefined && object.lsblkResults !== null) {
      for (const e of object.lsblkResults) {
        message.lsblkResults.push(LsblkResult.fromJSON(e));
      }
    }
    return message;
  },

  toJSON(message: ListTargetLsblkResult): unknown {
    const obj: any = {};
    if (message.lsblkResults) {
      obj.lsblkResults = message.lsblkResults.map((e) =>
        e ? LsblkResult.toJSON(e) : undefined
      );
    } else {
      obj.lsblkResults = [];
    }
    return obj;
  },

  fromPartial(
    object: DeepPartial<ListTargetLsblkResult>
  ): ListTargetLsblkResult {
    const message = { ...baseListTargetLsblkResult } as ListTargetLsblkResult;
    message.lsblkResults = [];
    if (object.lsblkResults !== undefined && object.lsblkResults !== null) {
      for (const e of object.lsblkResults) {
        message.lsblkResults.push(LsblkResult.fromPartial(e));
      }
    }
    return message;
  },
};

const baseListTarget: object = { name: "" };

export const ListTarget = {
  encode(
    message: ListTarget,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    if (message.uuid.length !== 0) {
      writer.uint32(10).bytes(message.uuid);
    }
    if (message.name !== "") {
      writer.uint32(26).string(message.name);
    }
    if (message.ssh !== undefined) {
      SSHAccess.encode(message.ssh, writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): ListTarget {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseListTarget } as ListTarget;
    message.uuid = new Uint8Array();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.uuid = reader.bytes();
          break;
        case 3:
          message.name = reader.string();
          break;
        case 2:
          message.ssh = SSHAccess.decode(reader, reader.uint32());
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): ListTarget {
    const message = { ...baseListTarget } as ListTarget;
    message.uuid = new Uint8Array();
    if (object.uuid !== undefined && object.uuid !== null) {
      message.uuid = bytesFromBase64(object.uuid);
    }
    if (object.name !== undefined && object.name !== null) {
      message.name = String(object.name);
    } else {
      message.name = "";
    }
    if (object.ssh !== undefined && object.ssh !== null) {
      message.ssh = SSHAccess.fromJSON(object.ssh);
    } else {
      message.ssh = undefined;
    }
    return message;
  },

  toJSON(message: ListTarget): unknown {
    const obj: any = {};
    message.uuid !== undefined &&
      (obj.uuid = base64FromBytes(
        message.uuid !== undefined ? message.uuid : new Uint8Array()
      ));
    message.name !== undefined && (obj.name = message.name);
    message.ssh !== undefined &&
      (obj.ssh = message.ssh ? SSHAccess.toJSON(message.ssh) : undefined);
    return obj;
  },

  fromPartial(object: DeepPartial<ListTarget>): ListTarget {
    const message = { ...baseListTarget } as ListTarget;
    if (object.uuid !== undefined && object.uuid !== null) {
      message.uuid = object.uuid;
    } else {
      message.uuid = new Uint8Array();
    }
    if (object.name !== undefined && object.name !== null) {
      message.name = object.name;
    } else {
      message.name = "";
    }
    if (object.ssh !== undefined && object.ssh !== null) {
      message.ssh = SSHAccess.fromPartial(object.ssh);
    } else {
      message.ssh = undefined;
    }
    return message;
  },
};

const baseListWorkerRequest: object = {};

export const ListWorkerRequest = {
  encode(
    _: ListWorkerRequest,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): ListWorkerRequest {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseListWorkerRequest } as ListWorkerRequest;
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(_: any): ListWorkerRequest {
    const message = { ...baseListWorkerRequest } as ListWorkerRequest;
    return message;
  },

  toJSON(_: ListWorkerRequest): unknown {
    const obj: any = {};
    return obj;
  },

  fromPartial(_: DeepPartial<ListWorkerRequest>): ListWorkerRequest {
    const message = { ...baseListWorkerRequest } as ListWorkerRequest;
    return message;
  },
};

const baseListWorkerResult: object = {};

export const ListWorkerResult = {
  encode(
    message: ListWorkerResult,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    for (const v of message.workers) {
      ListWorker.encode(v!, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): ListWorkerResult {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseListWorkerResult } as ListWorkerResult;
    message.workers = [];
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.workers.push(ListWorker.decode(reader, reader.uint32()));
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): ListWorkerResult {
    const message = { ...baseListWorkerResult } as ListWorkerResult;
    message.workers = [];
    if (object.workers !== undefined && object.workers !== null) {
      for (const e of object.workers) {
        message.workers.push(ListWorker.fromJSON(e));
      }
    }
    return message;
  },

  toJSON(message: ListWorkerResult): unknown {
    const obj: any = {};
    if (message.workers) {
      obj.workers = message.workers.map((e) =>
        e ? ListWorker.toJSON(e) : undefined
      );
    } else {
      obj.workers = [];
    }
    return obj;
  },

  fromPartial(object: DeepPartial<ListWorkerResult>): ListWorkerResult {
    const message = { ...baseListWorkerResult } as ListWorkerResult;
    message.workers = [];
    if (object.workers !== undefined && object.workers !== null) {
      for (const e of object.workers) {
        message.workers.push(ListWorker.fromPartial(e));
      }
    }
    return message;
  },
};

const baseListWorker: object = { hostname: "" };

export const ListWorker = {
  encode(
    message: ListWorker,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    if (message.uuid.length !== 0) {
      writer.uint32(10).bytes(message.uuid);
    }
    if (message.hostname !== "") {
      writer.uint32(18).string(message.hostname);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): ListWorker {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseListWorker } as ListWorker;
    message.uuid = new Uint8Array();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.uuid = reader.bytes();
          break;
        case 2:
          message.hostname = reader.string();
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): ListWorker {
    const message = { ...baseListWorker } as ListWorker;
    message.uuid = new Uint8Array();
    if (object.uuid !== undefined && object.uuid !== null) {
      message.uuid = bytesFromBase64(object.uuid);
    }
    if (object.hostname !== undefined && object.hostname !== null) {
      message.hostname = String(object.hostname);
    } else {
      message.hostname = "";
    }
    return message;
  },

  toJSON(message: ListWorker): unknown {
    const obj: any = {};
    message.uuid !== undefined &&
      (obj.uuid = base64FromBytes(
        message.uuid !== undefined ? message.uuid : new Uint8Array()
      ));
    message.hostname !== undefined && (obj.hostname = message.hostname);
    return obj;
  },

  fromPartial(object: DeepPartial<ListWorker>): ListWorker {
    const message = { ...baseListWorker } as ListWorker;
    if (object.uuid !== undefined && object.uuid !== null) {
      message.uuid = object.uuid;
    } else {
      message.uuid = new Uint8Array();
    }
    if (object.hostname !== undefined && object.hostname !== null) {
      message.hostname = object.hostname;
    } else {
      message.hostname = "";
    }
    return message;
  },
};

export interface Management {
  CreateTask(
    request: DeepPartial<CreateTaskRequest>,
    metadata?: grpc.Metadata
  ): Promise<CreateTaskResult>;
  ListTask(
    request: DeepPartial<ListTaskRequest>,
    metadata?: grpc.Metadata
  ): Promise<ListTaskResult>;
  CreateTarget(
    request: DeepPartial<CreateTargetRequest>,
    metadata?: grpc.Metadata
  ): Promise<CreateTargetResult>;
  ListTarget(
    request: DeepPartial<ListTargetRequest>,
    metadata?: grpc.Metadata
  ): Promise<ListTargetResult>;
  GetTarget(
    request: DeepPartial<GetTargetRequest>,
    metadata?: grpc.Metadata
  ): Promise<GetTargetResult>;
  ListTargetLsblk(
    request: DeepPartial<ListTargetLsblkRequest>,
    metadata?: grpc.Metadata
  ): Promise<ListTargetLsblkResult>;
  ListWorker(
    request: DeepPartial<ListWorkerRequest>,
    metadata?: grpc.Metadata
  ): Promise<ListWorkerResult>;
}

export class ManagementClientImpl implements Management {
  private readonly rpc: Rpc;

  constructor(rpc: Rpc) {
    this.rpc = rpc;
    this.CreateTask = this.CreateTask.bind(this);
    this.ListTask = this.ListTask.bind(this);
    this.CreateTarget = this.CreateTarget.bind(this);
    this.ListTarget = this.ListTarget.bind(this);
    this.GetTarget = this.GetTarget.bind(this);
    this.ListTargetLsblk = this.ListTargetLsblk.bind(this);
    this.ListWorker = this.ListWorker.bind(this);
  }

  CreateTask(
    request: DeepPartial<CreateTaskRequest>,
    metadata?: grpc.Metadata
  ): Promise<CreateTaskResult> {
    return this.rpc.unary(
      ManagementCreateTaskDesc,
      CreateTaskRequest.fromPartial(request),
      metadata
    );
  }

  ListTask(
    request: DeepPartial<ListTaskRequest>,
    metadata?: grpc.Metadata
  ): Promise<ListTaskResult> {
    return this.rpc.unary(
      ManagementListTaskDesc,
      ListTaskRequest.fromPartial(request),
      metadata
    );
  }

  CreateTarget(
    request: DeepPartial<CreateTargetRequest>,
    metadata?: grpc.Metadata
  ): Promise<CreateTargetResult> {
    return this.rpc.unary(
      ManagementCreateTargetDesc,
      CreateTargetRequest.fromPartial(request),
      metadata
    );
  }

  ListTarget(
    request: DeepPartial<ListTargetRequest>,
    metadata?: grpc.Metadata
  ): Promise<ListTargetResult> {
    return this.rpc.unary(
      ManagementListTargetDesc,
      ListTargetRequest.fromPartial(request),
      metadata
    );
  }

  GetTarget(
    request: DeepPartial<GetTargetRequest>,
    metadata?: grpc.Metadata
  ): Promise<GetTargetResult> {
    return this.rpc.unary(
      ManagementGetTargetDesc,
      GetTargetRequest.fromPartial(request),
      metadata
    );
  }

  ListTargetLsblk(
    request: DeepPartial<ListTargetLsblkRequest>,
    metadata?: grpc.Metadata
  ): Promise<ListTargetLsblkResult> {
    return this.rpc.unary(
      ManagementListTargetLsblkDesc,
      ListTargetLsblkRequest.fromPartial(request),
      metadata
    );
  }

  ListWorker(
    request: DeepPartial<ListWorkerRequest>,
    metadata?: grpc.Metadata
  ): Promise<ListWorkerResult> {
    return this.rpc.unary(
      ManagementListWorkerDesc,
      ListWorkerRequest.fromPartial(request),
      metadata
    );
  }
}

export const ManagementDesc = {
  serviceName: "Management",
};

export const ManagementCreateTaskDesc: UnaryMethodDefinitionish = {
  methodName: "CreateTask",
  service: ManagementDesc,
  requestStream: false,
  responseStream: false,
  requestType: {
    serializeBinary() {
      return CreateTaskRequest.encode(this).finish();
    },
  } as any,
  responseType: {
    deserializeBinary(data: Uint8Array) {
      return {
        ...CreateTaskResult.decode(data),
        toObject() {
          return this;
        },
      };
    },
  } as any,
};

export const ManagementListTaskDesc: UnaryMethodDefinitionish = {
  methodName: "ListTask",
  service: ManagementDesc,
  requestStream: false,
  responseStream: false,
  requestType: {
    serializeBinary() {
      return ListTaskRequest.encode(this).finish();
    },
  } as any,
  responseType: {
    deserializeBinary(data: Uint8Array) {
      return {
        ...ListTaskResult.decode(data),
        toObject() {
          return this;
        },
      };
    },
  } as any,
};

export const ManagementCreateTargetDesc: UnaryMethodDefinitionish = {
  methodName: "CreateTarget",
  service: ManagementDesc,
  requestStream: false,
  responseStream: false,
  requestType: {
    serializeBinary() {
      return CreateTargetRequest.encode(this).finish();
    },
  } as any,
  responseType: {
    deserializeBinary(data: Uint8Array) {
      return {
        ...CreateTargetResult.decode(data),
        toObject() {
          return this;
        },
      };
    },
  } as any,
};

export const ManagementListTargetDesc: UnaryMethodDefinitionish = {
  methodName: "ListTarget",
  service: ManagementDesc,
  requestStream: false,
  responseStream: false,
  requestType: {
    serializeBinary() {
      return ListTargetRequest.encode(this).finish();
    },
  } as any,
  responseType: {
    deserializeBinary(data: Uint8Array) {
      return {
        ...ListTargetResult.decode(data),
        toObject() {
          return this;
        },
      };
    },
  } as any,
};

export const ManagementGetTargetDesc: UnaryMethodDefinitionish = {
  methodName: "GetTarget",
  service: ManagementDesc,
  requestStream: false,
  responseStream: false,
  requestType: {
    serializeBinary() {
      return GetTargetRequest.encode(this).finish();
    },
  } as any,
  responseType: {
    deserializeBinary(data: Uint8Array) {
      return {
        ...GetTargetResult.decode(data),
        toObject() {
          return this;
        },
      };
    },
  } as any,
};

export const ManagementListTargetLsblkDesc: UnaryMethodDefinitionish = {
  methodName: "ListTargetLsblk",
  service: ManagementDesc,
  requestStream: false,
  responseStream: false,
  requestType: {
    serializeBinary() {
      return ListTargetLsblkRequest.encode(this).finish();
    },
  } as any,
  responseType: {
    deserializeBinary(data: Uint8Array) {
      return {
        ...ListTargetLsblkResult.decode(data),
        toObject() {
          return this;
        },
      };
    },
  } as any,
};

export const ManagementListWorkerDesc: UnaryMethodDefinitionish = {
  methodName: "ListWorker",
  service: ManagementDesc,
  requestStream: false,
  responseStream: false,
  requestType: {
    serializeBinary() {
      return ListWorkerRequest.encode(this).finish();
    },
  } as any,
  responseType: {
    deserializeBinary(data: Uint8Array) {
      return {
        ...ListWorkerResult.decode(data),
        toObject() {
          return this;
        },
      };
    },
  } as any,
};

interface UnaryMethodDefinitionishR
  extends grpc.UnaryMethodDefinition<any, any> {
  requestStream: any;
  responseStream: any;
}

type UnaryMethodDefinitionish = UnaryMethodDefinitionishR;

interface Rpc {
  unary<T extends UnaryMethodDefinitionish>(
    methodDesc: T,
    request: any,
    metadata: grpc.Metadata | undefined
  ): Promise<any>;
}

export class GrpcWebImpl {
  private host: string;
  private options: {
    transport?: grpc.TransportFactory;

    debug?: boolean;
    metadata?: grpc.Metadata;
  };

  constructor(
    host: string,
    options: {
      transport?: grpc.TransportFactory;

      debug?: boolean;
      metadata?: grpc.Metadata;
    }
  ) {
    this.host = host;
    this.options = options;
  }

  unary<T extends UnaryMethodDefinitionish>(
    methodDesc: T,
    _request: any,
    metadata: grpc.Metadata | undefined
  ): Promise<any> {
    const request = { ..._request, ...methodDesc.requestType };
    const maybeCombinedMetadata =
      metadata && this.options.metadata
        ? new BrowserHeaders({
            ...this.options?.metadata.headersMap,
            ...metadata?.headersMap,
          })
        : metadata || this.options.metadata;
    return new Promise((resolve, reject) => {
      grpc.unary(methodDesc, {
        request,
        host: this.host,
        metadata: maybeCombinedMetadata,
        transport: this.options.transport,
        debug: this.options.debug,
        onEnd: function (response) {
          if (response.status === grpc.Code.OK) {
            resolve(response.message);
          } else {
            const err = new Error(response.statusMessage) as any;
            err.code = response.status;
            err.metadata = response.trailers;
            reject(err);
          }
        },
      });
    });
  }
}

declare var self: any | undefined;
declare var window: any | undefined;
declare var global: any | undefined;
var globalThis: any = (() => {
  if (typeof globalThis !== "undefined") return globalThis;
  if (typeof self !== "undefined") return self;
  if (typeof window !== "undefined") return window;
  if (typeof global !== "undefined") return global;
  throw "Unable to locate global object";
})();

const atob: (b64: string) => string =
  globalThis.atob ||
  ((b64) => globalThis.Buffer.from(b64, "base64").toString("binary"));
function bytesFromBase64(b64: string): Uint8Array {
  const bin = atob(b64);
  const arr = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; ++i) {
    arr[i] = bin.charCodeAt(i);
  }
  return arr;
}

const btoa: (bin: string) => string =
  globalThis.btoa ||
  ((bin) => globalThis.Buffer.from(bin, "binary").toString("base64"));
function base64FromBytes(arr: Uint8Array): string {
  const bin: string[] = [];
  for (const byte of arr) {
    bin.push(String.fromCharCode(byte));
  }
  return btoa(bin.join(""));
}

type Builtin =
  | Date
  | Function
  | Uint8Array
  | string
  | number
  | boolean
  | undefined;
export type DeepPartial<T> = T extends Builtin
  ? T
  : T extends Array<infer U>
  ? Array<DeepPartial<U>>
  : T extends ReadonlyArray<infer U>
  ? ReadonlyArray<DeepPartial<U>>
  : T extends {}
  ? { [K in keyof T]?: DeepPartial<T[K]> }
  : Partial<T>;

function toTimestamp(date: Date): Timestamp {
  const seconds = date.getTime() / 1_000;
  const nanos = (date.getTime() % 1_000) * 1_000_000;
  return { seconds, nanos };
}

function fromTimestamp(t: Timestamp): Date {
  let millis = t.seconds * 1_000;
  millis += t.nanos / 1_000_000;
  return new Date(millis);
}

function fromJsonTimestamp(o: any): Date {
  if (o instanceof Date) {
    return o;
  } else if (typeof o === "string") {
    return new Date(o);
  } else {
    return fromTimestamp(Timestamp.fromJSON(o));
  }
}

function longToNumber(long: Long): number {
  if (long.gt(Number.MAX_SAFE_INTEGER)) {
    throw new globalThis.Error("Value is larger than Number.MAX_SAFE_INTEGER");
  }
  return long.toNumber();
}

if (_m0.util.Long !== Long) {
  _m0.util.Long = Long as any;
  _m0.configure();
}
