import Table from 'react-bootstrap/Table';

import {listTask_StatusToJSON} from '../../proto/fact/management';

import styles from './list.module.css';
import type {SerializableTask} from '.';

interface Props {
	tasks: SerializableTask[];
}

const renderType = (task: SerializableTask): string => {
	if (task.taskCollectDisk !== undefined) {
		return 'Capture disks';
	}

	if (task.taskCollectMemory !== undefined) {
		return 'Capture memory';
	}

	if (task.taskCollectLsblk !== undefined) {
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
						<td>{task.taskCollectDisk.selector?.path}</td>
					</tr>
				</tbody>
			</Table>
		);
	}

	if (task.taskCollectMemory !== undefined) {
		return '';
	}

	if (task.taskCollectLsblk !== undefined) {
		return '';
	}

	return '';
};

const ListTask = ({tasks}: Props) => {
	const renderTask = (task: SerializableTask) => (
		<tr>
			<td>{listTask_StatusToJSON(task.status)}</td>
			<td>{renderType(task)}</td>
			<td className="p-0">{renderOptions(task)}</td>
			<td className="p-0">
				<Table size="sm" className="mb-0">
					<tbody>
						{task.target ? (
							<tr>
								<th>Target</th>
								<td><small className="text-muted">{task.target}</small></td>
							</tr>
						) : ''}
						<tr>
							<th>Worker</th>
							<td><small className="text-muted">{task.worker}</small></td>
						</tr>
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
					</tbody>
				</Table>
			</td>
		</tr>
	);

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
				{tasks.map(task => renderTask(task))}
			</tbody>
		</Table>
	);
};

export default ListTask;
