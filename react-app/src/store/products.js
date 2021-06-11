// constants
const SET_PRODUCT = "products/SET_PRODUCT";
const SHOW_PRODUCTS = "products/SHOW_PRODUCTS";
const SHOW_CART_PRODUCTS = "products/SHOW_CART_PRODUCTS";

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

const showCartProducts = (cartProducts) => {
    return {
        type: SHOW_CART_PRODUCTS,
        cartProducts
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

export const searchProducts = (searchTerm) => async (dispatch) => {
    const res = await fetch(`api/products/search`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            searchTerm,
        }),
    });

    if (res.ok) {
        const data = await res.json();

        dispatch(showProducts(data))
    }

    return res;
};

export const getCartProducts = (productsArr) => async (dispatch) => {
    const res = await fetch(`api/products/cart`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            productsArr,
        }),
    });
    
    if (res.ok) {
        const data = await res.json();
        dispatch(showCartProducts(data));
    }

    return res;
}


const initialState = { product: null, allProducts: null, cartProducts: null };

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
            };
        case SHOW_CART_PRODUCTS:
            return {
                ...state,
                cartProducts: action.cartProducts
            }
        default:
            return state;
    }
}


export default productReducer