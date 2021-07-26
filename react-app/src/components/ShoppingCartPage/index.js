import React, { useState, useEffect } from "react"
import { useHistory } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";

import * as productActions from "../../store/products"
import CartProductTile from "../CartProductTile"
import "./ShoppingCartPage.css"

function ShoppingCartPage() {
    const dispatch = useDispatch();
    const history = useHistory()
    const cartProducts = useSelector((state) => state.products.cartProducts);
    const sessionUser = useSelector((state) => state.session.user);
    const [cart, updateCart] = useState({})
    const [emptyCart, setEmptyCart] = useState(false)


    useEffect(() => {
        const currentCart = JSON.parse(localStorage.getItem('cart'))
        if (!currentCart) {
            setEmptyCart(true)
        } else {
            setEmptyCart(false)
        }
        dispatch(productActions.getCartProducts(currentCart))
    }, [dispatch, cart])

    const handleEmpty = (e) => {
        localStorage.removeItem('cart')
        setEmptyCart(true)
        updateCart({})
    }

    const handleCheckout = cart => async(e) => {
        if (sessionUser) {
            localStorage.removeItem('cart')
            setEmptyCart(true)
            await updateCart({})
            history.push(`/users/${sessionUser.id}/order`)
        } else {
            history.push('/login')
        }
    }


    if (cartProducts && !emptyCart) {
        const formattedTotal = cartProducts.total.toFixed(2)
        
        
        return (
            <div className="shopping-cart-page__container">
                <div className="shopping-cart-page-title">Your Cart <button className="shopping-cart-page-empty-btn" type="button" onClick={handleEmpty}>Empty Cart</button></div>
                <CartProductTile change={updateCart} />
                <div className="shopping-cart-page-total">Total: ${formattedTotal}</div>
                <button className="shopping-cart-page-btn" type="submit" onClick={handleCheckout(cartProducts)}>Checkout</button>
            </div>
        )
    }

    return (
        <div className="shopping-cart-page__container">
            <h1>Your cart is empty</h1>
        </div>
    )
}

export default ShoppingCartPage;