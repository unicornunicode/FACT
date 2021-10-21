import clsx from 'clsx';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Button from 'react-bootstrap/Button';
import {useForm, Controller} from 'react-hook-form';
import type {SubmitHandler} from 'react-hook-form';

import styles from './create.module.css';

interface Inputs {
	name: string;
	access: string;
	ssh_user: string;
	ssh_host: string;
	ssh_port: number;
	ssh_private_key: string;
	ssh_become: boolean;
	ssh_become_password: string;
}

const CreateTarget = () => {
	const {register, control, handleSubmit, watch, formState: {errors}} = useForm<Inputs>();
	const access = watch('access');
	const sshUser = watch('ssh_user');
	// eslint-disable-next-line @typescript-eslint/naming-convention
	const sshBecome = watch('ssh_become');

	const onSubmit: SubmitHandler<Inputs> = data => {
		console.debug(data);
	};

	const renderSsh = (
		<>
			<Row>
				<Form.Group as={Col} className="mb-3" controlId="target-ssh-userhostport">
					<Form.Label>SSH Host</Form.Label>
					<InputGroup>
						<Form.Control required type="text" placeholder="user" {...register('ssh_user')}/>
						<InputGroup.Text>@</InputGroup.Text>
						<Form.Control required type="text" placeholder="host.domain" {...register('ssh_host')}/>
						<Form.Control required className={clsx('flex-grow-0', styles.sshPort)} min="1" max="65535" type="number" placeholder="port" {...register('ssh_port')}/>
						<Form.Text>{errors.ssh_user}{errors.ssh_host}{errors.ssh_port}</Form.Text>
					</InputGroup>
				</Form.Group>
			</Row>
			<Row>
				<Form.Group as={Col} className="mb-3" controlId="target-ssh-privatekey">
					<Form.Label>SSH Private Key</Form.Label>
					<Form.Control required as="textarea" rows={3} {...register('ssh_private_key')}/>
				</Form.Group>
			</Row>
			<Row>
				<Form.Group as={Col} className="mb-3" controlId="target-become">
					<Form.Label>Use <code>sudo</code></Form.Label>
					<InputGroup hasValidation>
						<Controller defaultValue name="ssh_become" control={control} render={({field}) => <InputGroup.Checkbox aria-label="Enable privilege escalation" {...field} ref={undefined}/>}/>
						<Form.Control required type="text" placeholder="sudo password" disabled={!sshBecome} {...register('ssh_become_password')}/>
					</InputGroup>
					{sshUser !== 'root' && !sshBecome ? <Form.Text className="text-danger">You should enable <code>sudo</code> if you are using a non-root user</Form.Text> : ''}
					{sshUser === 'root' && sshBecome ? <Form.Text className="text-danger">You should not need to enable <code>sudo</code> if you are using the root user</Form.Text> : ''}
				</Form.Group>
			</Row>
			<Row>
				<Col className="mb-3">
					<Button type="submit" variant="primary">
						Create
					</Button>
				</Col>
			</Row>
		</>
	);

	const renderAccess: Record<string, JSX.Element> = {
		ssh: renderSsh,
	};

	return (
		<Form onSubmit={handleSubmit(onSubmit)}>
			<Row>
				<Form.Group as={Col} className="mb-3" controlId="target-name">
					<Form.Label>Name</Form.Label>
					<Form.Control type="text" placeholder="" {...register('name')}/>
					<Form.Text>{errors.name}</Form.Text>
				</Form.Group>
				<Form.Group as={Col} className="mb-3" controlId="target-access">
					<Form.Label>Access method</Form.Label>
					<div className="py-1">
						<Form.Check inline label="SSH" value="ssh" type="radio" id="target-access-ssh" {...register('access')}/>
					</div>
					<Form.Text>{errors.access}</Form.Text>
				</Form.Group>
			</Row>
			{renderAccess[access]}
		</Form>
	);
};

export default CreateTarget;
