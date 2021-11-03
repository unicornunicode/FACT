import type {NextPage} from 'next';
import Head from 'next/head';
import Link from 'next/link';
import {useEffect, useState} from 'react';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';

import {serializeTask, sortCompletedAt} from '../features/task';
import type {SerializableTask} from '../features/task';
import {serializeWorker} from '../features/worker';
import type {SerializableWorker} from '../features/worker';
import {ManagementClientImpl} from '../proto/fact/management';
import {managementRpc} from '../features/grpc';

import TaskList from '../features/task/list';
import WorkerList from '../features/worker/list';

const Home: NextPage = () => {
	const [tasks, setTasks] = useState<SerializableTask[]>([]);
	const [workers, setWorkers] = useState<SerializableWorker[]>([]);

	useEffect(() => {
		const fetchTasks = async (): Promise<void> => {
			const rpc = await managementRpc();
			const client = new ManagementClientImpl(rpc);
			const {tasks} = await client.ListTask({limit: 8});
			setTasks(tasks.map(task => serializeTask(task)).sort(sortCompletedAt));
		};

		void fetchTasks();
	}, []);

	useEffect(() => {
		const fetchWorkers = async (): Promise<void> => {
			const rpc = await managementRpc();
			const client = new ManagementClientImpl(rpc);
			const {workers} = await client.ListWorker({});
			setWorkers(workers.map(worker => serializeWorker(worker)));
		};

		void fetchWorkers();
	}, []);

	return (
		<main>
			<Head>
				<title>Overview</title>
			</Head>
			<Container fluid>
				<h2>Recent Tasks</h2>
				<TaskList simple tasks={tasks}/>
				<div className="m-3 text-center">
					<Link passHref href="/task"><Button variant="link">Show details</Button></Link>
				</div>
				<h2>Workers</h2>
				<WorkerList workers={workers}/>
			</Container>
		</main>
	);
};

export default Home;
