import type {UrlObject} from 'url';
import Link from 'next/link';

interface Props {
	uuid: string;
	href?: string | UrlObject;
}

const Uuid = ({uuid, href}: Props) => {
	if (href === undefined) {
		return <small className="text-muted">{uuid}</small>;
	}

	return <small className="text-muted"><Link href={href}>{uuid}</Link></small>;
};

export default Uuid;
