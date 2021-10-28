import {useEffect, Fragment} from 'react';
import Table from 'react-bootstrap/Table';
import Form from 'react-bootstrap/Form';
import {useForm} from 'react-hook-form';

import type {SerializableTarget} from '.';

export interface SelectTargetsFormData {
	selection: string[];
}

type SelectMode = null | 'target' | 'target+disk';

interface Props {
	targets: SerializableTarget[];
	mode: SelectMode;
	onSubmit: (data: SelectTargetsFormData) => Promise<void>;
	children: JSX.Element[] | JSX.Element;
}

const renderAccess = ({ssh}: SerializableTarget) => {
	if (ssh) {
		return (
			<span>SSH: {ssh.user}@{ssh.host}:{ssh.port}{ssh.become ? <>, with <code>sudo</code></> : ''}
			</span>
		);
	}

	return <span>Invalid</span>;
};

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
			<tr>
				<th>{mode?.startsWith('target') ? renderCheck(target.uuid) : ''}</th>
				<td>{target.name}</td>
				<td>{target.uuid}</td>
				<td>{renderAccess(target)}</td>
			</tr>
		</Fragment>
	);

	return (
		<Form onSubmit={handleSubmit(onSubmit)}>
			{children}
			<Table>
				<thead>
					<tr>
						<th/>
						<th>Name</th>
						<th>UUID</th>
						<th>Access</th>
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
