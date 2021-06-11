import React, { useState, useEffect } from "react"
import { useParams, useHistory } from "react-router-dom";
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
            return setEmptyCart(true)
        }
        setEmptyCart(false)
        dispatch(productActions.getCartProducts(currentCart))
    }, [dispatch, cart, emptyCart])

    const handleEmpty = (e) => {
        localStorage.removeItem('cart')
        setEmptyCart(true)
    }

    const handleCheckout = cart => (e) => {
        if (sessionUser) {
            localStorage.removeItem('cart')
            setEmptyCart(true)
            history.push(`/users/${sessionUser.id}/order`)
        } else {
            history.push('/login')
        }
    }


    if (cartProducts && !emptyCart) {
        const formattedTotal = cartProducts.total.toFixed(2)
        
        
        return (
            <div className="shopping-cart-page__container">
                <h1>Cart</h1>
                <CartProductTile change={updateCart} />
                <h1>Total: ${formattedTotal}</h1>
                <button type="submit" onClick={handleEmpty}>Empty Cart</button>
                <button type="submit" onClick={handleCheckout(cartProducts)}>Checkout</button>
            </div>
        )
    }

    return (<h1>Your cart is empty</h1>)
}

export default ShoppingCartPage;