import {useState, useCallback} from 'react';
import Button from 'react-bootstrap/Button';
import {parse as parseUuid} from 'uuid';

import {ManagementClientImpl} from '../../proto/fact/management';
import {managementRpc} from '../grpc';

import SelectTargetsForm from './select-form';
import type {SelectTargetsFormData} from './select-form';
import type {SerializableTarget} from '.';

interface Props {
	targets: SerializableTarget[];
	onShowAddTarget: () => Promise<void>;
}

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

const SelectTargets = ({targets, onShowAddTarget}: Props) => {
	const [targetSelection, setTargetSelection] = useState<Array<{target: string}>>([]);
	const [diskSelection, setDiskSelection] = useState<Array<{target: string; disk: string}>>([]);
	const [canScanDisks, setCanScanDisks] = useState(false);
	const [canCaptureDisks, setCanCaptureDisks] = useState(false);
	const [canCaptureMemory, setCanCaptureMemory] = useState(false);

	const onSelectionUpdate = useCallback(async (data: SelectTargetsFormData) => {
		let selection = data.selection;
		if (!Array.isArray(selection)) {
			selection = [selection];
		}

		// Parse out targets or disks
		const targets: Array<{target: string}> = [];
		const disks: Array<{target: string; disk: string}> = [];
		for (const s of selection) {
			const map = parseSelection(s);
			if ('disk' in map && 'target' in map) {
				disks.push(map as unknown as DiskSel);
			} else if ('target' in map) {
				targets.push(map as unknown as TargetSel);
			}
		}

		setTargetSelection(targets);
		setDiskSelection(disks);

		setCanScanDisks(targets.length > 0 && disks.length === 0);
		setCanCaptureDisks(targets.length === 0 && disks.length > 0);
		setCanCaptureMemory(targets.length > 0 && disks.length === 0);
	}, []);

	const onScanDisks = useCallback(async () => {
		const rpc = await managementRpc();
		const client = new ManagementClientImpl(rpc);
		for (const {target} of targetSelection) {
			// eslint-disable-next-line no-await-in-loop
			await client.CreateTask({
				target: new Uint8Array(parseUuid(target)),
				taskCollectLsblk: {},
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
					selector: {
						path: disk,
					},
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

	return (
		<>
			<div className="d-flex gap-2 py-2">
				<Button className="me-auto" onClick={onShowAddTarget}>Add target</Button>
				<Button disabled={!canScanDisks} onClick={onScanDisks}>Scan disks</Button>
				<Button disabled={!canCaptureDisks} onClick={onCaptureDisks}>Capture disks</Button>
				<Button disabled={!canCaptureMemory} onClick={onCaptureMemory}>Capture memory</Button>
			</div>
			<SelectTargetsForm targets={targets} mode="target+disk" onUpdate={onSelectionUpdate}/>
		</>
	);
};

export default SelectTargets;
