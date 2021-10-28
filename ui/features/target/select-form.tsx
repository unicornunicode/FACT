import {useState, useEffect, Fragment} from 'react';
import type {FormEvent} from 'react';
import Table from 'react-bootstrap/Table';
import Form from 'react-bootstrap/Form';

import SelectTargetsFormTarget from './select-form-target';
import SelectTargetsFormDisks from './select-form-disks';
import styles from './select-form.module.css';
import type {SerializableTarget} from '.';

export interface SelectTargetsFormData {
	selection: string[];
}

type SelectMode = null | 'target' | 'target+disk' | 'disk';

interface Props {
	targets: SerializableTarget[];
	mode: SelectMode;
	onUpdate: (data: SelectTargetsFormData) => Promise<void>;
}

const SelectTargetsForm = ({targets, mode, onUpdate}: Props) => {
	const [selection, setSelection] = useState<string[]>([]);
	const selectionUpdate = (key: string, value: boolean) => {
		if (selection.includes(key)) {
			if (!value) {
				setSelection(selection.filter(s => s !== key));
			}
		} else if (value) {
			setSelection([...selection, key]);
		}
	};

	useEffect(() => {
		void onUpdate({selection});
	}, [onUpdate, selection]);

	const onInput = (event: FormEvent<HTMLInputElement>): void => {
		const target = event.target as HTMLInputElement;
		selectionUpdate(target.value, target.checked);
	};

	const renderCheck = (value: string) => (
		<Form.Check id={'selection+' + value} type="checkbox" value={value} onInput={onInput}/>
	);

	const renderTarget = (target: SerializableTarget, mode: SelectMode) => (
		<Fragment key={target.uuid}>
			<SelectTargetsFormTarget target={target}>
				{selection => mode?.startsWith('target') ? renderCheck(selection) : ''}
			</SelectTargetsFormTarget>
			<tr>
				<td/>
				<td colSpan={3} className="p-0">
					<SelectTargetsFormDisks target={target}>
						{selection => mode?.endsWith('disk') ? renderCheck(selection) : ''}
					</SelectTargetsFormDisks>
				</td>
			</tr>
		</Fragment>
	);

	return (
		<Form>
			<Table>
				<thead>
					<tr>
						<th className={styles.colCheck}/>
						<th>Target</th>
						<th>Access</th>
						<th>UUID</th>
					</tr>
				</thead>
				<tbody>
					{targets.map(target => renderTarget(target, mode))}
				</tbody>
			</Table>
		</Form>
	);
};

export default SelectTargetsForm;
