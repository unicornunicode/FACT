/* eslint-disable */
import { util, configure, Writer, Reader } from 'protobufjs/minimal';
import * as Long from 'long';
import { grpc } from '@improbable-eng/grpc-web';
import { Observable } from 'rxjs';
import { BrowserHeaders } from 'browser-headers';
import { share } from 'rxjs/operators';

export const protobufPackage = '';

export interface SessionResults {
workerRegistration: WorkerRegistration | undefined,
workerTaskResult: WorkerTaskResult | undefined,
}

export interface SessionEvents {
workerAcceptance: WorkerAcceptance | undefined,
workerTask: WorkerTask | undefined,
}

export interface WorkerRegistration {
previousUuid?: Uint8Array | undefined,
hostname: string,
}

export interface WorkerAcceptance {
uuid: Uint8Array,
}

export interface WorkerTask {
uuid: Uint8Array,
target?: Target | undefined,
taskNone: TaskNone | undefined,
taskCollectDisk: TaskCollectDisk | undefined,
taskCollectMemory: TaskCollectMemory | undefined,
}

export interface Target {
uuid: Uint8Array,
ssh: SSHAccess | undefined,
}

export interface SSHAccess {
host: string,
user: string,
port: number,
privateKey: string,
/** sudo */
become: boolean,
becomePassword: string,
}

export interface WorkerTaskResult {
uuid: Uint8Array,
taskNone: TaskNoneResult | undefined,
taskCollectDisk: TaskCollectDiskResult | undefined,
taskCollectMemory: TaskCollectMemoryResult | undefined,
}

export interface TaskNone {
}

export interface TaskNoneResult {
}

export interface TaskCollectDisk {
selector: CollectDiskSelector | undefined,
}

export interface TaskCollectDiskResult {
}

export interface CollectDiskSelector {
group: CollectDiskSelector_Group,
}

export enum CollectDiskSelector_Group {
ALL_DISKS = 0,
ROOT_DISK = 1,
ROOT_PARTITION = 2,
UNRECOGNIZED = -1,
}

export function collectDiskSelector_GroupFromJSON(object: any): CollectDiskSelector_Group {
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

export function collectDiskSelector_GroupToJSON(object: CollectDiskSelector_Group): string {
switch (object) {
case CollectDiskSelector_Group.ALL_DISKS: return "ALL_DISKS";
case CollectDiskSelector_Group.ROOT_DISK: return "ROOT_DISK";
case CollectDiskSelector_Group.ROOT_PARTITION: return "ROOT_PARTITION";
default: return "UNKNOWN";
}
}

export interface TaskCollectMemory {
}

export interface TaskCollectMemoryResult {
}

const baseSessionResults: object = {  };

export const SessionResults = {
            encode(
      message: SessionResults,
      writer: Writer = Writer.create(),
    ): Writer {
if (message.workerRegistration !== undefined) {
          WorkerRegistration.encode(message.workerRegistration, writer.uint32(10).fork()).ldelim();
        }
if (message.workerTaskResult !== undefined) {
          WorkerTaskResult.encode(message.workerTaskResult, writer.uint32(18).fork()).ldelim();
        }
return writer;
},

decode(
      input: Reader | Uint8Array,
      length?: number,
    ): SessionResults {
      const reader = input instanceof Reader ? input : new Reader(input);
      let end = length === undefined ? reader.len : reader.pos + length;
      const message = { ...baseSessionResults } as SessionResults;
while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
case 1:
message.workerRegistration = WorkerRegistration.decode(reader, reader.uint32());
break;
case 2:
message.workerTaskResult = WorkerTaskResult.decode(reader, reader.uint32());
break;
default:
      reader.skipType(tag & 7);
      break;
}
}
return message;
},

fromJSON(object: any): SessionResults {
      const message = { ...baseSessionResults } as SessionResults;
if (object.workerRegistration !== undefined && object.workerRegistration !== null) {
message.workerRegistration = WorkerRegistration.fromJSON(object.workerRegistration);
} else {
message.workerRegistration = undefined;
}
if (object.workerTaskResult !== undefined && object.workerTaskResult !== null) {
message.workerTaskResult = WorkerTaskResult.fromJSON(object.workerTaskResult);
} else {
message.workerTaskResult = undefined;
}
return message
},

