import {useState, useEffect} from 'react';

import {parse as uuidParse} from 'uuid';
import type {TargetDiskinfo} from '../../proto/fact/tasks';
import {ManagementClientImpl} from '../../proto/fact/management';
import {managementRpc} from '../grpc';
import DisksTable from './disks-table';
import type {SelectCheckbox, SerializableTarget} from '.';

interface Props {
	target: SerializableTarget | null;
	checkbox?: SelectCheckbox;
}

const SelectFormDisks = ({target, checkbox}: Props) => {
	const [disks, setDisks] = useState<TargetDiskinfo[] | null>(null);
	useEffect(() => {
		if (target === null) {
			return;
		}

		const uuid = uuidParse(target.uuid) as Uint8Array;
		const fetchTargetDiskinfo = async (): Promise<void> => {
			const rpc = await managementRpc();
			const client = new ManagementClientImpl(rpc);
			const {diskinfos} = await client.ListTargetDiskinfo({uuid});
			setDisks(diskinfos);
		};

		void fetchTargetDiskinfo();
	}, [target]);

	return (
		<DisksTable target={target} disks={disks} checkbox={checkbox}/>
	);
};

export default SelectFormDisks;
