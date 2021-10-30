import type {GetServerSideProps, NextPage} from 'next';
import Head from 'next/head';
import Container from 'react-bootstrap/Container';

import {serializeWorker} from '../../features/worker';
import type {SerializableWorker} from '../../features/worker';
import {managementRpc} from '../../features/grpc';
import {ManagementClientImpl} from '../../proto/fact/management';

import WorkerList from '../../features/worker/list';

interface Props {
	workers: SerializableWorker[];
}

export const getServerSideProps: GetServerSideProps<Props> = async () => {
	const rpc = await managementRpc();
	const client = new ManagementClientImpl(rpc);
	const {workers} = await client.ListWorker({});
	return {
		props: {
			workers: workers.map(w => serializeWorker(w)),
		},
	};
};

const WorkerListPage: NextPage<Props> = ({workers}: Props) => (
	<main>
		<Head>
			<title>Workers</title>
		</Head>
		<Container fluid>
			<WorkerList workers={workers}/>
		</Container>
	</main>
);

export default WorkerListPage;