toJSON(message: SessionResults): unknown {
      const obj: any = {};
message.workerRegistration !== undefined && (obj.workerRegistration = message.workerRegistration ? WorkerRegistration.toJSON(message.workerRegistration) : undefined);
message.workerTaskResult !== undefined && (obj.workerTaskResult = message.workerTaskResult ? WorkerTaskResult.toJSON(message.workerTaskResult) : undefined);
return obj;
},

fromPartial(object: DeepPartial<SessionResults>): SessionResults {
      const message = { ...baseSessionResults } as SessionResults;
if (object.workerRegistration !== undefined && object.workerRegistration !== null) {
message.workerRegistration = WorkerRegistration.fromPartial(object.workerRegistration);
} else {
message.workerRegistration = undefined
}
if (object.workerTaskResult !== undefined && object.workerTaskResult !== null) {
message.workerTaskResult = WorkerTaskResult.fromPartial(object.workerTaskResult);
} else {
message.workerTaskResult = undefined
}
return message;
}
          };

const baseSessionEvents: object = {  };

export const SessionEvents = {
            encode(
      message: SessionEvents,
      writer: Writer = Writer.create(),
    ): Writer {
if (message.workerAcceptance !== undefined) {
          WorkerAcceptance.encode(message.workerAcceptance, writer.uint32(10).fork()).ldelim();
        }
if (message.workerTask !== undefined) {
          WorkerTask.encode(message.workerTask, writer.uint32(18).fork()).ldelim();
        }
return writer;
},

decode(
      input: Reader | Uint8Array,
      length?: number,
    ): SessionEvents {
      const reader = input instanceof Reader ? input : new Reader(input);
      let end = length === undefined ? reader.len : reader.pos + length;
      const message = { ...baseSessionEvents } as SessionEvents;
while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
case 1:
message.workerAcceptance = WorkerAcceptance.decode(reader, reader.uint32());
break;
case 2:
message.workerTask = WorkerTask.decode(reader, reader.uint32());
break;
default:
      reader.skipType(tag & 7);
      break;
}
}
return message;
},

fromJSON(object: any): SessionEvents {
      const message = { ...baseSessionEvents } as SessionEvents;
if (object.workerAcceptance !== undefined && object.workerAcceptance !== null) {
message.workerAcceptance = WorkerAcceptance.fromJSON(object.workerAcceptance);
} else {
message.workerAcceptance = undefined;
}
if (object.workerTask !== undefined && object.workerTask !== null) {
message.workerTask = WorkerTask.fromJSON(object.workerTask);
} else {
message.workerTask = undefined;
}
return message
},

toJSON(message: SessionEvents): unknown {
      const obj: any = {};
message.workerAcceptance !== undefined && (obj.workerAcceptance = message.workerAcceptance ? WorkerAcceptance.toJSON(message.workerAcceptance) : undefined);
message.workerTask !== undefined && (obj.workerTask = message.workerTask ? WorkerTask.toJSON(message.workerTask) : undefined);
return obj;
},

fromPartial(object: DeepPartial<SessionEvents>): SessionEvents {
      const message = { ...baseSessionEvents } as SessionEvents;
if (object.workerAcceptance !== undefined && object.workerAcceptance !== null) {
message.workerAcceptance = WorkerAcceptance.fromPartial(object.workerAcceptance);
} else {
message.workerAcceptance = undefined
}
if (object.workerTask !== undefined && object.workerTask !== null) {
message.workerTask = WorkerTask.fromPartial(object.workerTask);
} else {
message.workerTask = undefined
}
return message;
}
          };

const baseWorkerRegistration: object = { hostname: "" };

