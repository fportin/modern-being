import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, Redirect } from "react-router-dom";

import * as productActions from "../../store/products";
import './ProductTile.css';

function ProductTile() {
    const dispatch = useDispatch();
    const history = useHistory();
    const allProducts = useSelector((state) => state.products.allProducts);
    const sessionUser = useSelector((state) => state.session.user);
    // const allReviews = useSelector((state) => state.reviews.allReviews);
    // const [errors, setErrors] = useState([]);


    // useEffect(() => {
    //     dispatch(productActions.getProducts())
    // }, [dispatch]);

    const handleAdd = productId => (e) => {
        e.preventDefault()
        const currentCart = localStorage.getItem('cart')
        let quantity = 1
        let data = { [productId]: quantity }
        if (currentCart) {
            data = JSON.parse(currentCart)
            // dispatch(productActions.getCartProducts(data))
            if (data[`${productId}`]) {
                if (data[`${productId}`] < 10) {
                    data[`${productId}`] += 1
                } else {
                    alert("Order limit per item is 10.")
                }
            } else {
                data[`${productId}`] = quantity
            }
            localStorage.setItem('cart', JSON.stringify(data))
        } else {
            localStorage.setItem('cart', JSON.stringify(data))
        }
        history.push('/cart')
    }

    const handleClick = productId => (e) => {
        e.preventDefault();
        history.push(`/products/${productId}`)
    }

    if (allProducts) {
        const availableProducts = allProducts.matchingProducts
        if (availableProducts.length === 0) {
            return <h1>Sorry! There are no matches.</h1>

        } else if (availableProducts) {

            return (
                <>
                    {availableProducts?.map(product => {
                        return (
                            <div key={product.id} className="product-tile__container">
                                <div className='product-tile-photo' style={{ backgroundImage: `url(${product.photo})` }} onClick={handleClick(product.id)}></div>
                                <div className="product-tile-text">
                                    <div className='product-tile-name' onClick={handleClick(product.id)}>{product.name}</div>
                                    <div className='product-tile-brand'>{product.brand}</div>
                                    <div className='product-tile-price'>${product.price.toFixed(2)}</div>
                                    <button type="submit" onClick={handleAdd(product.id)}>Add to Cart</button>
                                </div>
                            </div>
                        )
                    })}
    
                </>
    
            )
        }

    }



    return (<></>);
}



export default ProductTile;