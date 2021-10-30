import {useState, useEffect} from 'react';

import {parse as uuidParse} from 'uuid';
import type {LsblkResult} from '../../proto/fact/tasks';
import {ManagementClientImpl} from '../../proto/fact/management';
import {managementRpc} from '../grpc';
import DisksTable from './disks-table';
import type {SelectCheckbox, SerializableTarget} from '.';

interface Props {
	target: SerializableTarget | null;
	checkbox?: SelectCheckbox;
}

const SelectFormDisks = ({target, checkbox}: Props) => {
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

	return (
		<DisksTable target={target} disks={disks} checkbox={checkbox}/>
	);
};

export default SelectFormDisks;
