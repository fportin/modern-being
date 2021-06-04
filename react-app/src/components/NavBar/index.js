import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';

import banner from "../../images/modern-being-name-black.png"
import "./NavBar.css";

const NavBar = () => {
  return (
    <>
      <nav className="navbar__container">
        <NavLink to="/" className="nav-banner__container">
          <img src={banner} alt="Modern-Being banner" />
        </NavLink>
        <ul>
          {/* <li>
            <NavLink to="/" exact={true} activeClassName="active">
              Home
            </NavLink>
          </li> */}
          <li>
            <NavLink to="/login" exact={true} activeClassName="active">
              Login
            </NavLink>
          </li>
          {/* <li>
            <NavLink to="/users" exact={true} activeClassName="active">
              Users
            </NavLink>
          </li> */}
          <li>
            <LogoutButton />
          </li>
        </ul>
        
      </nav>
      <div className="subbar__container"></div>

    </>
  );
}

export default NavBar;
