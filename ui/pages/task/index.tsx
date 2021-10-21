import type {GetServerSideProps, NextPage} from 'next';
import Head from 'next/head';
import Container from 'react-bootstrap/Container';

import {serializeTask} from '../../features/task';
import type {SerializableTask} from '../../features/task';
import {managementRpc} from '../../features/grpc';
import {ManagementClientImpl} from '../../proto/fact/management';

import CreateTask from '../../features/task/create';

interface Props {
	tasks: SerializableTask[];
}

export const getServerSideProps: GetServerSideProps<Props> = async () => {
	const rpc = await managementRpc();
	const client = new ManagementClientImpl(rpc);
	const {tasks} = await client.ListTask({});
	return {
		props: {
			tasks: tasks.map(t => serializeTask(t)),
		},
	};
};

const ListTaskPage: NextPage<Props> = ({tasks}: Props) => {
	const onCreateTask = async (uuid: Uint8Array) => {
		console.debug(uuid);
	};

	return (
		<main>
			<Head>
				<title>Tasks</title>
			</Head>
			<Container fluid>
				<CreateTask onComplete={onCreateTask}/>
				<pre><code>{JSON.stringify(tasks, null, 2)}</code></pre>
			</Container>
		</main>
	);
};

export default ListTaskPage;
