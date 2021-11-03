import Uuid from '../uuid';
import type {SerializableTarget, SelectCheckbox} from '.';

interface Props {
	target: SerializableTarget;
	checkbox?: SelectCheckbox;
}

const SelectFormTarget = ({target, checkbox}: Props) => (
	<tr>
		{checkbox && <td>{checkbox([`target.${target.uuid}`])}</td>}
		<td>{target.name}</td>
		<td><Uuid uuid={target.uuid} href={`/target/${target.uuid}`}/></td>
	</tr>
);

export default SelectFormTarget;
