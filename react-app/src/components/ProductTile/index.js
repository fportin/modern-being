import React from "react";
import { useSelector } from "react-redux";
import { useHistory } from "react-router-dom";

// import * as productActions from "../../store/products";
import shaded from "../../images/shade-star.png"
import './ProductTile.css';

function ProductTile() {
    // const dispatch = useDispatch();
    const history = useHistory();
    const allProducts = useSelector((state) => state.products.allProducts);

    // const handleAdd = productId => (e) => {
    //     e.preventDefault()
    //     const currentCart = localStorage.getItem('cart')
    //     let quantity = 1
    //     let data = { [productId]: quantity }
    //     if (currentCart) {
    //         data = JSON.parse(currentCart)
            
    //         if (data[`${productId}`]) {
    //             if (data[`${productId}`] < 10) {
    //                 data[`${productId}`] += 1
    //             } else {
    //                 alert("Order limit per item is 10.")
    //             }
    //         } else {
    //             data[`${productId}`] = quantity
    //         }
    //         localStorage.setItem('cart', JSON.stringify(data))
    //     } else {
    //         localStorage.setItem('cart', JSON.stringify(data))
    //     }
    //     const newCart = JSON.parse(localStorage.getItem('cart'))
    //     dispatch(productActions.getCartProducts(newCart))
    // }

    const handleClick = productId => (e) => {
        e.preventDefault();
        window.scrollTo(0, 0)
        history.push(`/products/${productId}`)
    }

    const reviewsLink = productId => (e) => {
        e.preventDefault();
        window.scrollTo(0,0)
        history.push(`/products/${productId}`)
        setTimeout(() => {
            window.scrollTo(0, 580)
        }, 50)
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
                                    <div className="product-tile-text-top">
                                        <div className='product-tile-name' onClick={handleClick(product.id)}>{product.name}</div>
                                        <div className='product-tile-brand'>{product.brand}</div>
                                        <div className='product-tile-price'>{product.price.toLocaleString('en-US', { style: 'currency', currency: 'USD' })}</div>
                                        <div className='product-tile-rating'>{product.rating.toFixed(1)}<img className="star-icon" src={shaded} alt="Star Icon" />
                                            <span className='product-tile-rating-reviewers' onClick={reviewsLink(product.id)}>({product.reviewers} Reviews)</span>
                                        </div>
                                    </div>
                                    {/* <button type="submit" onClick={handleAdd(product.id)} className="product-tile-add-btn">Add to Cart</button> */}
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