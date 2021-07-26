import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";

import * as categoryActions from "../../store/category";
import './CategoryTile.css';

function CategoryTile() {
    const dispatch = useDispatch();
    const history = useHistory();
    const allCategories = useSelector((state) => state.categories.allCategories);
    // const [errors, setErrors] = useState([]);


    useEffect(() => {
        dispatch(categoryActions.getCategories())
    }, [dispatch]);

    const handleClick = categoryId => (e) => {
        e.preventDefault();
        window.scrollTo(0, 0)
        history.push(`/categories/${categoryId}`)
    }

    if (allCategories) {
        const availableCategories = allCategories.matchingCategories
        return (
            <>
                {availableCategories?.map(category => {
                    if (category[0].id <= 10) {
                        return (
                            <div key={category[0].id} className="category-tile__container" onClick={handleClick(category[0].id)}>
                                <div className='category-tile-photo' style={{ backgroundImage: `url(${category[1].photo})` }} ></div>
                                <div className='category-tile-type'>{category[0].type}</div>
                            </div>
                        )
                    } else {
                        return null
                    }

                })}

            </>

        )

    }



    return (<></>);
}



export default CategoryTile;