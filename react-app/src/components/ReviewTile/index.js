import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import * as reviewActions from "../../store/review"
import ReviewForm from "../ReviewForm"
import shaded from "../../images/shade-star.png"
import unshaded from "../../images/unshade-star.png"
import "./ReviewTile.css"

function ReviewTile({ submitted }) {
    const dispatch = useDispatch();
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
                submitted({})
                return
            }
        }
        return setErrors(['Errors in editing your review for the Product.']);
    };

    const handleCancel = (e) => {
        e.preventDefault();
        setEditReview(false)
        setErrors([])
    }

    const handleDelete = async (e) => {
        e.preventDefault();
        if (sessionUser) {
            const data = await dispatch(reviewActions.deleteReview({ currentProduct, sessionUser, target }))
            if (data.errors) {
                return setErrors(data.errors)
            } else {
                setEditReview(false)
                submitted({})
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
                        alt="Star Icon"
                    />
                </label>
            )
        }
        
        const availableReviews = allReviews.matchingReviews
        return (
            <div className="reviews__container">
                <div className='review-title'>Reviews:</div>
                <ReviewForm edit={editReview} updater={setPageRefresh} submit={submitted} />
                {availableReviews.map((review, idx) => {
                    if (!editReview) {
                        return (
                            <div key={`review-${review[0].id}`} className='review-box'>
                                <div className="review-box-user">{review[1].username}</div>
                                {[...Array(5)].map((star, idx2) => {
                                    return (<img
                                        key={`${idx2}-rating`}
                                        className="star-icon"
                                        id={`${idx2}-star`}
                                        alt="Star Icon"
                                        src={(review[0].rating >= idx2 + 1) ? shaded : unshaded}
                                    />)
                                })}
                                <div className="review-box-body">{review[0].body}</div>
                                {sessionUser?.id === review[0].userId ? <button type='submit' onClick={handleEdit(review[0])} className="review-box-edit-btn">Edit</button> : null}
                            </div>
                        )

                    } else {
                        if (sessionUser?.id === review[0].userId && target === review[0].id) {
                            return (
                                <div key={`${idx}-edit-review`} className='edit-review__container'>
                                    <form onSubmit={handleSubmitEdit}>
                                        <ul className='edit-review-form-errors'>
                                            {errors.map((error, idx) => <li key={`${idx}-edit-error`}>{error}</li>)}
                                        </ul>
                                        <label className="edit-review-title">
                                            Edit your Review:
                                            <span className="edit-review-stars__container">{stars}</span>
                                            <textarea
                                                value={reviewBody || ""}
                                                onChange={(e) => setReviewBody(e.target.value)}
                                                rows="5"
                                                cols="100"
                                                className="edit-review-box"
                                                name="edit-body"
                                            />
                                        </label>
                                        <div className='edit-review-btn__container'>
                                            <button className='review-form-btn' type="submit">Submit</button>
                                            <button className='review-form-btn' type="reset" onClick={handleCancel}>Cancel</button>
                                            <button className='review-form-btn delete' type="button" onClick={handleDelete}>Delete</button>
                                        </div>
                                    </form>
                                </div>
                            )

                        }
                        return (<></>)
                    }
                })}
            </div>
        )

    }

    return (<h1>Reviews</h1>);
}



export default ReviewTile;