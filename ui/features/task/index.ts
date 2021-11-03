import {stringify as stringifyUuid} from 'uuid';

import {serializeUuid} from '../../utils/serde';
import type {ListTask} from '../../proto/fact/management';
import type {TaskIngest} from '../../proto/fact/tasks';

export interface SerializableTask extends Omit<ListTask, 'uuid' | 'target' | 'worker' | 'createdAt' | 'assignedAt' | 'completedAt' | 'taskIngest'> {
	uuid: string;
	target: string | null;
	worker: string | null;
	createdAt: string | null;
	assignedAt: string | null;
	completedAt: string | null;
	taskIngest: SerializableTaskIngest | null;
}

export function serializeTask(task: ListTask): SerializableTask {
	return {
		...serializeUuid(task),
		target: task.target.length === 0 ? null : stringifyUuid(task.target),
		worker: task.worker.length === 0 ? null : stringifyUuid(task.worker),
		createdAt: task.createdAt?.toISOString() ?? null,
		assignedAt: task.assignedAt?.toISOString() ?? null,
		completedAt: task.completedAt?.toISOString() ?? null,
		taskIngest: task.taskIngest === undefined ? null : serializeTaskIngest(task.taskIngest),
	};
}

export interface SerializableTaskIngest extends Omit<TaskIngest, 'collectedUuid'> {
	collectedUuid: string;
}

export function serializeTaskIngest(taskIngest: TaskIngest): SerializableTaskIngest {
	return {
		collectedUuid: stringifyUuid(taskIngest.collectedUuid),
	};
}

export function sortCompletedAt(a: SerializableTask, b: SerializableTask) {
	if (a.createdAt === null) {
		return -1;
	}

	if (b.createdAt === null) {
		return 1;
	}

	return new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime();
}

export function formatType(task: SerializableTask): string {
	if (task.taskCollectDisk !== undefined) {
		return 'Capture disks';
	}

	if (task.taskCollectMemory !== undefined) {
		return 'Capture memory';
	}

	if (task.taskCollectDiskinfo !== undefined) {
		return 'Scan disks';
	}

	if (task.taskIngest !== undefined) {
		return 'Ingest captures';
	}

	return 'Unknown';
}
