import Table from 'react-bootstrap/Table';

import styles from './list.module.css';
import type {SerializableWorker} from '.';

interface Props {
	workers: SerializableWorker[];
}

const ListWorker = ({workers}: Props) => {
	const renderWorker = (worker: SerializableWorker) => (
		<tr>
			<td>{worker.hostname}</td>
			<td><small className="text-muted">{worker.uuid}</small></td>
		</tr>
	);

	return (
		<Table>
			<thead>
				<tr>
					<th>Worker</th>
					<th className={styles.colUUID}>UUID</th>
				</tr>
			</thead>
			<tbody>
				{workers.map(worker => renderWorker(worker))}
			</tbody>
		</Table>
	);
};

export default ListWorker;
