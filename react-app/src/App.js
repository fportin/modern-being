import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import NavBar from "./components/NavBar";
import FrontPage from "./components/FrontPage";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import UsersList from "./components/UsersList";
import User from "./components/User";
import CategoryPage from "./components/CategoryPage";
import ProductPage from "./components/ProductPage";
import ShoppingCartPage from "./components/ShoppingCartPage";
import { authenticate } from "./store/session";

function App() {
  const user = useSelector(state => state.session.user)
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, []);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar />
      <Switch>
        <Route path="/" exact={true}>
          <FrontPage />
        </Route>
        <Route path="/login" exact={true}>
          <LoginForm />
        </Route>
        <Route path="/sign-up" exact={true}>
          <SignUpForm />
        </Route>
        <Route path="/categories/:categoryId" exact={true}>
          <CategoryPage />
        </Route>
        <Route path="/products/:productId" exact={true}>
          <ProductPage />
        </Route>
        <Route path="/cart" exact={true}>
          <ShoppingCartPage />
        </Route>
        <ProtectedRoute path="/users" exact={true} >
          <UsersList/>
        </ProtectedRoute>
        <ProtectedRoute path="/users/:userId" exact={true} >
          <User />
        </ProtectedRoute>
        {/* <ProtectedRoute path="/cart" exact={true} >
          <h1>My Cart Page</h1>
        </ProtectedRoute> */}
      </Switch>
    </BrowserRouter>
  );
}

export default App;
