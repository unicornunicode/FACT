/* eslint-disable */
import Long from "long";
import _m0 from "protobufjs/minimal";

export const protobufPackage = "";

export interface Target {
  uuid: Uint8Array;
  ssh: SSHAccess | undefined;
}

export interface SSHAccess {
  host: string;
  user: string;
  port: number;
  privateKey: string;
  /** sudo */
  become: boolean;
  becomePassword: string;
}

export interface TaskNone {}

export interface TaskNoneResult {}

export interface TaskCollectDisk {
  selector: CollectDiskSelector | undefined;
}

export interface TaskCollectDiskResult {}

export interface CollectDiskSelector {
  group: CollectDiskSelector_Group;
}

export enum CollectDiskSelector_Group {
  ALL_DISKS = 0,
  ROOT_DISK = 1,
  ROOT_PARTITION = 2,
  UNRECOGNIZED = -1,
}

export function collectDiskSelector_GroupFromJSON(
  object: any
): CollectDiskSelector_Group {
  switch (object) {
    case 0:
    case "ALL_DISKS":
      return CollectDiskSelector_Group.ALL_DISKS;
    case 1:
    case "ROOT_DISK":
      return CollectDiskSelector_Group.ROOT_DISK;
    case 2:
    case "ROOT_PARTITION":
      return CollectDiskSelector_Group.ROOT_PARTITION;
    case -1:
    case "UNRECOGNIZED":
    default:
      return CollectDiskSelector_Group.UNRECOGNIZED;
  }
}

export function collectDiskSelector_GroupToJSON(
  object: CollectDiskSelector_Group
): string {
  switch (object) {
    case CollectDiskSelector_Group.ALL_DISKS:
      return "ALL_DISKS";
    case CollectDiskSelector_Group.ROOT_DISK:
      return "ROOT_DISK";
    case CollectDiskSelector_Group.ROOT_PARTITION:
      return "ROOT_PARTITION";
    default:
      return "UNKNOWN";
  }
}

export interface TaskCollectMemory {}

export interface TaskCollectMemoryResult {}

const baseTarget: object = {};

