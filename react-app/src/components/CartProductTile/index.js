import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, Redirect } from "react-router-dom";

import './CartProductTile.css';

function CartProductTile({change}) {
    const history = useHistory();
    const cartProducts = useSelector((state) => state.products.cartProducts);
    const sessionUser = useSelector((state) => state.session.user);
    const [quantity, setQuantity] = useState()
    const [target, setTarget] = useState(null);
    // const allReviews = useSelector((state) => state.reviews.allReviews);
    // const [errors, setErrors] = useState([]);
    

    const handleClick = productId => (e) => {
        e.preventDefault();
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
                        <div key={product.id} className='product-tile__container' >
                            <img src={`${product.photo}`} alt='item' className='cart-product-photo' onClick={handleClick(product.id)} />
                            <div onClick={handleClick(product.id)}>${product.name}</div>
                            <div>${product.price}</div>
                            <h1>${product.subtotal}</h1>
                            <input 
                                type="number" 
                                value={target === product.id ? quantity : product.quantity} 
                                onChange={handleQuantity(product.id)} 
                                min="1" 
                                max="10" 
                            />
                            <button type="submit" onClick={handleRemove(product.id)}>Remove Item</button>
                        </div>
                    )
                })}
                
            </>

        )

    }



    return (<></>);
}



export default CartProductTile;