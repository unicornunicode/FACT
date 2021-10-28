import {useState, useEffect, useCallback} from 'react';
import type {GetServerSideProps, NextPage} from 'next';
import Head from 'next/head';
import {useRouter} from 'next/router';
import Container from 'react-bootstrap/Container';

import {serializeTarget} from '../../features/target';
import type {SerializableTarget} from '../../features/target';
import {managementRpc} from '../../features/grpc';
import {ManagementClientImpl} from '../../proto/fact/management';

import CreateTarget from '../../features/target/create';
import SelectTargets from '../../features/target/select';

interface Props {
	targets: SerializableTarget[];
}

export const getServerSideProps: GetServerSideProps<Props> = async () => {
	const rpc = await managementRpc();
	const client = new ManagementClientImpl(rpc);
	const {targets} = await client.ListTarget({});
	return {
		props: {
			targets: targets.map(t => serializeTarget(t)),
		},
	};
};

const ListTargetPage: NextPage<Props> = ({targets}: Props) => {
	const router = useRouter();

	const onCreateTarget = useCallback(async (_uuid: Uint8Array) => {
		await router.replace(router.asPath);
	}, [router]);
	useEffect(() => {
		const interval = setInterval(async () => {
			await router.replace(router.asPath);
		}, 10_000);

		return () => {
			clearInterval(interval);
		};
	}, [router]);

	// eslint-disable-next-line @typescript-eslint/naming-convention
	const [showAddTarget, setShowAddTarget] = useState(false);
	const handleCloseAddTarget = useCallback(async () => {
		setShowAddTarget(false);
	}, []);

	const handleShowAddTarget = useCallback(async () => {
		setShowAddTarget(true);
	}, []);

	return (
		<main>
			<Head>
				<title>Targets</title>
			</Head>
			<Container fluid>
				<SelectTargets targets={targets} onShowAddTarget={handleShowAddTarget}/>
			</Container>
			<CreateTarget modal modalShow={showAddTarget} onComplete={onCreateTarget} onModalClose={handleCloseAddTarget}/>
		</main>
	);
};

export default ListTargetPage;
