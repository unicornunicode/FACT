import type {SerializableTarget} from '.';

interface Props {
	target: SerializableTarget;
	children: (selection: string) => JSX.Element[] | JSX.Element | string;
}

const renderAccess = ({ssh}: SerializableTarget) => {
	if (ssh) {
		return (
			<span>
				<strong className="text-muted">SSH: </strong>
				{ssh.user}@{ssh.host}:{ssh.port}
				{ssh.become ? <>, with <code>sudo</code></> : <></>}
			</span>
		);
	}

	return <span>Invalid</span>;
};

const SelectTargetsFormTarget = ({target, children}: Props) => (
	<tr>
		<td>{children(target.uuid)}</td>
		<td>{target.name}</td>
		<td>{renderAccess(target)}</td>
		<td><small className="text-muted">{target.uuid}</small></td>
	</tr>
);

export default SelectTargetsFormTarget;
