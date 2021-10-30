import Link from 'next/link';

import type {SerializableTarget, SelectCheckbox} from '.';

interface Props {
	target: SerializableTarget;
	checkbox?: SelectCheckbox;
}

const SelectFormTarget = ({target, checkbox}: Props) => (
	<tr>
		{checkbox === undefined ? '' : <td>{checkbox(`target.${target.uuid}`)}</td>}
		<td>{target.name}</td>
		<td><small className="text-muted"><Link href={`/target/${target.uuid}`}>{target.uuid}</Link></small></td>
	</tr>
);

export default SelectFormTarget;
