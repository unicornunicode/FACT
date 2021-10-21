import {parse as parseUuid} from 'uuid';

import {ManagementClientImpl} from '../../proto/fact/management';
import {managementRpc} from '../grpc';

import CreateTaskForm from './create-form';
import type {CreateTaskFormData} from './create-form';

interface Props {
	onComplete: (uuid: Uint8Array) => Promise<void>;
}

const CreateTask = ({onComplete}: Props) => {
	const onSubmit = async (data: CreateTaskFormData) => {
		const rpc = await managementRpc();
		const client = new ManagementClientImpl(rpc);
		const {uuid} = await client.CreateTask({
			target: new Uint8Array(parseUuid(data.target)),
			taskCollectDisk: data.task === 'collectDisk' ? {
				selector: {
					path: data.collectDiskSelectorPath,
				},
			} : undefined,
			taskCollectMemory: data.task === 'collectMemory' ? {} : undefined,
		});
		await onComplete(uuid);
	};

	return (
		<CreateTaskForm onSubmit={onSubmit}/>
	);
};

export default CreateTask;