export const WorkerRegistration = {
            encode(
      message: WorkerRegistration,
      writer: Writer = Writer.create(),
    ): Writer {
if (message.previousUuid !== undefined) {
          writer.uint32(10).bytes(message.previousUuid);
        }
if (message.hostname !== "") {
          writer.uint32(18).string(message.hostname);
        }
return writer;
},

decode(
      input: Reader | Uint8Array,
      length?: number,
    ): WorkerRegistration {
      const reader = input instanceof Reader ? input : new Reader(input);
      let end = length === undefined ? reader.len : reader.pos + length;
      const message = { ...baseWorkerRegistration } as WorkerRegistration;
while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
case 1:
message.previousUuid = reader.bytes();
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

fromJSON(object: any): WorkerRegistration {
      const message = { ...baseWorkerRegistration } as WorkerRegistration;
if (object.previousUuid !== undefined && object.previousUuid !== null) {
message.previousUuid = bytesFromBase64(object.previousUuid);
}
if (object.hostname !== undefined && object.hostname !== null) {
message.hostname = String(object.hostname);
} else {
message.hostname = "";
}
return message
},

toJSON(message: WorkerRegistration): unknown {
      const obj: any = {};
message.previousUuid !== undefined && (obj.previousUuid = message.previousUuid !== undefined ? base64FromBytes(message.previousUuid) : undefined);
message.hostname !== undefined && (obj.hostname = message.hostname);
return obj;
},

fromPartial(object: DeepPartial<WorkerRegistration>): WorkerRegistration {
      const message = { ...baseWorkerRegistration } as WorkerRegistration;
if (object.previousUuid !== undefined && object.previousUuid !== null) {
message.previousUuid = object.previousUuid;
} else {
message.previousUuid = undefined
}
if (object.hostname !== undefined && object.hostname !== null) {
message.hostname = object.hostname;
} else {
message.hostname = ""
}
return message;
}
          };

const baseWorkerAcceptance: object = {  };

export const WorkerAcceptance = {
            encode(
      message: WorkerAcceptance,
      writer: Writer = Writer.create(),
    ): Writer {
if (message.uuid.length !== 0) {
          writer.uint32(10).bytes(message.uuid);
        }
return writer;
},

decode(
      input: Reader | Uint8Array,
      length?: number,
    ): WorkerAcceptance {
      const reader = input instanceof Reader ? input : new Reader(input);
      let end = length === undefined ? reader.len : reader.pos + length;
      const message = { ...baseWorkerAcceptance } as WorkerAcceptance;
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

fromJSON(object: any): WorkerAcceptance {
      const message = { ...baseWorkerAcceptance } as WorkerAcceptance;
message.uuid = new Uint8Array();
if (object.uuid !== undefined && object.uuid !== null) {
message.uuid = bytesFromBase64(object.uuid);
}
return message
},

toJSON(message: WorkerAcceptance): unknown {
      const obj: any = {};
message.uuid !== undefined && (obj.uuid = base64FromBytes(message.uuid !== undefined ? message.uuid : new Uint8Array()));
return obj;
},

fromPartial(object: DeepPartial<WorkerAcceptance>): WorkerAcceptance {
      const message = { ...baseWorkerAcceptance } as WorkerAcceptance;
if (object.uuid !== undefined && object.uuid !== null) {
message.uuid = object.uuid;
} else {
message.uuid = new Uint8Array()
}
return message;
}
          };

const baseWorkerTask: object = {  };

export const WorkerTask = {
            encode(
      message: WorkerTask,
      writer: Writer = Writer.create(),
    ): Writer {
if (message.uuid.length !== 0) {
          writer.uint32(10).bytes(message.uuid);
        }
if (message.target !== undefined) {
          Target.encode(message.target, writer.uint32(18).fork()).ldelim();
        }
if (message.taskNone !== undefined) {
          TaskNone.encode(message.taskNone, writer.uint32(26).fork()).ldelim();
        }
if (message.taskCollectDisk !== undefined) {
          TaskCollectDisk.encode(message.taskCollectDisk, writer.uint32(34).fork()).ldelim();
        }
if (message.taskCollectMemory !== undefined) {
          TaskCollectMemory.encode(message.taskCollectMemory, writer.uint32(42).fork()).ldelim();
        }
return writer;
},

decode(
      input: Reader | Uint8Array,
      length?: number,
    ): WorkerTask {
      const reader = input instanceof Reader ? input : new Reader(input);
      let end = length === undefined ? reader.len : reader.pos + length;
      const message = { ...baseWorkerTask } as WorkerTask;
message.uuid = new Uint8Array();
while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
case 1:
message.uuid = reader.bytes();
break;
case 2:
message.target = Target.decode(reader, reader.uint32());
break;
case 3:
message.taskNone = TaskNone.decode(reader, reader.uint32());
break;
case 4:
message.taskCollectDisk = TaskCollectDisk.decode(reader, reader.uint32());
break;
case 5:
message.taskCollectMemory = TaskCollectMemory.decode(reader, reader.uint32());
break;
default:
      reader.skipType(tag & 7);
      break;
}
}
return message;
},

fromJSON(object: any): WorkerTask {
      const message = { ...baseWorkerTask } as WorkerTask;
message.uuid = new Uint8Array();
if (object.uuid !== undefined && object.uuid !== null) {
message.uuid = bytesFromBase64(object.uuid);
}
if (object.target !== undefined && object.target !== null) {
message.target = Target.fromJSON(object.target);
} else {
message.target = undefined;
}
if (object.taskNone !== undefined && object.taskNone !== null) {
message.taskNone = TaskNone.fromJSON(object.taskNone);
} else {
message.taskNone = undefined;
}
if (object.taskCollectDisk !== undefined && object.taskCollectDisk !== null) {
message.taskCollectDisk = TaskCollectDisk.fromJSON(object.taskCollectDisk);
} else {
message.taskCollectDisk = undefined;
}
if (object.taskCollectMemory !== undefined && object.taskCollectMemory !== null) {
message.taskCollectMemory = TaskCollectMemory.fromJSON(object.taskCollectMemory);
} else {
message.taskCollectMemory = undefined;
}
return message
},

toJSON(message: WorkerTask): unknown {
      const obj: any = {};
message.uuid !== undefined && (obj.uuid = base64FromBytes(message.uuid !== undefined ? message.uuid : new Uint8Array()));
message.target !== undefined && (obj.target = message.target ? Target.toJSON(message.target) : undefined);
message.taskNone !== undefined && (obj.taskNone = message.taskNone ? TaskNone.toJSON(message.taskNone) : undefined);
message.taskCollectDisk !== undefined && (obj.taskCollectDisk = message.taskCollectDisk ? TaskCollectDisk.toJSON(message.taskCollectDisk) : undefined);
message.taskCollectMemory !== undefined && (obj.taskCollectMemory = message.taskCollectMemory ? TaskCollectMemory.toJSON(message.taskCollectMemory) : undefined);
return obj;
},

fromPartial(object: DeepPartial<WorkerTask>): WorkerTask {
      const message = { ...baseWorkerTask } as WorkerTask;
if (object.uuid !== undefined && object.uuid !== null) {
message.uuid = object.uuid;
} else {
message.uuid = new Uint8Array()
}
if (object.target !== undefined && object.target !== null) {
message.target = Target.fromPartial(object.target);
} else {
message.target = undefined
}
if (object.taskNone !== undefined && object.taskNone !== null) {
message.taskNone = TaskNone.fromPartial(object.taskNone);
} else {
message.taskNone = undefined
}
if (object.taskCollectDisk !== undefined && object.taskCollectDisk !== null) {
message.taskCollectDisk = TaskCollectDisk.fromPartial(object.taskCollectDisk);
} else {
message.taskCollectDisk = undefined
}
if (object.taskCollectMemory !== undefined && object.taskCollectMemory !== null) {
message.taskCollectMemory = TaskCollectMemory.fromPartial(object.taskCollectMemory);
} else {
message.taskCollectMemory = undefined
}
return message;
}
          };

