/* eslint-disable @typescript-eslint/ban-types */

import {stringify as uuidStringify, parse as uuidParse} from 'uuid';

interface UuidRaw {
	uuid: ArrayLike<number>;
}

interface UuidString {
	uuid: string;
}

export function serializeUuid<T extends UuidRaw>(o: T): Omit<T, 'uuid'> & UuidString {
	return {
		...o,
		uuid: uuidStringify(o.uuid),
	};
}

export function deserializeUuid<T extends UuidString>(o: T): Omit<T, 'uuid'> & UuidRaw {
	return {
		...o,
		uuid: uuidParse(o.uuid),
	};
}
