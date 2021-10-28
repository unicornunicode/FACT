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
	target: SerializableTarget;
	children: (selection: string) => JSX.Element[] | JSX.Element | string;
}

const SelectTargetsFormDisks = ({target, children}: Props) => {
	const [disks, setDisks] = useState<LsblkResult[] | null>(null);
	useEffect(() => {
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
			<td>{children(`target.${target.uuid}+disk.${disk.deviceName}`)}</td>
			<td>{disk.deviceName}</td>
			<td>{disk.type}</td>
			<td title={`${disk.size} bytes`}>{filesize(disk.size)}</td>
			<td>{disk.mountpoint}</td>
		</tr>
	);

	const renderLoading = () => (
		<div className="p-2 text-center text-muted">
			Loading...
		</div>
	);

	return disks === null ? renderLoading() : (
		<Table size="sm" className="mb-0">
			<tbody>
				<tr>
					<th className={styles.colCheck}/>
					<th>Disk</th>
					<th>Type</th>
					<th>Size</th>
					<th>Mount</th>
				</tr>
				{disks?.map(disk => renderDisk(disk))}
			</tbody>
		</Table>
	);
};

export default SelectTargetsFormDisks;