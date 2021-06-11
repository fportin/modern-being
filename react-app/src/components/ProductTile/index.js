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
                            <div key={product.id} className='product-tile__container' style={{ backgroundImage: `url(${product.photo})` }} onClick={handleClick(product.id)}>
                                {product.name}
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