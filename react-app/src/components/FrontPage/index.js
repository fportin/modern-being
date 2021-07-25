import React, { useEffect } from "react"
import { useDispatch } from "react-redux";

import * as categoryActions from "../../store/category"
import CategoryTile from "../CategoryTile"
import "./FrontPage.css"
import logo from "../../images/modern-being-logo.png"

function FrontPage() {
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(categoryActions.getCategories())
    }, [dispatch])

    return (
        <div className="front-page__container">
            <div className="front-logo__container" style={{ backgroundImage: `url(${logo})` }}>
            </div>
            <div className="front-page-text">Shop our Latest Tech</div>
            <CategoryTile />
        </div>
    )
}

export default FrontPage;