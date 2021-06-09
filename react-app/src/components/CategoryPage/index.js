import React, { useEffect } from "react"
import { useParams, useHistory} from "react-router-dom";
import { useDispatch } from "react-redux";

import * as productActions from "../../store/products"
import ProductTile from "../ProductTile"
import "./CategoryPage.css"

function CategoryPage() {
    const dispatch = useDispatch();
    const { categoryId } = useParams();

    useEffect(() => {
        dispatch(productActions.getProducts(categoryId))
    }, [dispatch, categoryId])

    return (
        <div className="category-page__container">
            <ProductTile />
        </div>
    )
}

export default CategoryPage;