const baseTarget: object = {  };

export const Target = {
            encode(
      message: Target,
      writer: Writer = Writer.create(),
    ): Writer {
if (message.uuid.length !== 0) {
          writer.uint32(10).bytes(message.uuid);
        }
if (message.ssh !== undefined) {
          SSHAccess.encode(message.ssh, writer.uint32(18).fork()).ldelim();
        }
return writer;
},

decode(
      input: Reader | Uint8Array,
      length?: number,
    ): Target {
      const reader = input instanceof Reader ? input : new Reader(input);
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
return message
},

toJSON(message: Target): unknown {
      const obj: any = {};
message.uuid !== undefined && (obj.uuid = base64FromBytes(message.uuid !== undefined ? message.uuid : new Uint8Array()));
message.ssh !== undefined && (obj.ssh = message.ssh ? SSHAccess.toJSON(message.ssh) : undefined);
return obj;
},

fromPartial(object: DeepPartial<Target>): Target {
      const message = { ...baseTarget } as Target;
if (object.uuid !== undefined && object.uuid !== null) {
message.uuid = object.uuid;
} else {
message.uuid = new Uint8Array()
}
if (object.ssh !== undefined && object.ssh !== null) {
message.ssh = SSHAccess.fromPartial(object.ssh);
} else {
message.ssh = undefined
}
return message;
}
          };

