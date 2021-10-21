import {serializeUuid} from '../../utils/serde';
import type {ListTask} from '../../proto/fact/management';

export interface SerializableTask extends Omit<ListTask, 'uuid'> {
	uuid: string;
}

export function serializeTask(task: ListTask): SerializableTask {
	return serializeUuid(task);
}
