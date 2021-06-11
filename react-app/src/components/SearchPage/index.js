import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom"

import ProductTile from "../ProductTile"
import "./SearchPage.css"


const SearchPage = () => {

    return (
        <div className="full-search-page__container">
            <div className="search-page__container">
                <ProductTile />
            </div>
        </div>
    )
   
};


export default SearchPage;
