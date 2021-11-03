import {useState, useCallback} from 'react';
import Button from 'react-bootstrap/Button';
import {parse as parseUuid} from 'uuid';

import {ManagementClientImpl} from '../../proto/fact/management';
import {managementRpc} from '../grpc';

import SelectForm from './select-form';
import type {SelectFormData} from './select-form';
import type {SerializableTarget} from '.';

interface Props {
	targets: SerializableTarget[];
	onShowAddTarget: () => Promise<void>;
}

const splitSelection = (s: string[]): string[] => s.flatMap(v => v.split(','));

const parseSelection = (s: string): Record<string, string> => {
	const parts = s.split(/\+/);
	const sel: Record<string, string> = {};
	for (const part of parts) {
		const [key, value] = part.split(/\./);
		sel[key] = value;
	}

	return sel;
};

interface TargetSel {
	target: string;
}

interface DiskSel {
	target: string;
	disk: string;
}

interface TaskSel {
	task: string;
}

const renderCount = (s: string, items: unknown[]): JSX.Element => {
	if (items.length === 0) {
		return <span>{s}</span>;
	}

	return <span>{s} ({items.length})</span>;
};

const Select = ({targets, onShowAddTarget}: Props) => {
	const [targetSelection, setTargetSelection] = useState<TargetSel[]>([]);
	const [diskSelection, setDiskSelection] = useState<DiskSel[]>([]);
	const [taskSelection, setTaskSelection] = useState<TaskSel[]>([]);
	const [canScanDisks, setCanScanDisks] = useState(false);
	const [canCaptureDisks, setCanCaptureDisks] = useState(false);
	const [canCaptureMemory, setCanCaptureMemory] = useState(false);
	const [canIngest, setCanIngest] = useState(false);

	const onSelectionUpdate = useCallback(async (data: SelectFormData) => {
		let selection = data.selection;
		if (!Array.isArray(selection)) {
			selection = [selection];
		}

		// Parse out targets or disks
		const targets: TargetSel[] = [];
		const disks: DiskSel[] = [];
		const tasks: TaskSel[] = [];
		for (const s of splitSelection(selection)) {
			const map = parseSelection(s);
			if ('disk' in map && 'target' in map) {
				disks.push(map as unknown as DiskSel);
			} else if ('target' in map) {
				targets.push(map as unknown as TargetSel);
			} else if ('task' in map) {
				tasks.push(map as unknown as TaskSel);
			}
		}

		setTargetSelection(targets);
		setDiskSelection(disks);
		setTaskSelection(tasks);

		setCanScanDisks(targets.length > 0 && disks.length === 0);
		setCanCaptureDisks(targets.length === 0 && disks.length > 0);
		setCanCaptureMemory(targets.length > 0 && disks.length === 0);
		setCanIngest(tasks.length > 0);
	}, []);

	const onScanDisks = useCallback(async () => {
		const rpc = await managementRpc();
		const client = new ManagementClientImpl(rpc);
		for (const {target} of targetSelection) {
			// eslint-disable-next-line no-await-in-loop
			await client.CreateTask({
				target: new Uint8Array(parseUuid(target)),
				taskCollectDiskinfo: {},
			});
		}
	}, [targetSelection]);

	const onCaptureDisks = useCallback(async () => {
		const rpc = await managementRpc();
		const client = new ManagementClientImpl(rpc);
		for (const {target, disk} of diskSelection) {
			// eslint-disable-next-line no-await-in-loop
			await client.CreateTask({
				target: new Uint8Array(parseUuid(target)),
				taskCollectDisk: {
					deviceName: disk,
				},
			});
		}
	}, [diskSelection]);

	const onCaptureMemory = useCallback(async () => {
		const rpc = await managementRpc();
		const client = new ManagementClientImpl(rpc);
		for (const {target} of targetSelection) {
			// eslint-disable-next-line no-await-in-loop
			await client.CreateTask({
				target: new Uint8Array(parseUuid(target)),
				taskCollectMemory: {},
			});
		}
	}, [targetSelection]);

	const onIngest = useCallback(async () => {
		const rpc = await managementRpc();
		const client = new ManagementClientImpl(rpc);
		for (const {task} of taskSelection) {
			// eslint-disable-next-line no-await-in-loop
			await client.CreateTask({
				taskIngest: {
					collectedUuid: new Uint8Array(parseUuid(task)),
				},
			});
		}
	}, [taskSelection]);

	return (
		<>
			<div className="d-flex gap-2 py-2">
				<Button className="me-auto" onClick={onShowAddTarget}>Add target</Button>
				<Button disabled={!canScanDisks} onClick={onScanDisks}>{renderCount('Scan disks', targetSelection)}</Button>
				<Button disabled={!canCaptureDisks} onClick={onCaptureDisks}>{renderCount('Capture disks', diskSelection)}</Button>
				<Button disabled={!canCaptureMemory} onClick={onCaptureMemory}>{renderCount('Capture memory', targetSelection)}</Button>
				<Button disabled={!canIngest} onClick={onIngest}>{renderCount('Run ingestion', taskSelection)}</Button>
			</div>
			<SelectForm targets={targets} mode="target+disk+task" onUpdate={onSelectionUpdate}/>
		</>
	);
};

export default Select;
