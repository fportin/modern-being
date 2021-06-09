import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory } from "react-router-dom";

import * as productActions from "../../store/products";
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
        let quantity = 0
        let data = `{${productId}: ${quantity}}`
        if (currentCart) {
            data = JSON.parse(currentCart)
            console.log(data)
            let newData = data.data
            // console.log(data.data[`${productId}`])
            console.log("NEW", newData.productId)
            // localStorage.setItem('cart', JSON.stringify([JSON.parse(currentCart), `{${productId}: ${quantity}}`]))
        } else {
            quantity++
            // localStorage.setItem('cart', JSON.stringify(`{${productId}: ${quantity}}`))
            localStorage.setItem('cart', JSON.stringify({data: `{${productId}: ${quantity}}`}))
        }
    }

    if (currentProduct) {
        const formattedPrice = currentProduct.price.toFixed(2)
        return (
            <div className='product-page'>
                <div className='product-page__container'>
                    <h1 className='product-name'>{currentProduct.name}</h1>
                    <h4 className='product-brand'>Brand: {currentProduct.brand}</h4>
                    <img src={`https:${currentProduct.photo}`} alt='item' className='product-photo' />
                    <h4 className='product-price'>${formattedPrice}</h4>
                    <p className='product-description'>{currentProduct.description}</p>
                    <button type="submit" onClick={handleAdd(currentProduct.id)}>Add to Cart</button>
                </div>
            </div>
        );
    }
    return (<></>);

}

export default ProductPage;