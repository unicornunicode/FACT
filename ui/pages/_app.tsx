import '../styles/globals.css';
import type {AppProps} from 'next/app';
import Head from 'next/head';

const MyApp = ({Component, pageProps}: AppProps) => (
	<>
		<Head>
			<link
				rel="stylesheet"
				href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css"
				integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU"
				crossOrigin="anonymous"
			/>
		</Head>
		<Component {...pageProps}/>
	</>
);

export default MyApp;
