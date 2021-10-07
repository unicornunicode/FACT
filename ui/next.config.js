/* eslint-disable unicorn/prefer-module */

/** @type {import('next').NextConfig} */

module.exports = {
	reactStrictMode: true,
	experimental: {
		swcLoader: true,
		swcMinify: true,
	},
};
