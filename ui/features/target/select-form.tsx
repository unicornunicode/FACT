import {useEffect, Fragment} from 'react';
import Table from 'react-bootstrap/Table';
import Form from 'react-bootstrap/Form';
import {useForm} from 'react-hook-form';

import SelectTargetsFormTarget from './select-form-target';
import SelectTargetsFormDisks from './select-form-disks';
import {colCheck} from './select-form.module.css';
import type {SerializableTarget} from '.';

export interface SelectTargetsFormData {
	selection: string[];
}

type SelectMode = null | 'target' | 'target+disk' | 'disk';

interface Props {
	targets: SerializableTarget[];
	mode: SelectMode;
	onSubmit: (data: SelectTargetsFormData) => Promise<void>;
	children: JSX.Element[] | JSX.Element | string;
}

const SelectTargetsForm = ({targets, mode, onSubmit, children}: Props) => {
	const {register, handleSubmit, reset, formState: {isSubmitSuccessful}} = useForm<SelectTargetsFormData>();

	useEffect(() => {
		if (isSubmitSuccessful) {
			reset();
		}
	}, [isSubmitSuccessful, reset]);

	const renderCheck = (value: string) => (
		<Form.Check id={'selection+' + value} type="checkbox" value={value} aria-label="Use sudo for privilege escalation" {...register('selection')}/>
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
		<Form onSubmit={handleSubmit(onSubmit)}>
			{children}
			<Table>
				<thead>
					<tr>
						<th className={colCheck}/>
						<th>Target</th>
						<th>Access</th>
						<th>UUID</th>
					</tr>
				</thead>
				<tbody>
					{targets.filter((_, i) => i === 0).map(target => renderTarget(target, mode))}
				</tbody>
			</Table>
		</Form>
	);
};

export default SelectTargetsForm;
