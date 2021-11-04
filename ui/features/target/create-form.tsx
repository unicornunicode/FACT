import {useEffect} from 'react';
import clsx from 'clsx';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';
import {useForm} from 'react-hook-form';

import styles from './create-form.module.css';

export interface CreateFormData {
	name: string;
	access: string;
	sshUser: string;
	sshHost: string;
	sshPort: number;
	sshPrivateKey: string;
	sshBecome: boolean;
	sshBecomePassword: string;
}

interface Props {
	onSubmit: (data: CreateFormData) => Promise<void>;
	modal: boolean;
	modalShow: boolean;
	onModalClose: () => void;
}

const sshPrivateKeyPlaceholder = '-----BEGIN OPENSSH PRIVATE KEY-----\naGVoZSB5b3UgZm91bmQgdGhpcyBtZXNzYWdlLCBncmVhdCBqb2I...';

const CreateForm = ({onSubmit, modal, modalShow, onModalClose}: Props) => {
	const {register, handleSubmit, watch, reset, formState: {isSubmitSuccessful}} = useForm<CreateFormData>({
		defaultValues: {
			sshPort: 22,
			sshBecome: true,
		},
	});
	const access = watch('access');
	const sshUser = watch('sshUser');
	// eslint-disable-next-line @typescript-eslint/naming-convention
	const sshBecome = watch('sshBecome');

	useEffect(() => {
		if (isSubmitSuccessful) {
			reset({sshHost: ''});
		}
	}, [isSubmitSuccessful, reset]);

	const renderSsh = (
		<>
			<Row>
				<Form.Group as={Col} className="mb-3" controlId="target-ssh-userhostport">
					<Form.Label>SSH Host</Form.Label>
					<InputGroup>
						<Form.Control required type="text" placeholder="user" {...register('sshUser')}/>
						<InputGroup.Text>@</InputGroup.Text>
						<Form.Control required type="text" placeholder="host.domain" {...register('sshHost')}/>
						<Form.Control required className={clsx('flex-grow-0', styles.sshPort)} min="1" max="65535" type="number" placeholder="port" {...register('sshPort')}/>
					</InputGroup>
				</Form.Group>
			</Row>
			<Row>
				<Form.Group as={Col} className="mb-3" controlId="target-ssh-privatekey">
					<Form.Label>SSH Private Key</Form.Label>
					<Form.Control required className="font-monospace" as="textarea" rows={3} {...register('sshPrivateKey')} placeholder={sshPrivateKeyPlaceholder}/>
				</Form.Group>
			</Row>
			<Row>
				<Form.Group as={Col} className="mb-3" controlId="target-become">
					<Form.Label>Use <code>sudo</code></Form.Label>
					<InputGroup>
						<InputGroup.Text>
							<Form.Check.Input id="target-ssh-become" type="checkbox" aria-label="Use sudo for privilege escalation" {...register('sshBecome')}/>
						</InputGroup.Text>
						<Form.Control required type="text" placeholder="(sudo password currently ignored)" disabled={!sshBecome} {...register('sshBecomePassword')}/>
					</InputGroup>
					{sshUser !== 'root' && !sshBecome ? <Form.Text className="text-danger">You should enable <code>sudo</code> if you are using a non-root user</Form.Text> : ''}
					{sshUser === 'root' && sshBecome ? <Form.Text className="text-danger">You should not need to enable <code>sudo</code> if you are using the root user</Form.Text> : ''}
				</Form.Group>
			</Row>
		</>
	);

	const renderAccess: Record<string, JSX.Element> = {
		ssh: renderSsh,
	};

	const renderForm = () => (
		<>
			<Row>
				<Form.Group as={Col} className="mb-3" controlId="target-name">
					<Form.Label>Name</Form.Label>
					<Form.Control type="text" placeholder="" {...register('name')}/>
				</Form.Group>
				<Form.Group as={Col} className="mb-3" controlId="target-access">
					<Form.Label>Access method</Form.Label>
					<div className="py-1">
						<Form.Check inline required type="radio" id="target-access-ssh" label="SSH" value="ssh" {...register('access')}/>
					</div>
				</Form.Group>
			</Row>
			{renderAccess[access]}
			{modal ? '' : (
				<Row>
					<Col className="mb-3">
						<Button type="submit">
							Add
						</Button>
					</Col>
				</Row>
			)}
		</>
	);

	if (modal) {
		return (
			<Modal show={modalShow} size="lg" onHide={onModalClose}>
				<Form onSubmit={handleSubmit(onSubmit)}>
					<Modal.Header closeButton>
						<Modal.Title>Add target</Modal.Title>
					</Modal.Header>
					<Modal.Body>
						{renderForm()}
					</Modal.Body>
					<Modal.Footer>
						<Button variant="secondary" onClick={onModalClose}>
							Close
						</Button>
						<Button type="submit">
							Add
						</Button>
					</Modal.Footer>
				</Form>
			</Modal>
		);
	}

	return (
		<Form onSubmit={handleSubmit(onSubmit)}>
			{renderForm()}
		</Form>
	);
};

export default CreateForm;
