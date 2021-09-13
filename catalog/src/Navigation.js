import React, { useState } from 'react';
import config from "./config";
import logo from "./logo.png";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,

} from 'reactstrap';



const Navigation = (props) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => setIsOpen(!isOpen);

  let imgLogo = null;
  if (config.logo === "default") {
      imgLogo = logo
  } else {
      imgLogo = config.logo
  }

  let styleNav = {"backgroundColor":config.colorB}

  let pref = ""

  console.log(config.basePath)

  if ("basePath" in config) {
    pref = config.basePath
  }


  return (
    <div>
      <Navbar style={styleNav} dark expand="md">
        <NavbarBrand href={pref}><img src={imgLogo} alt="logo" />{config.brand}</NavbarBrand>
        <NavbarToggler onClick={toggle} />
        <Collapse isOpen={isOpen} navbar>
          <Nav className="mr-auto" navbar>
            <NavItem>
              <NavLink href={pref + "/"}>Resources</NavLink>
            </NavItem>  
            <NavItem>
              <NavLink href={pref + "/providers"}>Providers</NavLink>
            </NavItem>
          </Nav>
          { (!!config.externalLink && !!config.externalLinkTitle) &&
            <Nav navbar>
              <NavItem>
                <NavLink href={config.externalLink} target="_blank" rel="noreferrer noopener">
                  <FontAwesomeIcon className="mr-2" icon="link" />{config.externalLinkTitle}
                </NavLink>
              </NavItem>
            </Nav>
          }
        </Collapse>
      </Navbar>
    </div>
  );
}

export default Navigation;