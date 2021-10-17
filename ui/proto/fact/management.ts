/* eslint-disable */
import { util, configure, Writer, Reader } from "protobufjs/minimal";
import * as Long from "long";
import { grpc } from "@improbable-eng/grpc-web";
import { BrowserHeaders } from "browser-headers";
import { Timestamp } from "../google/protobuf/timestamp";
import {
  TaskNone,
  TaskCollectDisk,
  TaskCollectMemory,
} from "../fact/controller";

export const protobufPackage = "";

export interface CreateTaskRequest {
  taskNone: TaskNone | undefined;
  taskCollectDisk: TaskCollectDisk | undefined;
  taskCollectMemory: TaskCollectMemory | undefined;
  target: Uint8Array;
}

export interface TargetSelector {}

export interface CreateTaskResult {
  uuid: Uint8Array;
}

export interface ListTaskRequest {}

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

export interface ListWorkerRequest {}

export interface ListWorkerResult {
  uuid: Uint8Array;
  hostname: string;
}

const baseCreateTaskRequest: object = {};

export const CreateTaskRequest = {
  encode(message: CreateTaskRequest, writer: Writer = Writer.create()): Writer {
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
    if (message.target.length !== 0) {
      writer.uint32(34).bytes(message.target);
    }
    return writer;
  },

  decode(input: Reader | Uint8Array, length?: number): CreateTaskRequest {
    const reader = input instanceof Reader ? input : new Reader(input);
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
    if (object.target !== undefined && object.target !== null) {
      message.target = object.target;
    } else {
      message.target = new Uint8Array();
    }
    return message;
  },
};

const baseTargetSelector: object = {};

export const TargetSelector = {
  encode(_: TargetSelector, writer: Writer = Writer.create()): Writer {
    return writer;
  },

  decode(input: Reader | Uint8Array, length?: number): TargetSelector {
    const reader = input instanceof Reader ? input : new Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseTargetSelector } as TargetSelector;
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

  fromJSON(_: any): TargetSelector {
    const message = { ...baseTargetSelector } as TargetSelector;
    return message;
  },

  toJSON(_: TargetSelector): unknown {
    const obj: any = {};
    return obj;
  },

  fromPartial(_: DeepPartial<TargetSelector>): TargetSelector {
    const message = { ...baseTargetSelector } as TargetSelector;
    return message;
  },
};

const baseCreateTaskResult: object = {};

export const CreateTaskResult = {
  encode(message: CreateTaskResult, writer: Writer = Writer.create()): Writer {
    if (message.uuid.length !== 0) {
      writer.uint32(10).bytes(message.uuid);
    }
    return writer;
  },

  decode(input: Reader | Uint8Array, length?: number): CreateTaskResult {
    const reader = input instanceof Reader ? input : new Reader(input);
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

const baseListTaskRequest: object = {};

export const ListTaskRequest = {
  encode(_: ListTaskRequest, writer: Writer = Writer.create()): Writer {
    return writer;
  },

  decode(input: Reader | Uint8Array, length?: number): ListTaskRequest {
    const reader = input instanceof Reader ? input : new Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseListTaskRequest } as ListTaskRequest;
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

  fromJSON(_: any): ListTaskRequest {
    const message = { ...baseListTaskRequest } as ListTaskRequest;
    return message;
  },

  toJSON(_: ListTaskRequest): unknown {
    const obj: any = {};
    return obj;
  },

  fromPartial(_: DeepPartial<ListTaskRequest>): ListTaskRequest {
    const message = { ...baseListTaskRequest } as ListTaskRequest;
    return message;
  },
};

const baseListTaskResult: object = {};

export const ListTaskResult = {
  encode(message: ListTaskResult, writer: Writer = Writer.create()): Writer {
    for (const v of message.tasks) {
      ListTask.encode(v!, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: Reader | Uint8Array, length?: number): ListTaskResult {
    const reader = input instanceof Reader ? input : new Reader(input);
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
  encode(message: ListTask, writer: Writer = Writer.create()): Writer {
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
    if (message.worker.length !== 0) {
      writer.uint32(82).bytes(message.worker);
    }
    return writer;
  },

  decode(input: Reader | Uint8Array, length?: number): ListTask {
    const reader = input instanceof Reader ? input : new Reader(input);
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
    if (object.worker !== undefined && object.worker !== null) {
      message.worker = object.worker;
    } else {
      message.worker = new Uint8Array();
    }
    return message;
  },
};

const baseListWorkerRequest: object = {};

export const ListWorkerRequest = {
  encode(_: ListWorkerRequest, writer: Writer = Writer.create()): Writer {
    return writer;
  },

  decode(input: Reader | Uint8Array, length?: number): ListWorkerRequest {
    const reader = input instanceof Reader ? input : new Reader(input);
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

const baseListWorkerResult: object = { hostname: "" };

export const ListWorkerResult = {
  encode(message: ListWorkerResult, writer: Writer = Writer.create()): Writer {
    if (message.uuid.length !== 0) {
      writer.uint32(10).bytes(message.uuid);
    }
    if (message.hostname !== "") {
      writer.uint32(18).string(message.hostname);
    }
    return writer;
  },

  decode(input: Reader | Uint8Array, length?: number): ListWorkerResult {
    const reader = input instanceof Reader ? input : new Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseListWorkerResult } as ListWorkerResult;
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

  fromJSON(object: any): ListWorkerResult {
    const message = { ...baseListWorkerResult } as ListWorkerResult;
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

  toJSON(message: ListWorkerResult): unknown {
    const obj: any = {};
    message.uuid !== undefined &&
      (obj.uuid = base64FromBytes(
        message.uuid !== undefined ? message.uuid : new Uint8Array()
      ));
    message.hostname !== undefined && (obj.hostname = message.hostname);
    return obj;
  },

  fromPartial(object: DeepPartial<ListWorkerResult>): ListWorkerResult {
    const message = { ...baseListWorkerResult } as ListWorkerResult;
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

// If you get a compile-error about 'Constructor<Long> and ... have no overlap',
// add '--ts_proto_opt=esModuleInterop=true' as a flag when calling 'protoc'.
if (util.Long !== Long) {
  util.Long = Long as any;
  configure();
}
