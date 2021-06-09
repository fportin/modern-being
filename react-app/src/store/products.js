// constants
const SET_PRODUCT = "products/SET_PRODUCT";
const SHOW_PRODUCTS = "products/SHOW_PRODUCTS";

const setProduct = (product) => {
    return {
        type: SET_PRODUCT,
        product
    }
}

const showProducts = (allProducts) => {
    return {
        type: SHOW_PRODUCTS,
        allProducts
    }
}


export const getProducts = (categoryId) => async(dispatch) => {
    const res = await fetch(`/api/products/categories/${categoryId}`);

    if (res.ok) {
        const data = await res.json();

        dispatch(showProducts(data))
    }
}

export const getProduct = (productId) => async (dispatch) => {
    const res = await fetch(`/api/products/${productId}`)

    if (res.ok) {
        const data = await res.json()

        dispatch(setProduct(data))
    }
}


const initialState = { product: null, allProducts: null };

const productReducer = (state = initialState, action) => {
    switch (action.type) {
        case SHOW_PRODUCTS:
            return {
                ...state,
                allProducts: action.allProducts
            };
        case SET_PRODUCT:
            return {
                ...state,
                product: action.product
            }
        default:
            return state;
    }
}


export default productReducer