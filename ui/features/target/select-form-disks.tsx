import {useState, useEffect} from 'react';
import Table from 'react-bootstrap/Table';
import filesize from 'filesize';

import {parse as uuidParse} from 'uuid';
import type {LsblkResult} from '../../proto/fact/tasks';
import {ManagementClientImpl} from '../../proto/fact/management';
import {managementRpc} from '../grpc';
import styles from './select-form.module.css';
import type {SerializableTarget} from '.';

interface Props {
	target: SerializableTarget | null;
	children?: (selection: string) => JSX.Element[] | JSX.Element | string;
}

const SelectTargetsFormDisks = ({target, children}: Props) => {
	const [disks, setDisks] = useState<LsblkResult[] | null>(null);
	useEffect(() => {
		if (target === null) {
			return;
		}

		const uuid = uuidParse(target.uuid) as Uint8Array;
		const fetchLsblkResult = async (): Promise<void> => {
			const rpc = await managementRpc();
			const client = new ManagementClientImpl(rpc);
			const {lsblkResults} = await client.ListTargetLsblk({uuid});
			setDisks(lsblkResults);
		};

		void fetchLsblkResult();
	}, [target]);
	const renderDisk = (disk: LsblkResult) => (
		<tr key={disk.deviceName}>
			{children === undefined || target === null ? '' : <td>{children(`target.${target.uuid}+disk.${disk.deviceName}`)}</td>}
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
					{children === undefined ? '' : <th className={styles.colCheck}/>}
					<th>Disk</th>
					<th className={styles.colType}>Type</th>
					<th className={styles.colSize}>Size</th>
					<th className={styles.colMount}>Mount</th>
				</tr>
				{disks?.map(disk => renderDisk(disk))}
			</tbody>
		</Table>
	);
};

export default SelectTargetsFormDisks;
