import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Redirect, NavLink, useHistory } from "react-router-dom";
import { login } from "../../store/session";

import logo from "../../images/modern-being-logo.png"
import "./LoginForm.css";

const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();
  const history = useHistory()

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data.errors) {
      setErrors(data.errors);
    } else {
      history.goBack();
    }
  };

  const demoLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login("demo@aa.io", "password"));
    if (data.errors) {
      setErrors(data.errors);
    } else {
      history.goBack();
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <div className="login-page__container">
      <form className="login-form__container" onSubmit={onLogin}>
        <div className="login-logo__container" style={{ backgroundImage: `url(${logo})` }}>
        </div>
        <div className="login-page__greeting">Please sign in to your Account.</div>
        <div className="login-page__errors">
          {errors.map((error) => (
            <div key={error}>{error}</div>
          ))}
        </div>
        <div className="email-input-container">
          <input
            name="email"
            type="text"
            placeholder="Email"
            value={email}
            onChange={updateEmail}
            className="email-login-input"
          />
          <label htmlFor="email" className="email-login-label" >Email</label>
        </div>
        <div className="password-input-container">
          <input
            name="password"
            type="password"
            placeholder="Password"
            value={password}
            onChange={updatePassword}
            className="password-login-input"
          />
          <label htmlFor="password" className="password-login-label">Password</label>
        </div>
          <button type="submit" className="login-btn">Login</button>
          <button type="submit" className="demo-btn" onClick={demoLogin}>Demo User</button>
        <NavLink to="/sign-up" exact={true} className="sign-up-link">
          Create an Account
        </NavLink>
      </form>
    </div>
  );
};

export default LoginForm;
