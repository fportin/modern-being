import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";

import * as productActions from "../../store/products";
import ReviewTile from "../ReviewTile"
import './ProductPage.css';

function ProductPage() {
    const dispatch = useDispatch();
    const { productId } = useParams();
    const currentProduct = useSelector((state) => state.products.product);


    useEffect(() => {
        dispatch(productActions.getProduct(productId))
    }, [productId, dispatch]);

    const handleAdd = productId => (e) => {
        e.preventDefault()
        const currentCart = localStorage.getItem('cart')
        let quantity = 1
        let data = {[productId]: quantity}
        if (currentCart) {
            data = JSON.parse(currentCart)
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
        const newCart = JSON.parse(localStorage.getItem('cart'))
        dispatch(productActions.getCartProducts(newCart))
    }

    if (currentProduct) {
        const formattedPrice = currentProduct.price.toFixed(2)
        return (
            <div className='product-page'>
                <div className='product-page__container'>
                    <div style={{ backgroundImage: `url(${currentProduct.photo})` }} className='product-photo' />
                    <div className="product-details__container">
                        <div className='product-name'>{currentProduct.name}</div>
                        <div className='product-brand'>Brand: <span className="product-brand-name">{currentProduct.brand}</span></div>
                        <h3 className='product-price'>${formattedPrice}</h3>
                        <p className='product-description'>{currentProduct.description}</p>
                        <button type="submit" onClick={handleAdd(currentProduct.id)} className="product-page-add-btn">Add to Cart</button>
                    </div>
                </div>
                <div className="product-page-reviews__container">
                    <ReviewTile />
                </div>
            </div>
        );
    }
    return (<></>);

}

export default ProductPage;