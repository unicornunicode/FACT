import type {NextPage} from 'next';
import Head from 'next/head';
import {useEffect, useState} from 'react';

import type {ListTask} from '../proto/fact/management';
import {ManagementClientImpl} from '../proto/fact/management';
import {managementRpc} from '../features/grpc';

const Home: NextPage = () => {
	const [tasks, setTasks] = useState<ListTask[]>([]);
	useEffect(() => {
		const fetchTasks = async (): Promise<void> => {
			const rpc = await managementRpc();
			const client = new ManagementClientImpl(rpc);
			const listTaskResult = await client.ListTask({});
			setTasks(listTaskResult.tasks);
		};

		void fetchTasks();
	}, []);
	return (
		<main>
			<Head>
				<title>Overview</title>
			</Head>
			<pre><code>{JSON.stringify(tasks, null, 2)}</code></pre>
		</main>
	);
};

export default Home;
