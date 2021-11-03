import type {GetServerSideProps, NextPage} from 'next';
import Head from 'next/head';
import Container from 'react-bootstrap/Container';
import {parse as parseUuid} from 'uuid';

import {serializeTask, formatType} from '../../features/task';
import type {SerializableTask} from '../../features/task';
import {ensureOne} from '../../utils/params';
import {managementRpc} from '../../features/grpc';
import {ManagementClientImpl} from '../../proto/fact/management';

import TaskInfo from '../../features/task/info';

interface Props {
	task: SerializableTask;
}

export const getServerSideProps: GetServerSideProps<Props> = async ({params}) => {
	const uuid = parseUuid(ensureOne(params, 'uuid')) as Uint8Array;

	const rpc = await managementRpc();
	const client = new ManagementClientImpl(rpc);
	const {task} = await client.GetTask({uuid});
	if (!task) {
		return {
			notFound: true,
		};
	}

	return {
		props: {
			task: serializeTask(task),
		},
	};
};

const GetTaskPage: NextPage<Props> = ({task}: Props) => (
	<main>
		<Head>
			<title>Task {formatType(task)}</title>
		</Head>
		<Container fluid>
			<TaskInfo task={task}/>
		</Container>
	</main>
);

export default GetTaskPage;
