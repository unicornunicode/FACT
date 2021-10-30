import Table from 'react-bootstrap/Table';
import filesize from 'filesize';

import type {LsblkResult} from '../../proto/fact/tasks';
import styles from './select-form.module.css';
import type {SerializableTarget, SelectCheckbox} from '.';

interface Props {
	target: SerializableTarget | null;
	disks: LsblkResult[] | null;
	checkbox?: SelectCheckbox;
}

const DisksTable = ({target, disks, checkbox}: Props) => {
	const renderDisk = (disk: LsblkResult) => (
		<tr key={disk.deviceName}>
			{checkbox === undefined ? '' : <td>{target === null ? '' : checkbox(`target.${target.uuid}+disk.${disk.deviceName}`)}</td>}
			<td className="text-nowrap">{disk.deviceName}</td>
			<td>{disk.type}</td>
			<td title={`${disk.size} bytes`}>{filesize(disk.size)}</td>
			<td>{disk.mountpoint}</td>
		</tr>
	);

	if (disks === null) {
		return (
			<div className="p-2 text-center fst-italic text-muted">
				Loading...
			</div>
		);
	}

	if (disks.length === 0) {
		return (
			<div className="p-2 text-center fst-italic">
				No known disks
			</div>
		);
	}

	return (
		<Table size="sm" className="mb-0">
			<tbody>
				<tr>
					{checkbox === undefined ? '' : <th className={styles.colCheck}/>}
					<th>Disk</th>
					<th className={styles.colType}>Type</th>
					<th className={styles.colSize}>Size</th>
					<th className={styles.colMount}>Mount</th>
				</tr>
				{disks.map(disk => renderDisk(disk))}
			</tbody>
		</Table>
	);
};

export default DisksTable;