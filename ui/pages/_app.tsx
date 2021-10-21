import type {AppProps} from 'next/app';
import Head from 'next/head';
import SSRProvider from 'react-bootstrap/SSRProvider';

import Navigation from '../features/navigation/navigation';

import '../styles/globals.scss';

const MyApp = ({Component, pageProps}: AppProps) => (
	<>
		<Head>
			<title>FACT</title>
		</Head>
		<SSRProvider>
			<Navigation/>
			<Component {...pageProps}/>
		</SSRProvider>
	</>
);

export default MyApp;
