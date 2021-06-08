// constants
// const SET_PRODUCT = "products/SET_PRODUCT";
const SHOW_PRODUCTS = "products/SHOW_PRODUCTS";

const showProducts = (allProducts) => {
    return {
        type: SHOW_PRODUCTS,
        allProducts
    }
}


export const getProducts = () => async(dispatch) => {
    const res = await fetch('/api/products');

    if (res.ok) {
        const data = await res.json();

        dispatch(showProducts(data))
    }
}


const initialState = { product: null };

const productReducer = (state = initialState, action) => {
    switch (action.type) {
        case SHOW_PRODUCTS:
            return {
                ...state,
                allProducts: action.allProducts
            };
        default:
            return state;
    }
}


export default productReducer