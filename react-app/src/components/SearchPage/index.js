import React from "react";
import { useLocation } from "react-router-dom"

import ProductTile from "../ProductTile"
import "./SearchPage.css"


const SearchPage = () => {
    const location = useLocation();

    return (
        <div className="full-search-page__container">
            <div className="search-page__container">
                {location.state ? <h1>You searched for "{location.state.searchTerm}".</h1> : null}
                <ProductTile />
            </div>
        </div>
    )
   
};


export default SearchPage;