export const Target = {
  encode(
    message: Target,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    if (message.uuid.length !== 0) {
      writer.uint32(10).bytes(message.uuid);
    }
    if (message.ssh !== undefined) {
      SSHAccess.encode(message.ssh, writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): Target {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseTarget } as Target;
    message.uuid = new Uint8Array();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.uuid = reader.bytes();
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

  fromJSON(object: any): Target {
    const message = { ...baseTarget } as Target;
    message.uuid = new Uint8Array();
    if (object.uuid !== undefined && object.uuid !== null) {
      message.uuid = bytesFromBase64(object.uuid);
    }
    if (object.ssh !== undefined && object.ssh !== null) {
      message.ssh = SSHAccess.fromJSON(object.ssh);
    } else {
      message.ssh = undefined;
    }
    return message;
  },

  toJSON(message: Target): unknown {
    const obj: any = {};
    message.uuid !== undefined &&
      (obj.uuid = base64FromBytes(
        message.uuid !== undefined ? message.uuid : new Uint8Array()
      ));
    message.ssh !== undefined &&
      (obj.ssh = message.ssh ? SSHAccess.toJSON(message.ssh) : undefined);
    return obj;
  },

  fromPartial(object: DeepPartial<Target>): Target {
    const message = { ...baseTarget } as Target;
    if (object.uuid !== undefined && object.uuid !== null) {
      message.uuid = object.uuid;
    } else {
      message.uuid = new Uint8Array();
    }
    if (object.ssh !== undefined && object.ssh !== null) {
      message.ssh = SSHAccess.fromPartial(object.ssh);
    } else {
      message.ssh = undefined;
    }
    return message;
  },
};

const baseSSHAccess: object = {
  host: "",
  user: "",
  port: 0,
  privateKey: "",
  become: false,
  becomePassword: "",
};

export const SSHAccess = {
  encode(
    message: SSHAccess,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    if (message.host !== "") {
      writer.uint32(10).string(message.host);
    }
    if (message.user !== "") {
      writer.uint32(18).string(message.user);
    }
    if (message.port !== 0) {
      writer.uint32(24).uint32(message.port);
    }
    if (message.privateKey !== "") {
      writer.uint32(34).string(message.privateKey);
    }
    if (message.become === true) {
      writer.uint32(40).bool(message.become);
    }
    if (message.becomePassword !== "") {
      writer.uint32(50).string(message.becomePassword);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SSHAccess {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseSSHAccess } as SSHAccess;
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.host = reader.string();
          break;
        case 2:
          message.user = reader.string();
          break;
        case 3:
          message.port = reader.uint32();
          break;
        case 4:
          message.privateKey = reader.string();
          break;
        case 5:
          message.become = reader.bool();
          break;
        case 6:
          message.becomePassword = reader.string();
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): SSHAccess {
    const message = { ...baseSSHAccess } as SSHAccess;
    if (object.host !== undefined && object.host !== null) {
      message.host = String(object.host);
    } else {
      message.host = "";
    }
    if (object.user !== undefined && object.user !== null) {
      message.user = String(object.user);
    } else {
      message.user = "";
    }
    if (object.port !== undefined && object.port !== null) {
      message.port = Number(object.port);
    } else {
      message.port = 0;
    }
    if (object.privateKey !== undefined && object.privateKey !== null) {
      message.privateKey = String(object.privateKey);
    } else {
      message.privateKey = "";
    }
    if (object.become !== undefined && object.become !== null) {
      message.become = Boolean(object.become);
    } else {
      message.become = false;
    }
    if (object.becomePassword !== undefined && object.becomePassword !== null) {
      message.becomePassword = String(object.becomePassword);
    } else {
      message.becomePassword = "";
    }
    return message;
  },

  toJSON(message: SSHAccess): unknown {
    const obj: any = {};
    message.host !== undefined && (obj.host = message.host);
    message.user !== undefined && (obj.user = message.user);
    message.port !== undefined && (obj.port = message.port);
    message.privateKey !== undefined && (obj.privateKey = message.privateKey);
    message.become !== undefined && (obj.become = message.become);
    message.becomePassword !== undefined &&
      (obj.becomePassword = message.becomePassword);
    return obj;
  },

  fromPartial(object: DeepPartial<SSHAccess>): SSHAccess {
    const message = { ...baseSSHAccess } as SSHAccess;
    if (object.host !== undefined && object.host !== null) {
      message.host = object.host;
    } else {
      message.host = "";
    }
    if (object.user !== undefined && object.user !== null) {
      message.user = object.user;
    } else {
      message.user = "";
    }
    if (object.port !== undefined && object.port !== null) {
      message.port = object.port;
    } else {
      message.port = 0;
    }
    if (object.privateKey !== undefined && object.privateKey !== null) {
      message.privateKey = object.privateKey;
    } else {
      message.privateKey = "";
    }
    if (object.become !== undefined && object.become !== null) {
      message.become = object.become;
    } else {
      message.become = false;
    }
    if (object.becomePassword !== undefined && object.becomePassword !== null) {
      message.becomePassword = object.becomePassword;
    } else {
      message.becomePassword = "";
    }
    return message;
  },
};

const baseTaskNone: object = {};

export const TaskNone = {
  encode(_: TaskNone, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): TaskNone {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseTaskNone } as TaskNone;
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

  fromJSON(_: any): TaskNone {
    const message = { ...baseTaskNone } as TaskNone;
    return message;
  },

  toJSON(_: TaskNone): unknown {
    const obj: any = {};
    return obj;
  },

  fromPartial(_: DeepPartial<TaskNone>): TaskNone {
    const message = { ...baseTaskNone } as TaskNone;
    return message;
  },
};

const baseTaskNoneResult: object = {};

export const TaskNoneResult = {
  encode(
    _: TaskNoneResult,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): TaskNoneResult {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseTaskNoneResult } as TaskNoneResult;
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

  fromJSON(_: any): TaskNoneResult {
    const message = { ...baseTaskNoneResult } as TaskNoneResult;
    return message;
  },

  toJSON(_: TaskNoneResult): unknown {
    const obj: any = {};
    return obj;
  },

  fromPartial(_: DeepPartial<TaskNoneResult>): TaskNoneResult {
    const message = { ...baseTaskNoneResult } as TaskNoneResult;
    return message;
  },
};

const baseTaskCollectDisk: object = {};

export const TaskCollectDisk = {
  encode(
    message: TaskCollectDisk,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    if (message.selector !== undefined) {
      CollectDiskSelector.encode(
        message.selector,
        writer.uint32(18).fork()
      ).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): TaskCollectDisk {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseTaskCollectDisk } as TaskCollectDisk;
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          message.selector = CollectDiskSelector.decode(
            reader,
            reader.uint32()
          );
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): TaskCollectDisk {
    const message = { ...baseTaskCollectDisk } as TaskCollectDisk;
    if (object.selector !== undefined && object.selector !== null) {
      message.selector = CollectDiskSelector.fromJSON(object.selector);
    } else {
      message.selector = undefined;
    }
    return message;
  },

  toJSON(message: TaskCollectDisk): unknown {
    const obj: any = {};
    message.selector !== undefined &&
      (obj.selector = message.selector
        ? CollectDiskSelector.toJSON(message.selector)
        : undefined);
    return obj;
  },

  fromPartial(object: DeepPartial<TaskCollectDisk>): TaskCollectDisk {
    const message = { ...baseTaskCollectDisk } as TaskCollectDisk;
    if (object.selector !== undefined && object.selector !== null) {
      message.selector = CollectDiskSelector.fromPartial(object.selector);
    } else {
      message.selector = undefined;
    }
    return message;
  },
};

const baseTaskCollectDiskResult: object = {};

export const TaskCollectDiskResult = {
  encode(
    _: TaskCollectDiskResult,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    return writer;
  },

  decode(
    input: _m0.Reader | Uint8Array,
    length?: number
  ): TaskCollectDiskResult {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseTaskCollectDiskResult } as TaskCollectDiskResult;
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

  fromJSON(_: any): TaskCollectDiskResult {
    const message = { ...baseTaskCollectDiskResult } as TaskCollectDiskResult;
    return message;
  },

  toJSON(_: TaskCollectDiskResult): unknown {
    const obj: any = {};
    return obj;
  },

  fromPartial(_: DeepPartial<TaskCollectDiskResult>): TaskCollectDiskResult {
    const message = { ...baseTaskCollectDiskResult } as TaskCollectDiskResult;
    return message;
  },
};

const baseCollectDiskSelector: object = { group: 0 };

export const CollectDiskSelector = {
  encode(
    message: CollectDiskSelector,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    if (message.group !== 0) {
      writer.uint32(8).int32(message.group);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CollectDiskSelector {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseCollectDiskSelector } as CollectDiskSelector;
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.group = reader.int32() as any;
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): CollectDiskSelector {
    const message = { ...baseCollectDiskSelector } as CollectDiskSelector;
    if (object.group !== undefined && object.group !== null) {
      message.group = collectDiskSelector_GroupFromJSON(object.group);
    } else {
      message.group = 0;
    }
    return message;
  },

  toJSON(message: CollectDiskSelector): unknown {
    const obj: any = {};
    message.group !== undefined &&
      (obj.group = collectDiskSelector_GroupToJSON(message.group));
    return obj;
  },

  fromPartial(object: DeepPartial<CollectDiskSelector>): CollectDiskSelector {
    const message = { ...baseCollectDiskSelector } as CollectDiskSelector;
    if (object.group !== undefined && object.group !== null) {
      message.group = object.group;
    } else {
      message.group = 0;
    }
    return message;
  },
};

const baseTaskCollectMemory: object = {};

export const TaskCollectMemory = {
  encode(
    _: TaskCollectMemory,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): TaskCollectMemory {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseTaskCollectMemory } as TaskCollectMemory;
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

  fromJSON(_: any): TaskCollectMemory {
    const message = { ...baseTaskCollectMemory } as TaskCollectMemory;
    return message;
  },

  toJSON(_: TaskCollectMemory): unknown {
    const obj: any = {};
    return obj;
  },

  fromPartial(_: DeepPartial<TaskCollectMemory>): TaskCollectMemory {
    const message = { ...baseTaskCollectMemory } as TaskCollectMemory;
    return message;
  },
};

const baseTaskCollectMemoryResult: object = {};

export const TaskCollectMemoryResult = {
  encode(
    _: TaskCollectMemoryResult,
    writer: _m0.Writer = _m0.Writer.create()
  ): _m0.Writer {
    return writer;
  },

  decode(
    input: _m0.Reader | Uint8Array,
    length?: number
  ): TaskCollectMemoryResult {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = {
      ...baseTaskCollectMemoryResult,
    } as TaskCollectMemoryResult;
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

  fromJSON(_: any): TaskCollectMemoryResult {
    const message = {
      ...baseTaskCollectMemoryResult,
    } as TaskCollectMemoryResult;
    return message;
  },

  toJSON(_: TaskCollectMemoryResult): unknown {
    const obj: any = {};
    return obj;
  },

  fromPartial(
    _: DeepPartial<TaskCollectMemoryResult>
  ): TaskCollectMemoryResult {
    const message = {
      ...baseTaskCollectMemoryResult,
    } as TaskCollectMemoryResult;
    return message;
  },
};

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

if (_m0.util.Long !== Long) {
  _m0.util.Long = Long as any;
  _m0.configure();
}