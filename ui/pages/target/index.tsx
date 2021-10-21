import type {GetServerSideProps, NextPage} from 'next';
import Head from 'next/head';
import Container from 'react-bootstrap/Container';

import CreateTarget from '../../features/target/create';
import type {ListTarget} from '../../proto/fact/management';
import {managementRpc} from '../../features/grpc';
import {ManagementClientImpl} from '../../proto/fact/management';

interface Props {
	targets: ListTarget[];
}

export const getServerSideProps: GetServerSideProps<Props> = async () => {
	const rpc = await managementRpc();
	const client = new ManagementClientImpl(rpc);
	const {targets} = await client.ListTarget({});
	return {
		props: {
			targets,
		},
	};
};

const ListTargetPage: NextPage<Props> = ({targets}: Props) => (
	<main>
		<Head>
			<title>Targets</title>
		</Head>
		<Container fluid>
			<CreateTarget/>
			<pre><code>{JSON.stringify(targets, null, 2)}</code></pre>
		</Container>
	</main>
);

export default ListTargetPage;
