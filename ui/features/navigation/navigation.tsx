import Link from 'next/link';
import Image from 'next/image';
import {Container, Nav, Navbar} from 'react-bootstrap';

import logo from '../../public/logo.svg';
import styles from './navigation.module.css';

const Navigation = () => (
	<Navbar bg="dark" variant="dark">
		<Container fluid>
			<Navbar.Brand className={styles.brand}><Image src={logo} alt="FACT" width={91} height={30}/></Navbar.Brand>
			<Nav className="me-auto">
				<Link passHref href="/"><Nav.Link>Overview</Nav.Link></Link>
				<Link passHref href="/task"><Nav.Link>Tasks</Nav.Link></Link>
				<Link passHref href="/worker"><Nav.Link>Workers</Nav.Link></Link>
			</Nav>
		</Container>
	</Navbar>
);

export default Navigation;