const baseSSHAccess: object = { host: "",user: "",port: 0,privateKey: "",become: false,becomePassword: "" };

export const SSHAccess = {
            encode(
      message: SSHAccess,
      writer: Writer = Writer.create(),
    ): Writer {
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

decode(
      input: Reader | Uint8Array,
      length?: number,
    ): SSHAccess {
      const reader = input instanceof Reader ? input : new Reader(input);
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
return message
},

toJSON(message: SSHAccess): unknown {
      const obj: any = {};
message.host !== undefined && (obj.host = message.host);
message.user !== undefined && (obj.user = message.user);
message.port !== undefined && (obj.port = message.port);
message.privateKey !== undefined && (obj.privateKey = message.privateKey);
message.become !== undefined && (obj.become = message.become);
message.becomePassword !== undefined && (obj.becomePassword = message.becomePassword);
return obj;
},

fromPartial(object: DeepPartial<SSHAccess>): SSHAccess {
      const message = { ...baseSSHAccess } as SSHAccess;
if (object.host !== undefined && object.host !== null) {
message.host = object.host;
} else {
message.host = ""
}
if (object.user !== undefined && object.user !== null) {
message.user = object.user;
} else {
message.user = ""
}
if (object.port !== undefined && object.port !== null) {
message.port = object.port;
} else {
message.port = 0
}
if (object.privateKey !== undefined && object.privateKey !== null) {
message.privateKey = object.privateKey;
} else {
message.privateKey = ""
}
if (object.become !== undefined && object.become !== null) {
message.become = object.become;
} else {
message.become = false
}
if (object.becomePassword !== undefined && object.becomePassword !== null) {
message.becomePassword = object.becomePassword;
} else {
message.becomePassword = ""
}
return message;
}
          };

const baseWorkerTaskResult: object = {  };

export const WorkerTaskResult = {
            encode(
      message: WorkerTaskResult,
      writer: Writer = Writer.create(),
    ): Writer {
if (message.uuid.length !== 0) {
          writer.uint32(10).bytes(message.uuid);
        }
if (message.taskNone !== undefined) {
          TaskNoneResult.encode(message.taskNone, writer.uint32(18).fork()).ldelim();
        }
if (message.taskCollectDisk !== undefined) {
          TaskCollectDiskResult.encode(message.taskCollectDisk, writer.uint32(26).fork()).ldelim();
        }
if (message.taskCollectMemory !== undefined) {
          TaskCollectMemoryResult.encode(message.taskCollectMemory, writer.uint32(34).fork()).ldelim();
        }
return writer;
},

decode(
      input: Reader | Uint8Array,
      length?: number,
    ): WorkerTaskResult {
      const reader = input instanceof Reader ? input : new Reader(input);
      let end = length === undefined ? reader.len : reader.pos + length;
      const message = { ...baseWorkerTaskResult } as WorkerTaskResult;
message.uuid = new Uint8Array();
while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
case 1:
message.uuid = reader.bytes();
break;
case 2:
message.taskNone = TaskNoneResult.decode(reader, reader.uint32());
break;
case 3:
message.taskCollectDisk = TaskCollectDiskResult.decode(reader, reader.uint32());
break;
case 4:
message.taskCollectMemory = TaskCollectMemoryResult.decode(reader, reader.uint32());
break;
default:
      reader.skipType(tag & 7);
      break;
}
}
return message;
},

fromJSON(object: any): WorkerTaskResult {
      const message = { ...baseWorkerTaskResult } as WorkerTaskResult;
message.uuid = new Uint8Array();
if (object.uuid !== undefined && object.uuid !== null) {
message.uuid = bytesFromBase64(object.uuid);
}
if (object.taskNone !== undefined && object.taskNone !== null) {
message.taskNone = TaskNoneResult.fromJSON(object.taskNone);
} else {
message.taskNone = undefined;
}
if (object.taskCollectDisk !== undefined && object.taskCollectDisk !== null) {
message.taskCollectDisk = TaskCollectDiskResult.fromJSON(object.taskCollectDisk);
} else {
message.taskCollectDisk = undefined;
}
if (object.taskCollectMemory !== undefined && object.taskCollectMemory !== null) {
message.taskCollectMemory = TaskCollectMemoryResult.fromJSON(object.taskCollectMemory);
} else {
message.taskCollectMemory = undefined;
}
return message
},

