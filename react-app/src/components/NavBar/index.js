import React, {useEffect, useState} from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector, useDispatch } from "react-redux";
import LogoutButton from '../auth/LogoutButton';
import SearchBar from "../SearchBar"

import banner from "../../images/modern-being-name-black.png"
import "./NavBar.css";

const NavBar = () => {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user)
  const cartProducts = useSelector((state) => state.products.cartProducts);
  const [searchBarActive, setSearchBarActive] = useState(false);
  // const [itemQty, setItemQty] = useState(0)

  // useEffect(() => {
    
  //   if (!currentCart) {
  //     return
  //   }
    
  //   setItemQty(cartProducts?.qty)
  // }, [dispatch, itemQty])

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
        <NavLink to="/login" exact={true} className='login-nav'>
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
        {!searchBarActive ? 
        <> 
          <NavLink to='/categories/11' className='computing-nav' style={{ textDecoration: 'none' }}>Computing</NavLink>
          <NavLink to='/categories/12' className='mobile-nav' style={{ textDecoration: 'none' }}>Mobile</NavLink>
          <NavLink to='/categories/13' className='wearable-nav' style={{ textDecoration: 'none' }}>Wearables</NavLink>
          <NavLink to='/categories/14' className='audio-nav' style={{ textDecoration: 'none' }}>Audio</NavLink>
        </> 
        : null
        }
        <SearchBar search={setSearchBarActive}/>
        <NavLink to='/cart' className='cart-nav' style={{ textDecoration: 'none' }}>Cart({cartProducts ? cartProducts.qty : null})</NavLink>
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
