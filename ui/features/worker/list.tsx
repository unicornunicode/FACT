import Table from 'react-bootstrap/Table';

import Uuid from '../uuid';
import styles from './list.module.css';
import type {SerializableWorker} from '.';

interface Props {
	workers: SerializableWorker[] | null;
}

const List = ({workers}: Props) => {
	const renderWorker = (worker: SerializableWorker) => (
		<tr key={worker.uuid}>
			<td>{worker.hostname}</td>
			<td><Uuid uuid={worker.uuid}/></td>
		</tr>
	);

	const renderWorkers = (workers: SerializableWorker[] | null) => {
		if (workers === null) {
			return (
				<tr>
					<td colSpan={2} className="p-2 text-center fst-italic text-muted">
						Loading
					</td>
				</tr>
			);
		}

		if (workers.length === 0) {
			return (
				<tr>
					<td colSpan={2} className="p-2 text-center fst-italic">
						No known workers. Add one by starting it
					</td>
				</tr>
			);
		}

		return workers.map(worker => renderWorker(worker));
	};

	return (
		<Table>
			<thead>
				<tr>
					<th>Worker</th>
					<th className={styles.colUUID}>UUID</th>
				</tr>
			</thead>
			<tbody>{renderWorkers(workers)}</tbody>
		</Table>
	);
};

export default List;
