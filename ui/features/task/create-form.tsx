import {useEffect} from 'react';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import {useForm} from 'react-hook-form';

export interface CreateTaskFormData {
	target: string;
	task: string;
	collectDiskSelectorPath: string;
}

interface Props {
	onSubmit: (data: CreateTaskFormData) => Promise<void>;
}

const CreateTaskForm = ({onSubmit}: Props) => {
	const {register, handleSubmit, watch, reset, formState: {isSubmitSuccessful}} = useForm<CreateTaskFormData>();
	const task = watch('task');

	useEffect(() => {
		if (isSubmitSuccessful) {
			reset();
		}
	}, [isSubmitSuccessful, reset]);

	const renderCollectDisk = (
		<Row>
			<Form.Group as={Col} className="mb-3" controlId="task-collect-disk-selector-path">
				<Form.Label>Disk Path</Form.Label>
				<Form.Control required type="text" placeholder="/dev/vda" {...register('collectDiskSelectorPath')}/>
			</Form.Group>
		</Row>
	);

	const renderTask: Record<string, JSX.Element> = {
		collectDisk: renderCollectDisk,
	};

	return (
		<Form onSubmit={handleSubmit(onSubmit)}>
			<Row>
				<Form.Group as={Col} className="mb-3" controlId="task-target">
					<Form.Label>Target</Form.Label>
					<Form.Control required className="font-monospace" type="text" placeholder="00000000-0000-0000-0000-000000000000" {...register('target')}/>
				</Form.Group>
				<Form.Group as={Col} className="mb-3" controlId="task-task">
					<Form.Label>Task</Form.Label>
					<div className="py-1">
						<Form.Check inline required type="radio" id="task-collect-disk" label="Collect Disk" value="collectDisk" {...register('task')}/>
						<Form.Check inline required type="radio" id="task-collect-memory" label="Collect Memory" value="collectMemory" {...register('task')}/>
					</div>
				</Form.Group>
			</Row>
			{renderTask[task]}
			<Row>
				<Col className="mb-3">
					<Button type="submit" variant="primary">
						Create
					</Button>
				</Col>
			</Row>
		</Form>
	);
};

export default CreateTaskForm;
