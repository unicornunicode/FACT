import {serializeUuid} from '../../utils/serde';
import type {ListTarget} from '../../proto/fact/management';

export interface SerializableTarget extends Omit<ListTarget, 'uuid'> {
	uuid: string;
}

export function serializeTarget(target: ListTarget): SerializableTarget {
	return serializeUuid(target);
}

export type SelectCheckbox = (selection: string) => JSX.Element[] | JSX.Element | string;
