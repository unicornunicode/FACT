import Link from 'next/link';
import Table from 'react-bootstrap/Table';

import {listTask_StatusToJSON} from '../../proto/fact/management';
import styles from './list.module.css';
import type {SerializableTask} from '.';

interface Props {
	tasks: SerializableTask[] | null;
	simple?: boolean;
}

const renderType = (task: SerializableTask): string => {
	if (task.taskCollectDisk !== undefined) {
		return 'Capture disks';
	}

	if (task.taskCollectMemory !== undefined) {
		return 'Capture memory';
	}

	if (task.taskCollectDiskinfo !== undefined) {
		return 'Scan disks';
	}

	return 'Unknown';
};

const renderOptions = (task: SerializableTask): JSX.Element | string => {
	if (task.taskCollectDisk !== undefined) {
		return (
			<Table size="sm" className="mb-0">
				<tbody>
					<tr>
						<th>Disk</th>
						<td>{task.taskCollectDisk.deviceName}</td>
					</tr>
				</tbody>
			</Table>
		);
	}

	if (task.taskCollectMemory !== undefined) {
		return '';
	}

	if (task.taskCollectDiskinfo !== undefined) {
		return '';
	}

	return '';
};

const renderDetails = (task: SerializableTask, simple: boolean | undefined): JSX.Element => (
	<Table size="sm" className="mb-0">
		<tbody>
			{simple ?? (
				<tr>
					<th>UUID</th>
					<td><small className="text-muted">{task.uuid}</small></td>
				</tr>
			)}
			{task.target && (
				<tr>
					<th>Target</th>
					<td><small className="text-muted">{task.target && <Link href={`/target/${task.target}`}>{task.target}</Link>}</small></td>
				</tr>
			)}
			{simple ?? (
				<>
					{task.worker && (
						<tr>
							<th>Worker</th>
							<td><small className="text-muted">{task.worker}</small></td>
						</tr>
					)}
					<tr>
						<th>Created</th>
						<td>{task.createdAt ? new Date(task.createdAt).toLocaleString() : ''}</td>
					</tr>
					<tr>
						<th>Assigned</th>
						<td>{task.assignedAt ? new Date(task.assignedAt).toLocaleString() : ''}</td>
					</tr>
					<tr>
						<th>Completed</th>
						<td>{task.completedAt ? new Date(task.completedAt).toLocaleString() : ''}</td>
					</tr>
				</>
			)}
		</tbody>
	</Table>
);

const List = ({tasks, simple}: Props) => {
	const renderTask = (task: SerializableTask) => (
		<tr key={task.uuid}>
			<td>{listTask_StatusToJSON(task.status)}</td>
			<td>{renderType(task)}</td>
			<td className="p-0">{renderOptions(task)}</td>
			<td className="p-0">{renderDetails(task, simple)}</td>
		</tr>
	);

	const renderTasks = (tasks: SerializableTask[] | null) => {
		if (tasks === null) {
			return (
				<tr>
					<td colSpan={4} className="p-2 text-center fst-italic text-muted">
						Loading
					</td>
				</tr>
			);
		}

		if (tasks.length === 0) {
			return (
				<tr>
					<td colSpan={4} className="p-2 text-center fst-italic">
						No tasks. Create one in &ldquo;Targets&rdquo;
					</td>
				</tr>
			);
		}

		return tasks.map(task => renderTask(task));
	};

	return (
		<Table>
			<thead>
				<tr>
					<th>Status</th>
					<th>Task</th>
					<th>Options</th>
					<th className={styles.colDetails}>Details</th>
				</tr>
			</thead>
			<tbody>
				{renderTasks(tasks)}
			</tbody>
		</Table>
	);
};

export default List;
