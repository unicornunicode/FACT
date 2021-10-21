import {serializeUuid} from '../../utils/serde';
import type {ListWorker} from '../../proto/fact/management';

export interface SerializableWorker extends Omit<ListWorker, 'uuid'> {
	uuid: string;
}

export function serializeWorker(target: ListWorker): SerializableWorker {
	return serializeUuid(target);
}
