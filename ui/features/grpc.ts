import {NodeHttpTransport} from '@improbable-eng/grpc-web-node-http-transport';

import {GrpcWebImpl} from '../proto/fact/management';
import {readConfig} from './config';

export async function managementRpc(): Promise<GrpcWebImpl> {
	const {management} = await readConfig();
	let transport;
	if (typeof window === 'undefined') {
		transport = NodeHttpTransport();
	}

	const rpc = new GrpcWebImpl(management.endpoint, {
		...management.options,
		transport,
	});
	return rpc;
}
