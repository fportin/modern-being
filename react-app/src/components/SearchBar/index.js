import React, { useState, useEffect } from "react";
import { useLocation, useHistory } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";

import * as productActions from "../../store/products"
import searchIcon from "../../images/magnifying-glass.png"
import "./SearchBar.css"

function Searchbar({ search }) {
    const location = useLocation();
    const dispatch = useDispatch();
    const history = useHistory();
    const [searchTerm, setSearchTerm] = useState("");
    const [searchActive, setSearchActive] = useState(false);
    // console.log("LOCATION", location.pathname)
    useEffect(() => {
        if (searchActive) {
            if (searchTerm) {
                dispatch(productActions.searchProducts(searchTerm));
                history.push("/search");
            } else if (!searchTerm && location.pathname === '/search') {
                history.push("/");
            }
        } else {
            history.push("/")
        }

    }, [searchTerm, dispatch]);

    const handleClickOut = (e) => {
        e.preventDefault()
        if (!searchTerm) {
            setSearchActive(false)
            search(false)
        }
    }


    return (
        <div className="search-bar__container">
            {searchActive ?
                <input
                    className="search-bar"
                    placeholder="Search Modern Being"
                    type="text"
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    onBlur={handleClickOut}
                    autoFocus
                /> :
                <img className="search-icon" src={searchIcon} onClick={(e) => {
                    setSearchActive(true)
                    search(true)
                }} />
            }
        </div>
    );
}

export default Searchbar;
