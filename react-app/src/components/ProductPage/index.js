import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";

import shaded from "../../images/shade-star.png"
import * as productActions from "../../store/products";
import ReviewTile from "../ReviewTile"
import './ProductPage.css';

function ProductPage() {
    const dispatch = useDispatch();
    const { productId } = useParams();
    const currentProduct = useSelector((state) => state.products.product);
    const [reviewSubmitted, setReviewSubmitted] = useState({})


    useEffect(() => {
        dispatch(productActions.getProduct(productId))
    }, [productId, dispatch, reviewSubmitted]);

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

    const reviewsLink = (e) => {
        e.preventDefault();
        window.scrollTo(0, 580)
    }

    if (currentProduct) {
        const formattedPrice = currentProduct.price.toLocaleString('en-US', { style: 'currency', currency: 'USD' })
        return (
            <div className='product-page'>
                <div className='product-page__container'>
                    <div style={{ backgroundImage: `url(${currentProduct.photo})` }} className='product-photo' />
                    <div className="product-details__container">
                        <div className='product-name'>{currentProduct.name}</div>
                        <div className='product-brand'>Brand: <span className="product-brand-name">{currentProduct.brand}</span></div>
                        <h3 className='product-price'>{formattedPrice}</h3>
                        <div className='product-rating'>{currentProduct.rating.toFixed(1)}<img className="star-icon" src={shaded} alt="Star Icon" />
                            <span className='product-rating-reviewers' onClick={reviewsLink}>({currentProduct.reviewers} Reviews)</span>
                        </div>
                        <p className='product-description'>{currentProduct.description}</p>
                        <button type="submit" onClick={handleAdd(currentProduct.id)} className="product-page-add-btn">Add to Cart</button>
                    </div>
                </div>
                <div className="product-page-reviews__container">
                    <ReviewTile submitted={setReviewSubmitted} />
                </div>
            </div>
        );
    }
    return (<></>);

}

export default ProductPage;