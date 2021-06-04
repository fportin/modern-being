import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux"
import { Redirect } from 'react-router-dom';
import { signUp } from '../../store/session';

import "./SignUpForm.css";

const SignUpForm = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const data = await dispatch(signUp(username, email, password));
      if (data.errors) {
        setErrors(data.errors);
      }
    }
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <div className="signup-page__container">
      <form className="signup-form__container" onSubmit={onSignUp}>
        <div className="signup-page__greeting">Create your MB Account.</div>
        <div className="signup-page__errors">
          {errors.map((error) => (
            <div key={error}>{error}</div>
          ))}
        </div>
        <div className="signup-username-input-container">
          <input
            type="text"
            name="username"
            placeholder="Name"
            onChange={updateUsername}
            value={username}
            required={true}
            className="name-signup-input"
          ></input>
          <label className="name-signup-label">Name</label>
        </div>
        <div className="signup-email-input-container">
          <input
            type="email"
            name="email"
            placeholder="Email"
            onChange={updateEmail}
            value={email}
            required={true}
            className="email-signup-input"
          ></input>
          <label className="email-signup-label">Email</label>
        </div>
        <div className="signup-password-input-container">
          <input
            type="password"
            name="password"
            placeholder="Password"
            onChange={updatePassword}
            value={password}
            required={true}
            className="password-signup-input"
          ></input>
          <label className="password-signup-label">Password</label>
        </div>
        <div className="signup-repeat_password-input-container">
          <input
            type="password"
            name="repeat_password"
            placeholder="Confirm Password"
            onChange={updateRepeatPassword}
            value={repeatPassword}
            required={true}
            className="repeat_password-signup-input"
          ></input>
          <label className="repeat_password-signup-label">Confirm Password</label>
        </div>
        <button type="submit" className="signup-btn">Sign Up</button>
      </form>
    </div>
  );
};

export default SignUpForm;
