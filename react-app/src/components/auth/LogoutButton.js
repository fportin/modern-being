import React from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";

import "../NavBar/NavBar.css"

const LogoutButton = () => {
  const dispatch = useDispatch();
  const onLogout = async (e) => {
    dispatch(logout());
  };

  return <div className="logout-btn" onClick={onLogout}>Logout</div>;
};

export default LogoutButton;