toJSON(message: WorkerTaskResult): unknown {
      const obj: any = {};
message.uuid !== undefined && (obj.uuid = base64FromBytes(message.uuid !== undefined ? message.uuid : new Uint8Array()));
message.taskNone !== undefined && (obj.taskNone = message.taskNone ? TaskNoneResult.toJSON(message.taskNone) : undefined);
message.taskCollectDisk !== undefined && (obj.taskCollectDisk = message.taskCollectDisk ? TaskCollectDiskResult.toJSON(message.taskCollectDisk) : undefined);
message.taskCollectMemory !== undefined && (obj.taskCollectMemory = message.taskCollectMemory ? TaskCollectMemoryResult.toJSON(message.taskCollectMemory) : undefined);
return obj;
},

fromPartial(object: DeepPartial<WorkerTaskResult>): WorkerTaskResult {
      const message = { ...baseWorkerTaskResult } as WorkerTaskResult;
if (object.uuid !== undefined && object.uuid !== null) {
message.uuid = object.uuid;
} else {
message.uuid = new Uint8Array()
}
if (object.taskNone !== undefined && object.taskNone !== null) {
message.taskNone = TaskNoneResult.fromPartial(object.taskNone);
} else {
message.taskNone = undefined
}
if (object.taskCollectDisk !== undefined && object.taskCollectDisk !== null) {
message.taskCollectDisk = TaskCollectDiskResult.fromPartial(object.taskCollectDisk);
} else {
message.taskCollectDisk = undefined
}
if (object.taskCollectMemory !== undefined && object.taskCollectMemory !== null) {
message.taskCollectMemory = TaskCollectMemoryResult.fromPartial(object.taskCollectMemory);
} else {
message.taskCollectMemory = undefined
}
return message;
}
          };

const baseTaskNone: object = {  };

export const TaskNone = {
            encode(
      _: TaskNone,
      writer: Writer = Writer.create(),
    ): Writer {
return writer;
},

decode(
      input: Reader | Uint8Array,
      length?: number,
    ): TaskNone {
      const reader = input instanceof Reader ? input : new Reader(input);
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
return message
},

toJSON(_: TaskNone): unknown {
      const obj: any = {};
return obj;
},

fromPartial(_: DeepPartial<TaskNone>): TaskNone {
      const message = { ...baseTaskNone } as TaskNone;
return message;
}
          };

const baseTaskNoneResult: object = {  };

export const TaskNoneResult = {
            encode(
      _: TaskNoneResult,
      writer: Writer = Writer.create(),
    ): Writer {
return writer;
},

decode(
      input: Reader | Uint8Array,
      length?: number,
    ): TaskNoneResult {
      const reader = input instanceof Reader ? input : new Reader(input);
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
return message
},

toJSON(_: TaskNoneResult): unknown {
      const obj: any = {};
return obj;
},

fromPartial(_: DeepPartial<TaskNoneResult>): TaskNoneResult {
      const message = { ...baseTaskNoneResult } as TaskNoneResult;
return message;
}
          };

const baseTaskCollectDisk: object = {  };

export const TaskCollectDisk = {
            encode(
      message: TaskCollectDisk,
      writer: Writer = Writer.create(),
    ): Writer {
if (message.selector !== undefined) {
          CollectDiskSelector.encode(message.selector, writer.uint32(18).fork()).ldelim();
        }
return writer;
},

decode(
      input: Reader | Uint8Array,
      length?: number,
    ): TaskCollectDisk {
      const reader = input instanceof Reader ? input : new Reader(input);
      let end = length === undefined ? reader.len : reader.pos + length;
      const message = { ...baseTaskCollectDisk } as TaskCollectDisk;
while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
case 2:
message.selector = CollectDiskSelector.decode(reader, reader.uint32());
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
return message
},

toJSON(message: TaskCollectDisk): unknown {
      const obj: any = {};
message.selector !== undefined && (obj.selector = message.selector ? CollectDiskSelector.toJSON(message.selector) : undefined);
return obj;
},

fromPartial(object: DeepPartial<TaskCollectDisk>): TaskCollectDisk {
      const message = { ...baseTaskCollectDisk } as TaskCollectDisk;
if (object.selector !== undefined && object.selector !== null) {
message.selector = CollectDiskSelector.fromPartial(object.selector);
} else {
message.selector = undefined
}
return message;
}
          };

const baseTaskCollectDiskResult: object = {  };

