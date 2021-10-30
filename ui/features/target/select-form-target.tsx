import Link from 'next/link';

import type {SerializableTarget} from '.';

interface Props {
	target: SerializableTarget;
	children: (selection: string) => JSX.Element[] | JSX.Element | string;
}

const SelectTargetsFormTarget = ({target, children}: Props) => (
	<tr>
		<td>{children(`target.${target.uuid}`)}</td>
		<td>{target.name}</td>
		<td><small className="text-muted"><Link href={`/target/${target.uuid}`}>{target.uuid}</Link></small></td>
	</tr>
);

export default SelectTargetsFormTarget;
