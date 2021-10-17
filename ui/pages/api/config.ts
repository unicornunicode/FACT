import type {NextApiRequest, NextApiResponse} from 'next';

import type {Config} from '../../features/config';
import {readConfig} from '../../features/config';

export default async function handler(
	request: NextApiRequest,
	response: NextApiResponse<Config>,
) {
	if (request.method === 'GET') {
		response.status(200).json(await readConfig());
	} else {
		response.status(405).end();
	}
}
