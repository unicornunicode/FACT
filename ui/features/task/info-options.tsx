import Table from 'react-bootstrap/Table';

import Uuid from '../uuid';
import type {SerializableTask} from '.';

interface Props {
	task: SerializableTask;
}

const InfoOptions = ({task}: Props) => {
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
		return null;
	}

	if (task.taskCollectDiskinfo !== undefined) {
		return null;
	}

	if (task.taskIngest !== null) {
		const collectedUuid = task.taskIngest.collectedUuid;
		return (
			<Table size="sm" className="mb-0">
				<tbody>
					<tr>
						<th>Capture task</th>
						<td><Uuid uuid={collectedUuid} href={`/task/${collectedUuid}`}/></td>
					</tr>
				</tbody>
			</Table>
		);
	}

	return null;
};

export default InfoOptions;
