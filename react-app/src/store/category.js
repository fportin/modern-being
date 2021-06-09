// constants
const SHOW_CATEGORIES = "category/SHOW_CATEGORIES";

const showCategories = (categories) => {
    return {
        type: SHOW_CATEGORIES,
        categories
    }
}


export const getCategories = () => async (dispatch) => {
    const res = await fetch('/api/categories');

    if (res.ok) {
        const data = await res.json();

        dispatch(showCategories(data))
    }
}


const initialState = { allCategories: null };

const categoryReducer = (state = initialState, action) => {
    switch (action.type) {
        case SHOW_CATEGORIES:
            return {
                ...state,
                allCategories: action.categories
            };
        default:
            return state;
    }
}


export default categoryReducer