import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory } from "react-router-dom";

import * as productActions from "../../store/products";
import ReviewTile from "../ReviewTile"
import './ProductPage.css';

function ProductPage() {
    const dispatch = useDispatch();
    const { productId } = useParams();
    const currentProduct = useSelector((state) => state.products.product);
    // const sessionUser = useSelector((state) => state.session.user);
    const history = useHistory();


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
        history.push('/cart')
    }

    if (currentProduct) {
        const formattedPrice = currentProduct.price.toFixed(2)
        return (
            <div className='product-page'>
                <div className='product-page__container'>
                    <img src={`${currentProduct.photo}`} alt='item' className='product-photo' />
                    <div className="product-details__container">
                        <h1 className='product-name'>{currentProduct.name}</h1>
                        <h4 className='product-brand'>Brand: {currentProduct.brand}</h4>
                        <h4 className='product-price'>${formattedPrice}</h4>
                        <p className='product-description'>{currentProduct.description}</p>
                        <button type="submit" onClick={handleAdd(currentProduct.id)}>Add to Cart</button>
                    </div>
                </div>
                <ReviewTile />
            </div>
        );
    }
    return (<></>);

}

export default ProductPage;