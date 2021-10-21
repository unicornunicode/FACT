import type {GetServerSideProps, NextPage} from 'next';
import Head from 'next/head';
import Container from 'react-bootstrap/Container';

import {serializeTarget} from '../../features/target';
import type {SerializableTarget} from '../../features/target';
import {managementRpc} from '../../features/grpc';
import {ManagementClientImpl} from '../../proto/fact/management';

import CreateTarget from '../../features/target/create';

interface Props {
	targets: SerializableTarget[];
}

export const getServerSideProps: GetServerSideProps<Props> = async () => {
	const rpc = await managementRpc();
	const client = new ManagementClientImpl(rpc);
	const {targets} = await client.ListTarget({});
	return {
		props: {
			targets: targets.map(t => serializeTarget(t)),
		},
	};
};

const ListTargetPage: NextPage<Props> = ({targets}: Props) => {
	const onCreateTarget = async (uuid: Uint8Array) => {
		console.debug(uuid);
	};

	return (
		<main>
			<Head>
				<title>Targets</title>
			</Head>
			<Container fluid>
				<CreateTarget onComplete={onCreateTarget}/>
				<pre><code>{JSON.stringify(targets, null, 2)}</code></pre>
			</Container>
		</main>
	);
};

export default ListTargetPage;
