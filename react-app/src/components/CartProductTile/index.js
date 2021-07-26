import React, { useState } from "react";
import { useSelector } from "react-redux";
import { useHistory } from "react-router-dom";

import './CartProductTile.css';

function CartProductTile({change}) {
    const history = useHistory();
    const cartProducts = useSelector((state) => state.products.cartProducts);
    const [quantity, setQuantity] = useState()
    const [target, setTarget] = useState(null);

    const handleClick = productId => (e) => {
        e.preventDefault();
        window.scrollTo(0, 0)
        history.push(`/products/${productId}`)
    }

    const handleQuantity = productId => (e) => {
        e.preventDefault();
        setTarget(productId)
        if (e.target.value >= 1 && e.target.value <= 10) {
            setQuantity(e.target.value)
            const currentCart = JSON.parse(localStorage.getItem('cart'))
            currentCart[`${productId}`] = parseInt(e.target.value)
            localStorage.setItem('cart', JSON.stringify(currentCart))
        }
        change({})

    }

    const handleRemove = productId => (e) => {
        e.preventDefault();
        const currentCart = JSON.parse(localStorage.getItem('cart'))
        delete currentCart[productId]
        if (Object.keys(currentCart).length < 1) {
            localStorage.removeItem('cart')
            return change({})
        }
        localStorage.setItem('cart', JSON.stringify(currentCart))
        change({})
        
    }

    if (cartProducts) {
        const addedProducts = cartProducts.matchingProducts
        return (
            <>
                {addedProducts?.map(product => {
                    return (
                        <div key={product.id} className='cart-product-tile__container' >
                            <div className='cart-product-photo' style={{ backgroundImage: `url(${product.photo})` }} onClick={handleClick(product.id)}></div>
                            <div className="cart-product-tile-text">
                                <div className="cart-product-tile-name" onClick={handleClick(product.id)}>{product.name}</div>
                                <div className="cart-product-tile-price">{product.price.toLocaleString('en-US', { style: 'currency', currency: 'USD' })}</div>
                                <label key={product.id} className="cart-product-tile-quantity-select">
                                    Quantity: 
                                        <select value={target === product.id ? quantity : product.quantity} onChange={handleQuantity(product.id)}>
                                        <option value="1">1</option>
                                        <option value="2">2</option>
                                        <option value="3">3</option>
                                        <option value="4">4</option>
                                        <option value="5">5</option>
                                        <option value="6">6</option>
                                        <option value="7">7</option>
                                        <option value="8">8</option>
                                        <option value="9">9</option>
                                        <option value="10">10</option>
                                    </select>
                                </label>
                                <div className="cart-product-tile-subtotal">Item Subtotal: {product.subtotal.toLocaleString('en-US', { style: 'currency', currency: 'USD' })}</div>
                                <button type="button" className="cart-product-tile-remove-btn" onClick={handleRemove(product.id)}>Remove</button>
                            </div>
                        </div>
                    )
                })}
                
            </>

        )

    }



    return (<></>);
}



export default CartProductTile;