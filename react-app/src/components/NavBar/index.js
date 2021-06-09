import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from "react-redux";
import LogoutButton from '../auth/LogoutButton';

import banner from "../../images/modern-being-name-black.png"
import "./NavBar.css";

const NavBar = () => {
  const sessionUser = useSelector((state) => state.session.user)

  let sessionLinks;
  if (sessionUser) {
    sessionLinks = (
      <> 
        <LogoutButton />
      </>
    )
  } else {
    sessionLinks = (
      <>
        <NavLink to="/login" exact={true} activeClassName="active">
          Login
        </NavLink>
      </>
    )
  }

  return (
    <>
      <nav className="navbar__container">
        <NavLink to="/" className="nav-banner__container">
          <img src={banner} alt="Modern-Being banner" />
        </NavLink>
        <NavLink to='/categories/11' className='computing-nav' style={{ textDecoration: 'none' }}>Computing</NavLink>
        <NavLink to='/categories/12' className='mobile-nav' style={{ textDecoration: 'none' }}>Mobile</NavLink>
        <NavLink to='/categories/13' className='wearable-nav' style={{ textDecoration: 'none' }}>Wearables</NavLink>
        <NavLink to='/categories/14' className='audio-nav' style={{ textDecoration: 'none' }}>Audio</NavLink>
        {sessionLinks}
        {/* <ul>
          <li>
            <NavLink to="/users" exact={true} activeClassName="active">
              Users
            </NavLink>
          </li>
        </ul> */}
        
      </nav>
      <div className="subbar__container"></div>

    </>
  );
}

export default NavBar;
