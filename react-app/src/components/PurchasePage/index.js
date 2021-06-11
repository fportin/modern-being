import React, { useEffect } from 'react';
import { Redirect, useHistory } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';

import './PurchasePage.css'


const PurchasePage = () => {
    // const dispatch = useDispatch();
    const sessionUser = useSelector(state => state.session.user);
    const history = useHistory();

    useEffect(() => {
        if (sessionUser) {
            const timeout = setTimeout(() => {
                history.push("/");
            }, 3000)
            return () => clearTimeout(timeout);
        }
    }, [sessionUser, history])
    if (sessionUser) return (
        <>
            <h1 className='purchase-page'>Thank you for your purchase, {sessionUser.username}! We will be processing your order shortly.</h1>
        </>
    )


};



export default PurchasePage;