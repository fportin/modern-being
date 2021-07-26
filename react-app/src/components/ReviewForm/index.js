import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";

import * as reviewActions from "../../store/review"
import shaded from "../../images/shade-star.png"
import unshaded from "../../images/unshade-star.png"
import './ReviewForm.css';

function ReviewForm({ edit, updater, submit }) {
    const dispatch = useDispatch()
    const history = useHistory()
    const currentProduct = useSelector((state) => state.products.product)
    const sessionUser = useSelector(state => state.session.user);
    const [reviewActive, setReviewActive] = useState(false);
    const [reviewBody, setReviewBody] = useState("");
    const [starRating, setStarRating] = useState(0)
    const [errors, setErrors] = useState([]);

    useEffect(() => {
        if (edit) {
            setReviewActive(false)
        }
    }, [edit]);

    const handleWrite = (e) => {
        e.preventDefault()
        if (sessionUser) {
            setReviewActive(true)
        } else {
            history.push("/login")
        }
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (sessionUser) {
            const data = await dispatch(reviewActions.createReview({ starRating, reviewBody, currentProduct, sessionUser }))
            if (data.errors) {
                return setErrors(data.errors)
            } else {
                setStarRating(0)
                setReviewBody('')
                setReviewActive(false)
                updater({})
                submit({})
                return
            }
        }
        return setErrors(['There was an error posting the Product Review.']);
    };

    const handleCancel = (e) => {
        e.preventDefault()
        setReviewActive(false)
        setStarRating(0)
        setReviewBody('')
        setErrors([])
    }

    if (currentProduct) {
        if (sessionUser && reviewActive && !edit) {
            const stars = []
            for(let i = 0; i < 5; i++) {
                const starVal = i + 1
                stars.push(
                    <label htmlFor={`${starVal}-star`} key={`${starVal}-star-form`}>
                        <input
                            type="radio"
                            name="rating"
                            value={starVal}
                            onChange={sessionUser ? ( (e) => {setStarRating(starVal)}) : null}
                            id={`${starVal}-star`}
                        />
                        <img 
                            className="star-icon" 
                            id={`${starVal}-star`}
                            alt="Star Icon"
                            src={(starVal <= starRating) ? shaded : unshaded}
                        />
                    </label>
                )
            }
            
            return (
                <>
                    <form className="review-form" onSubmit={handleSubmit}>
                        <ul className='review-form-errors'>
                            {errors.map((error, idx) => <div key={idx}>{error}</div>)}
                        </ul>
                        <label htmlFor="review" className='review-form-label'></label>
                        <div className="rating-container">
                            {stars}
                        </div>
                        <div className="review-container">
                            <textarea
                                id="review"
                                name="body"
                                placeholder={sessionUser ? "Tell us about the product" : "Login to post a review"}
                                value={reviewBody}
                                onChange={(e) => setReviewBody(e.target.value)}
                                required={true}
                                rows="5" 
                                cols="100"
                                className="review-input-box"
                            />
                        </div>
                        {sessionUser ? 
                            <div className='edit-review-btn__container'>
                                <button className='review-form-btn' type="submit">Submit</button>
                                <button className='review-form-btn' type="reset" onClick={handleCancel}>Cancel</button>
                            </div>
                            : null}                    
                    </form>
                </>
            );
        } else {
            if (!edit) {
                return (
                    <div className="write-review-btn" onClick={handleWrite}>{sessionUser ? "Write a Review" : "Login to Review"}</div>
                )

            }
        }

    }

    return (<></>)
}


export default ReviewForm;