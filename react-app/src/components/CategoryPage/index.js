import React, { useEffect } from "react"
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";

import * as productActions from "../../store/products"
import ProductTile from "../ProductTile"
import "./CategoryPage.css"

function CategoryPage() {
    const dispatch = useDispatch();
    const { categoryId } = useParams();
    const categories = useSelector((state) => state.categories.allCategories);

    useEffect(() => {
        dispatch(productActions.getProducts(categoryId))
    }, [dispatch, categoryId])

    return (
        <div className="category-page__container">
            {categories ? <div className="category-page-title">{categories.matchingCategories[categoryId - 1][0].type}</div> : null}
            <div className="category-page-products_container">
                <ProductTile />
            </div>
        </div>
    )
}

export default CategoryPage;