import {useEffect} from 'react';
import type {GetServerSideProps, NextPage} from 'next';
import Head from 'next/head';
import {useRouter} from 'next/router';
import Container from 'react-bootstrap/Container';

import {serializeTask} from '../../features/task';
import type {SerializableTask} from '../../features/task';
import {managementRpc} from '../../features/grpc';
import {ManagementClientImpl} from '../../proto/fact/management';

import TaskList from '../../features/task/list';

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
	const router = useRouter();

	useEffect(() => {
		const interval = setInterval(async () => {
			await router.replace(router.asPath);
		}, 10_000);

		return () => {
			clearInterval(interval);
		};
	}, [router]);

	return (
		<main>
			<Head>
				<title>Tasks</title>
			</Head>
			<Container fluid>
				<TaskList tasks={tasks}/>
			</Container>
		</main>
	);
};

export default ListTaskPage;
