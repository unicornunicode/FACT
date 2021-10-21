type Query = Record<string, string | string[] | undefined>;

export class InvalidQueryParameters extends Error {
	constructor(key: string, found: string | string[] | undefined) {
		let formatFound;
		if (found === undefined) {
			formatFound = 'is undefined';
		} else if (Array.isArray(found)) {
			formatFound = 'has multiple values';
		} else {
			formatFound = `is ${found}`;
		}

		super(`Invalid query parameters: ${key} ${formatFound}`);
	}
}

export function ensureOne(parameters: Query | undefined, key: string): string {
	const value = parameters?.[key];
	if (value === undefined || Array.isArray(value)) {
		throw new InvalidQueryParameters(key, value);
	}

	return value;
}
