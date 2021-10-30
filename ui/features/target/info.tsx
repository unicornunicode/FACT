import Table from 'react-bootstrap/Table';

import Disks from './disks';
import type {SerializableTarget} from '.';

interface Props {
	target: SerializableTarget | null;
}

const renderAccess = (target: SerializableTarget | null) => {
	if (target?.ssh !== undefined) {
		return (
			<Table size="sm" className="mb-0">
				<tbody>
					<tr>
						<th>Method</th>
						<td>SSH</td>
					</tr>
					<tr>
						<th>Host</th>
						<td>{target.ssh.user}@{target.ssh.host}:{target.ssh.port}</td>
					</tr>
					<tr>
						<th>Use <code>sudo</code></th>
						<td>{target.ssh.become ? 'Yes' : 'No'}</td>
					</tr>
				</tbody>
			</Table>
		);
	}

	return 'Unknown';
};

const Info = ({target}: Props) => (
	<Table>
		<tbody>
			<tr>
				<th>Name</th>
				<td>{target?.name}</td>
			</tr>
			<tr>
				<th>UUID</th>
				<td>{target?.uuid}</td>
			</tr>
			<tr>
				<th>Access</th>
				<td className="p-0">{renderAccess(target)}</td>
			</tr>
			<tr>
				<th>Disks</th>
				<td className="p-0"><Disks target={target}/></td>
			</tr>
		</tbody>
	</Table>
);

export default Info;
