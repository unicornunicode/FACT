import {useState, useEffect, Fragment} from 'react';
import type {FormEvent} from 'react';
import Table from 'react-bootstrap/Table';
import Form from 'react-bootstrap/Form';

import SelectFormTarget from './select-form-target';
import Disks from './disks';
import styles from './select-form.module.css';
import type {SerializableTarget} from '.';

export interface SelectFormData {
	selection: string[];
}

type SelectMode = null | 'target' | 'target+disk' | 'disk';

interface Props {
	targets: SerializableTarget[] | null;
	mode: SelectMode;
	onUpdate: (data: SelectFormData) => Promise<void>;
}

const SelectForm = ({targets, mode, onUpdate}: Props) => {
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
			<SelectFormTarget target={target} checkbox={selection => mode?.startsWith('target') ? renderCheck(selection) : ''}/>
			<tr>
				<td/>
				<td colSpan={3} className="p-0">
					<Disks target={target} checkbox={selection => mode?.endsWith('disk') ? renderCheck(selection) : ''}/>
				</td>
			</tr>
		</Fragment>
	);

	const renderTargets = (targets: SerializableTarget[] | null) => {
		if (targets === null) {
			return (
				<tr>
					<td colSpan={3} className="p-2 text-center fst-italic text-muted">
						Loading
					</td>
				</tr>
			);
		}

		if (targets.length === 0) {
			return (
				<tr>
					<td colSpan={3} className="p-2 text-center fst-italic">
						No known targets. Add one
					</td>
				</tr>
			);
		}

		return targets.map(target => renderTarget(target, mode));
	};

	return (
		<Form>
			<Table>
				<thead>
					<tr>
						<th className={styles.colCheck}/>
						<th>Target</th>
						<th className={styles.colUUID}>UUID</th>
					</tr>
				</thead>
				<tbody>{renderTargets(targets)}</tbody>
			</Table>
		</Form>
	);
};

export default SelectForm;
