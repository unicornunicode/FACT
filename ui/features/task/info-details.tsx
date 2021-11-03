import Table from 'react-bootstrap/Table';

import Uuid from '../uuid';
import type {SerializableTask} from '.';

interface Props {
	task: SerializableTask;
	simple?: boolean;
}

const InfoDetails = ({task, simple}: Props) => (
	<Table size="sm" className="mb-0">
		<tbody>
			{simple ?? (
				<tr>
					<th>UUID</th>
					<td><Uuid uuid={task.uuid} href={`/task/${task.uuid}`}/></td>
				</tr>
			)}
			{task.target && (
				<tr>
					<th>Target</th>
					<td><Uuid uuid={task.target} href={`/target/${task.target}`}/></td>
				</tr>
			)}
			{simple ?? (
				<>
					{task.worker && (
						<tr>
							<th>Worker</th>
							<td><Uuid uuid={task.worker}/></td>
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

export default InfoDetails;
