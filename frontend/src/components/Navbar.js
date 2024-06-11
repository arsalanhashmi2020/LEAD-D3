import React from 'react';
import { Navbar, Nav } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';

const NavigationBar = () => {
  return (
    <Navbar bg="dark" variant="dark" expand="lg">
      <Navbar.Brand href="/">LUMS Datalab</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="ml-auto">
          <LinkContainer to="/admin">
            <Nav.Link>Admin</Nav.Link>
          </LinkContainer>
          <LinkContainer to="/visualize">
            <Nav.Link>Visualize</Nav.Link>
          </LinkContainer>
          <LinkContainer to="/datasets">
            <Nav.Link>Datasets</Nav.Link>
          </LinkContainer>
          <LinkContainer to="/analysis">
            <Nav.Link>Analysis</Nav.Link>
          </LinkContainer>
          <LinkContainer to="/about">
            <Nav.Link>About Us</Nav.Link>
          </LinkContainer>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
};

export default NavigationBar;
