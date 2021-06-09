import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, Redirect } from "react-router-dom";

import './CartProductTile.css';

function CartProductTile() {
    const history = useHistory();
    const cartProducts = useSelector((state) => state.products.cartProducts);
    const sessionUser = useSelector((state) => state.session.user);
    // const allReviews = useSelector((state) => state.reviews.allReviews);
    // const [errors, setErrors] = useState([]);


    // useEffect(() => {
    //     dispatch(productActions.getProducts())
    // }, [dispatch]);

    const handleClick = productId => (e) => {
        e.preventDefault();
        history.push(`/products/${productId}`)
    }

    if (cartProducts) {
        const addedProducts = cartProducts.matchingProducts
        return (
            <>
                {addedProducts?.map(product => {
                    return (
                        <div key={product.id} className='product-tile__container' style={{ backgroundImage: `url(https:${product.photo})` }} onClick={handleClick(product.id)}>
                            {product.name}
                        </div>
                    )
                })}

            </>

        )

    }



    return (<></>);
}



export default CartProductTile;