export const TaskCollectDiskResult = {
            encode(
      _: TaskCollectDiskResult,
      writer: Writer = Writer.create(),
    ): Writer {
return writer;
},

decode(
      input: Reader | Uint8Array,
      length?: number,
    ): TaskCollectDiskResult {
      const reader = input instanceof Reader ? input : new Reader(input);
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
return message
},

toJSON(_: TaskCollectDiskResult): unknown {
      const obj: any = {};
return obj;
},

fromPartial(_: DeepPartial<TaskCollectDiskResult>): TaskCollectDiskResult {
      const message = { ...baseTaskCollectDiskResult } as TaskCollectDiskResult;
return message;
}
          };

const baseCollectDiskSelector: object = { group: 0 };

export const CollectDiskSelector = {
            encode(
      message: CollectDiskSelector,
      writer: Writer = Writer.create(),
    ): Writer {
if (message.group !== 0) {
          writer.uint32(8).int32(message.group);
        }
return writer;
},

decode(
      input: Reader | Uint8Array,
      length?: number,
    ): CollectDiskSelector {
      const reader = input instanceof Reader ? input : new Reader(input);
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
return message
},

toJSON(message: CollectDiskSelector): unknown {
      const obj: any = {};
message.group !== undefined && (obj.group = collectDiskSelector_GroupToJSON(message.group));
return obj;
},

fromPartial(object: DeepPartial<CollectDiskSelector>): CollectDiskSelector {
      const message = { ...baseCollectDiskSelector } as CollectDiskSelector;
if (object.group !== undefined && object.group !== null) {
message.group = object.group;
} else {
message.group = 0
}
return message;
}
          };

const baseTaskCollectMemory: object = {  };

export const TaskCollectMemory = {
            encode(
      _: TaskCollectMemory,
      writer: Writer = Writer.create(),
    ): Writer {
return writer;
},

decode(
      input: Reader | Uint8Array,
      length?: number,
    ): TaskCollectMemory {
      const reader = input instanceof Reader ? input : new Reader(input);
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
return message
},

toJSON(_: TaskCollectMemory): unknown {
      const obj: any = {};
return obj;
},

fromPartial(_: DeepPartial<TaskCollectMemory>): TaskCollectMemory {
      const message = { ...baseTaskCollectMemory } as TaskCollectMemory;
return message;
}
          };

const baseTaskCollectMemoryResult: object = {  };

export const TaskCollectMemoryResult = {
            encode(
      _: TaskCollectMemoryResult,
      writer: Writer = Writer.create(),
    ): Writer {
return writer;
},

decode(
      input: Reader | Uint8Array,
      length?: number,
    ): TaskCollectMemoryResult {
      const reader = input instanceof Reader ? input : new Reader(input);
      let end = length === undefined ? reader.len : reader.pos + length;
      const message = { ...baseTaskCollectMemoryResult } as TaskCollectMemoryResult;
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
      const message = { ...baseTaskCollectMemoryResult } as TaskCollectMemoryResult;
return message
},

toJSON(_: TaskCollectMemoryResult): unknown {
      const obj: any = {};
return obj;
},

fromPartial(_: DeepPartial<TaskCollectMemoryResult>): TaskCollectMemoryResult {
      const message = { ...baseTaskCollectMemoryResult } as TaskCollectMemoryResult;
return message;
}
          };

export interface WorkerTasks {
Session(request: DeepPartial<Observable<SessionResults>>,metadata?: grpc.Metadata): Observable<SessionEvents>;
}

export class WorkerTasksClientImpl implements WorkerTasks {
  
    private readonly rpc: Rpc;
    
    constructor(rpc: Rpc) {
  this.rpc = rpc;this.Session = this.Session.bind(this);}

    Session(
      request: DeepPartial<Observable<SessionResults>>,
      metadata?: grpc.Metadata,
    ): Observable<SessionEvents> {
      return this.rpc.invoke(
        WorkerTasksSessionDesc,
        Observable<SessionResults>.fromPartial(request),
        metadata,
      );
    }
  }

export const WorkerTasksDesc = {
      serviceName: "WorkerTasks",
    };

