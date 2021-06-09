import React, { useState, useEffect } from "react"
import { useParams, useHistory } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";

import * as productActions from "../../store/products"
import CartProductTile from "../CartProductTile"
import "./ShoppingCartPage.css"

function ShoppingCartPage() {
    const dispatch = useDispatch();
    const cartProducts = useSelector((state) => state.products.cartProducts);
    const [totalPrice, setTotalPrice] = useState(0);

    useEffect(() => {
        const currentCart = JSON.parse(localStorage.getItem('cart'))
        const productsArr = []
        for (const productId in currentCart) {
            productsArr.push(parseInt(productId))
        }
        dispatch(productActions.getCartProducts(productsArr))
    }, [dispatch])

    const items = JSON.parse(localStorage.getItem('cart'))
    // console.log(items)

    return (
        <div className="shopping-cart-page__container">
            <h1>Cart</h1>
            <CartProductTile />
        </div>
    )
}

export default ShoppingCartPage;