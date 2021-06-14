import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";

import * as reviewActions from "../../store/review"
import ReviewForm from "../ReviewForm"
import shaded from "../../images/shade-star.png"
import unshaded from "../../images/unshade-star.png"
import "./ReviewTile.css"

function ReviewTile() {
    const dispatch = useDispatch();
    const history = useHistory();
    const currentProduct = useSelector((state) => state.products.product)
    const sessionUser = useSelector((state) => state.session.user);
    const allReviews = useSelector((state) => state.reviews.allReviews);
    const [reviewBody, setReviewBody] = useState("");
    const [starRating, setStarRating] = useState(0)
    const [editReview, setEditReview] = useState(false);
    const [pageRefresh, setPageRefresh] = useState({});
    const [target, setTarget] = useState(null);
    const [errors, setErrors] = useState([]);


    useEffect(() => {
        dispatch(reviewActions.getReviews(currentProduct.id))
    }, [currentProduct.id, dispatch, editReview, pageRefresh]);


    const handleEdit = review => (e) => {
        e.preventDefault();
        setTarget(review.id)
        setEditReview(true)
        setStarRating(review.rating)
        setReviewBody(review.body)
    }

    const handleSubmitEdit = async (e) => {
        e.preventDefault();
        if (sessionUser) {
            const data = await dispatch(reviewActions.updateReview({ starRating, reviewBody, currentProduct, sessionUser, target }))
            if (data.errors) {
                return setErrors(data.errors)
            } else {
                setEditReview(false)
                return
            }
        }
        return setErrors(['Errors in editing your review for the Product.']);
    };

    const handleDelete = async (e) => {
        e.preventDefault();
        if (sessionUser) {
            const data = await dispatch(reviewActions.deleteReview({ currentProduct, sessionUser, target }))
            if (data.errors) {
                return setErrors(data.errors)
            } else {
                setEditReview(false)
                return
            }
        }
        return setErrors(['Errors in deleting the Product Review.']);
    };


    if (currentProduct && allReviews) {
        const stars = []
        for (let i = 0; i < 5; i++) {
            const starVal = i + 1
            stars.push(
                <label key={`${starVal}-edit-star`} htmlFor={`${starVal}`}>
                    <input
                        type="radio"
                        name="rating"
                        value={starVal}
                        onChange={sessionUser && editReview ? ((e) => { setStarRating(starVal) }) : null}
                        id={`${starVal}`}
                    />
                    <img
                        className="star-icon"
                        id={`${starVal}`}
                        src={(starVal <= starRating) ? shaded : unshaded}
                    />
                </label>
            )
        }
        
        const availableReviews = allReviews.matchingReviews
        return (
            <div className="reviews__container">
                <h4 className='review-title'>Reviews:</h4>
                <ReviewForm edit={editReview} updater={setPageRefresh} />
                {availableReviews.map((review, idx) => {
                    if (!editReview) {
                        return (
                            <div key={`review-${review[0].id}`} className='review-box'>
                                <h3>{review[1].username}</h3>
                                {[...Array(5)].map((star, idx2) => {
                                    return (<img
                                        key={`${idx2}-rating`}
                                        className="star-icon"
                                        id={`${idx2}-star`}
                                        src={(review[0].rating >= idx2 + 1) ? shaded : unshaded}
                                    />)
                                })}
                                <h4>{review[0].body}</h4>
                                {sessionUser?.id === review[0].userId ? <button type='submit' onClick={handleEdit(review[0])}>Edit</button> : null}
                            </div>
                        )

                    } else {
                        if (sessionUser?.id === review[0].userId && target === review[0].id) {
                            return (
                                <div key={`${idx}-edit-review`} className='review-box'>
                                    <form onSubmit={handleSubmitEdit}>
                                        <ul>
                                            {errors.map((error, idx) => <li key={`${idx}-edit-error`}>{error}</li>)}
                                        </ul>
                                        <label>
                                            Edit your Review:
                                            {stars}
                                            <textarea
                                                value={reviewBody || ""}
                                                onChange={(e) => setReviewBody(e.target.value)}
                                                rows="5"
                                                cols="100"
                                                className="review-edit-box"
                                                name="edit-body"
                                            />
                                        </label>
                                        <button type="submit">Edit Review</button>
                                    </form>
                                    <button type="submit" onClick={handleDelete}>Delete</button>
                                </div>
                            )

                        }
                        // return (<></>)
                    }
                })}
            </div>
        )

    }

    return (<h1>Reviews</h1>);
}



export default ReviewTile;