import React, { useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import { useSelector } from 'react-redux';

import './PurchasePage.css'


const PurchasePage = () => {
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
            <h1 className='purchase-page'>Thank you for your purchase, <span className='purchase-page-user-name'>{sessionUser.username}</span>! We will be processing your order shortly.</h1>
        </>
    )


};



export default PurchasePage;