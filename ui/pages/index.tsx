import {Button} from 'react-bootstrap';
import Head from 'next/head';
import Image from 'next/image';
import type {NextPage} from 'next';

import styles from '../styles/Home.module.css';

const Home: NextPage = () => (
	<div>
		<Head>
			<title>Create Next App</title>
		</Head>

		<main>
			<Button>Hello, world</Button>
			<Image src="/vercel.svg" alt="Vercel Logo" width={72} height={16}/>
		</main>

		<footer className={styles.footer}/>
	</div>
);

export default Home;
