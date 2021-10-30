import {ManagementClientImpl} from '../../proto/fact/management';
import {managementRpc} from '../grpc';

import CreateForm from './create-form';
import type {CreateFormData} from './create-form';

interface Props {
	onComplete: (uuid: Uint8Array) => Promise<void>;
	modal: boolean;
	modalShow: boolean;
	onModalClose: () => void;
}

const Create = ({onComplete, modal, modalShow, onModalClose}: Props) => {
	const onSubmit = async (data: CreateFormData) => {
		const rpc = await managementRpc();
		const client = new ManagementClientImpl(rpc);
		const {uuid} = await client.CreateTarget({
			name: data.name,
			ssh: {
				host: data.sshHost,
				port: data.sshPort,
				user: data.sshUser,
				privateKey: data.sshPrivateKey,
				become: data.sshBecome,
				becomePassword: data.sshBecomePassword,
			},
		});
		await onComplete(uuid);
	};

	return (
		<CreateForm modal={modal} modalShow={modalShow} onSubmit={onSubmit} onModalClose={onModalClose}/>
	);
};

export default Create;