export const WorkerTasksSessionDesc: UnaryMethodDefinitionish = {
      methodName: "Session",
      service: WorkerTasksDesc,
      requestStream: false,
      responseStream: true,
      requestType: {
    serializeBinary() {
      return Observable<SessionResults>.encode(this).finish();
    },
  } as any,
      responseType: {
    deserializeBinary(data: Uint8Array) {
      return { ...SessionEvents.decode(data), toObject() { return this; } };
    }
  } as any,
    };

interface UnaryMethodDefinitionishR extends grpc.UnaryMethodDefinition<any, any> { requestStream: any; responseStream: any; }

type UnaryMethodDefinitionish = UnaryMethodDefinitionishR;

interface Rpc {
unary<T extends UnaryMethodDefinitionish>(
      methodDesc: T,
      request: any,
      metadata: grpc.Metadata | undefined,
    ): Promise<any>;
invoke<T extends UnaryMethodDefinitionish>(
        methodDesc: T,
        request: any,
        metadata: grpc.Metadata | undefined,
      ): Observable<any>;
}

export class GrpcWebImpl {
      private host: string;
      private options: 
    {
      transport?: grpc.TransportFactory,
      streamingTransport?: grpc.TransportFactory,
      debug?: boolean,
      metadata?: grpc.Metadata,
    }
  ;
      
      constructor(host: string, options: 
    {
      transport?: grpc.TransportFactory,
      streamingTransport?: grpc.TransportFactory,
      debug?: boolean,
      metadata?: grpc.Metadata,
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
          ? new BrowserHeaders({ ...this.options?.metadata.headersMap, ...metadata?.headersMap })
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
  
    invoke<T extends UnaryMethodDefinitionish>(
      methodDesc: T,
      _request: any,
      metadata: grpc.Metadata | undefined
    ): Observable<any> {
      // Status Response Codes (https://developers.google.com/maps-booking/reference/grpc-api/status_codes)
      const upStreamCodes = [2, 4, 8, 9, 10, 13, 14, 15]; 
      const DEFAULT_TIMEOUT_TIME: number = 3_000;
      const request = { ..._request, ...methodDesc.requestType };
      const maybeCombinedMetadata =
      metadata && this.options.metadata
        ? new BrowserHeaders({ ...this.options?.metadata.headersMap, ...metadata?.headersMap })
        : metadata || this.options.metadata;
      return new Observable(observer => {
        const upStream = (() => {
          const client = grpc.invoke(methodDesc, {
            host: this.host,
            request,
            transport: this.options.streamingTransport || this.options.transport,
            metadata: maybeCombinedMetadata,
            debug: this.options.debug,
            onMessage: (next) => observer.next(next),
            onEnd: (code: grpc.Code, message: string) => {
              if (code === 0) {
                observer.complete();
              } else if (upStreamCodes.includes(code)) {
                setTimeout(upStream, DEFAULT_TIMEOUT_TIME);
              } else {
                observer.error(new Error(`Error ${code} ${message}`));
              }
            },
          });
          observer.add(() => client.close());
        });
        upStream();
      }).pipe(share());
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

const atob: (b64: string) => string = globalThis.atob || ((b64) => globalThis.Buffer.from(b64, 'base64').toString('binary'));
      function bytesFromBase64(b64: string): Uint8Array {
        const bin = atob(b64);
        const arr = new Uint8Array(bin.length);
        for (let i = 0; i < bin.length; ++i) {
            arr[i] = bin.charCodeAt(i);
        }
        return arr;
      }

const btoa : (bin: string) => string = globalThis.btoa || ((bin) => globalThis.Buffer.from(bin, 'binary').toString('base64'));
      function base64FromBytes(arr: Uint8Array): string {
        const bin: string[] = [];
        for (const byte of arr) {
          bin.push(String.fromCharCode(byte));
        }
        return btoa(bin.join(''));
      }

type Builtin = Date | Function | Uint8Array | string | number | boolean | undefined;
      export type DeepPartial<T> = T extends Builtin
        ? T
        : T extends Array<infer U>
        ? Array<DeepPartial<U>>
        : T extends ReadonlyArray<infer U>
        ? ReadonlyArray<DeepPartial<U>>
        : T extends {}
        ? { [K in keyof T]?: DeepPartial<T[K]> }
        : Partial<T>;













// If you get a compile-error about 'Constructor<Long> and ... have no overlap',
    // add '--ts_proto_opt=esModuleInterop=true' as a flag when calling 'protoc'.
      if (util.Long !== Long) {
        util.Long = Long as any;
        configure();
      }

