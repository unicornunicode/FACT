import Table from 'react-bootstrap/Table';

import {listTask_StatusToJSON} from '../../proto/fact/management';
import InfoOptions from './info-options';
import InfoDetails from './info-details';
import type {SerializableTask} from '.';
import {formatType} from '.';

interface Props {
	task: SerializableTask | null;
}

const Info = ({task}: Props) => (
	<Table>
		<tbody>
			<tr>
				<th>Status</th>
				<td>{task && listTask_StatusToJSON(task.status)}</td>
			</tr>
			<tr>
				<th>Type</th>
				<td>{task && formatType(task)}</td>
			</tr>
			<tr>
				<th>Details</th>
				<td className="p-0">{task && <InfoDetails task={task}/>}</td>
			</tr>
			<tr>
				<th>Options</th>
				<td className="p-0">{task && <InfoOptions task={task}/>}</td>
			</tr>
		</tbody>
	</Table>
);

export default Info;
