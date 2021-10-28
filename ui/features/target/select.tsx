import Button from 'react-bootstrap/Button';

import SelectTargetsForm from './select-form';
import type {SelectTargetsFormData} from './select-form';
import type {SerializableTarget} from '.';

interface Props {
	targets: SerializableTarget[];
}

const SelectTargets = ({targets}: Props) => {
	const onSubmit = async (data: SelectTargetsFormData) => {
		let selection = data.selection;
		if (!Array.isArray(selection)) {
			selection = [selection];
		}

		console.debug(selection);
	};

	return (
		<SelectTargetsForm targets={targets} mode={null} onSubmit={onSubmit}>
			<Button type="submit">Submit</Button>
		</SelectTargetsForm>
	);
};

export default SelectTargets;
