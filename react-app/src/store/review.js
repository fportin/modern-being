// constants
const SET_REVIEW = 'review/SET_REVIEW';
const SHOW_REVIEWS = 'review/SHOW_REVIEWS';

const setReview = (review) => {
    return {
        type: SET_REVIEW,
        review
    }
}

const showReviews = (allReviews) => {
    return {
        type: SHOW_REVIEWS,
        allReviews
    }
}


export const createReview = (productReview) => async (dispatch) => {
    const { starRating, reviewBody, currentProduct, sessionUser } = productReview;
    const rating = starRating
    const body = reviewBody
    const productId = currentProduct.id
    const userId = sessionUser.id;
    const res = await fetch(`/api/reviews/create`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            rating,
            body,
            productId,
            userId
        }),
    });

    const data = await res.json();
    if (data.errors) {
        return data
    }
    dispatch(setReview(data))
    return data;
};

export const getReviews = (productId) => async (dispatch) => {
    const res = await fetch(`/api/reviews/${productId}`);
    if (res.ok) {
        const data = await res.json();
        dispatch(showReviews(data));
    }
    // return res;
};

export const updateReview = (review) => async (dispatch) => {
    const { starRating, reviewBody, currentProduct, sessionUser, target } = review;
    const rating = starRating
    const body = reviewBody
    const productId = currentProduct.id
    const userId = sessionUser.id;
    const res = await fetch(`/api/reviews/${productId}/edit`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            rating,
            body,
            productId,
            userId,
            target
        }),
    });

    const data = await res.json();
    if (data.errors) {
        return data
    }
    dispatch(setReview(data))
    return data;
};

export const deleteReview = (review) => async (dispatch) => {
    const { currentProduct, sessionUser, target } = review;
    const productId = currentProduct.id
    const userId = sessionUser.id;
    const res = await fetch(`/api/reviews/${productId}/delete`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            productId,
            userId,
            target
        }),
    });
    
    const data = await res.json();
    if (data.errors) {
        return data
    }
    dispatch(setReview(data))
    return data;
};


const initialState = { allReviews: null, review: null }
const reviewReducer = (state = initialState, action) => {
    switch (action.type) {
        case SHOW_REVIEWS:
            return {
                ...state,
                allReviews: action.allReviews
            };
        case SET_REVIEW:
            return {
                ...state,
                review: action.review
            };
        default:
            return state;
    }
}


export default reviewReducer;