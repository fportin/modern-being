import React, { useState, useEffect } from "react"
import { useDispatch, useSelector } from "react-redux";

import * as productActions from "../../store/products"
import ProductTile from "../ProductTile"
import "./FrontPage.css"
import logo from "../../images/modern-being-logo.png"

function FrontPage() {
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(productActions.getProducts())
    }, [dispatch])

    return (
        <div className="front-page__container">
            <div className="front-logo__container" style={{ backgroundImage: `url(${logo})` }}>
            </div>
            <ProductTile />
        </div>
    )
}

export default FrontPage;