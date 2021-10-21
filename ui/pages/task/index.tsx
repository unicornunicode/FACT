import type {GetServerSideProps, NextPage} from 'next';
import Head from 'next/head';

import type {ListTask} from '../../proto/fact/management';
import {managementRpc} from '../../features/grpc';
import {ManagementClientImpl} from '../../proto/fact/management';

interface Props {
	tasks: ListTask[];
}

const ListTaskPage: NextPage<Props> = ({tasks}: Props) => (
	<main>
		<Head>
			<title>Tasks</title>
		</Head>
		<pre><code>{JSON.stringify(tasks, null, 2)}</code></pre>
	</main>
);

export const getServerSideProps: GetServerSideProps<Props> = async () => {
	const rpc = await managementRpc();
	const client = new ManagementClientImpl(rpc);
	const {tasks} = await client.ListTask({});
	return {
		props: {
			tasks,
		},
	};
};

export default ListTaskPage;
