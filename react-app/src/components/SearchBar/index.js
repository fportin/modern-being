import React, { useState, useEffect } from "react";
import { useLocation, useHistory } from "react-router-dom";
import { useDispatch } from "react-redux";

import * as productActions from "../../store/products"
import searchIcon from "../../images/magnifying-glass.png"
import "./SearchBar.css"

function Searchbar({ search, searchOn }) {
    const location = useLocation();
    const dispatch = useDispatch();
    const history = useHistory();
    const [searchTerm, setSearchTerm] = useState("");
    const [searchActive, setSearchActive] = useState(false);
    // console.log("LOCATION", location.pathname)
    useEffect(() => {
        if (!searchOn) {
            setSearchActive(false)
            setSearchTerm("")
            if (location.pathname === '/search') {
                history.push("/");
            }
        }

        if (searchActive) {
            if (searchTerm) {
                const timeout = setTimeout(() => {
                    dispatch(productActions.searchProducts(searchTerm));
                    history.push({
                        pathname: "/search",
                        state: {
                            searchTerm: searchTerm,
                        },
                    });
                }, 500)
                return () => clearTimeout(timeout)
            } else if (!searchTerm && location.pathname === '/search') {
                history.push("/");
            }
        }

    }, [searchTerm, dispatch, searchOn]);

    const handleClickOut = (e) => {
        e.preventDefault()
        if (!searchTerm) {
            setTimeout(() => {
                setSearchActive(false)
                search(false)
            }, 250)
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
                <img className="search-icon" src={searchIcon} alt='Search Icon' onClick={(e) => {
                    setSearchActive(true)
                    search(true)
                }} />
            }
        </div>
    );
}

export default Searchbar;
