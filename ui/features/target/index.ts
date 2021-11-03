import {stringify as uuidStringify} from 'uuid';

import {serializeUuid} from '../../utils/serde';
import type {ListTarget, ListTargetDiskinfo} from '../../proto/fact/management';

export interface SerializableTarget extends Omit<ListTarget, 'uuid'> {
	uuid: string;
}

export function serializeTarget(target: ListTarget): SerializableTarget {
	return serializeUuid(target);
}

export interface SerializableTargetDiskinfo extends Omit<ListTargetDiskinfo, 'collectedAt' | 'collectedUuid'> {
	collectedAt: string | null;
	collectedUuid: string | null;
}

export function serializeTargetDiskinfo(diskinfo: ListTargetDiskinfo): SerializableTargetDiskinfo {
	return {
		...diskinfo,
		collectedAt: diskinfo.collectedAt?.toISOString() ?? null,
		collectedUuid: diskinfo.collectedUuid.length === 0 ? null : uuidStringify(diskinfo.collectedUuid),
	};
}

export type SelectCheckbox = (selection: string[]) => JSX.Element[] | JSX.Element | string;
