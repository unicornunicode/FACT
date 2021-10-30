import type {GetServerSideProps, NextPage} from 'next';
import Head from 'next/head';
import Container from 'react-bootstrap/Container';
import {parse as parseUuid} from 'uuid';

import {serializeTarget} from '../../features/target';
import type {SerializableTarget} from '../../features/target';
import {ensureOne} from '../../utils/params';
import {managementRpc} from '../../features/grpc';
import {ManagementClientImpl} from '../../proto/fact/management';

import TargetInfo from '../../features/target/info';

interface Props {
	target: SerializableTarget;
}

export const getServerSideProps: GetServerSideProps<Props> = async ({params}) => {
	const uuid = parseUuid(ensureOne(params, 'uuid')) as Uint8Array;

	const rpc = await managementRpc();
	const client = new ManagementClientImpl(rpc);
	const {target} = await client.GetTarget({uuid});
	if (!target) {
		return {
			notFound: true,
		};
	}

	return {
		props: {
			target: serializeTarget(target),
		},
	};
};

const GetTargetPage: NextPage<Props> = ({target}: Props) => (
	<main>
		<Head>
			<title>Target {target.name}</title>
		</Head>
		<Container fluid>
			<TargetInfo target={target}/>
		</Container>
	</main>
);

export default GetTargetPage;
