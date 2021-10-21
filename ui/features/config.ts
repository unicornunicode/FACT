import process from 'process';

export type Config = {
	management: {
		endpoint: string;
		options: {
			debug?: boolean;
		};
	};
};

export async function readConfig(): Promise<Config> {
	if (typeof window !== 'undefined') {
		const response = await fetch('/api/config');
		const config = await response.json() as Config;
		return config;
	}

	return {
		management: {endpoint: process.env.MANAGEMENT_ENDPOINT ?? 'http://localhost:5124', options: {debug: false}},
	};
}
