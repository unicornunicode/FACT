import type {GetServerSideProps, NextPage} from 'next';
import Head from 'next/head';

import {parse as uuidParse} from 'uuid';
import {ensureOne} from '../../utils/params';
import type {ListTask} from '../../proto/fact/management';
import {managementRpc} from '../../features/grpc';
import {ManagementClientImpl} from '../../proto/fact/management';

interface Props {
	task: ListTask;
}

export const getServerSideProps: GetServerSideProps<Props> = async ({params}) => {
	const uuid = uuidParse(ensureOne(params, 'uuid'));

	const rpc = await managementRpc();
	const client = new ManagementClientImpl(rpc);
	const {tasks} = await client.ListTask({});
	const task = tasks.find(task => task.uuid === uuid);
	if (!task) {
		return {
			notFound: true,
		};
	}

	return {
		props: {
			task,
		},
	};
};

const ListTaskPage: NextPage<Props> = ({task}: Props) => (
	<main>
		<Head>
			<title>Task {task.uuid}</title>
		</Head>
		<pre><code>{JSON.stringify(task, null, 2)}</code></pre>
	</main>
);

export default ListTaskPage;
