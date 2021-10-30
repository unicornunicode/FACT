import Link from 'next/link';
import Image from 'next/image';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

import logo from '../../public/logo.svg';
import styles from './navigation.module.css';

const Navigation = () => (
	<Navbar bg="dark" variant="dark">
		<Container fluid>
			<Navbar.Brand className={styles.brand}><Image src={logo} alt="FACT" width={91} height={30}/></Navbar.Brand>
			<Nav className="me-auto">
				<Link passHref href="/"><Nav.Link>Dashboard</Nav.Link></Link>
				<Link passHref href="/target"><Nav.Link>Targets</Nav.Link></Link>
				<Link passHref href="/worker"><Nav.Link>Workers</Nav.Link></Link>
				<Link passHref href="/task"><Nav.Link>Task Log</Nav.Link></Link>
			</Nav>
		</Container>
	</Navbar>
);

export default Navigation;
