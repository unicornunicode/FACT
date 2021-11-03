import Table from 'react-bootstrap/Table';

import {listTask_StatusToJSON} from '../../proto/fact/management';
import styles from './list.module.css';
import InfoOptions from './info-options';
import InfoDetails from './info-details';
import type {SerializableTask} from '.';
import {formatType} from '.';

interface Props {
	tasks: SerializableTask[] | null;
	simple?: boolean;
}

const List = ({tasks, simple}: Props) => {
	const renderTask = (task: SerializableTask) => (
		<tr key={task.uuid}>
			<td>{listTask_StatusToJSON(task.status)}</td>
			<td>{formatType(task)}</td>
			<td className="p-0"><InfoOptions task={task}/></td>
			<td className="p-0"><InfoDetails task={task} simple={simple}/></td>
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
