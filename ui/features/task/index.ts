import {stringify as stringifyUuid} from 'uuid';

import {serializeUuid} from '../../utils/serde';
import type {ListTask} from '../../proto/fact/management';

export interface SerializableTask extends Omit<ListTask, 'uuid' | 'target' | 'worker' | 'createdAt' | 'assignedAt' | 'completedAt'> {
	uuid: string;
	target: string;
	worker: string;
	createdAt: string | null;
	assignedAt: string | null;
	completedAt: string | null;
}

export function serializeTask(task: ListTask): SerializableTask {
	return {
		...serializeUuid(task),
		target: stringifyUuid(task.target),
		worker: stringifyUuid(task.worker),
		createdAt: task.createdAt?.toISOString() ?? null,
		assignedAt: task.assignedAt?.toISOString() ?? null,
		completedAt: task.completedAt?.toISOString() ?? null,
	};
}
