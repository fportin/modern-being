import React, { useState, useEffect } from "react"

import "./FrontPage.css"
import logo from "../../images/modern-being-logo.png"

function FrontPage() {

    return (
        <div className="front-page__container">
            <div className="front-logo__container" style={{ backgroundImage: `url(${logo})` }}>
            </div>
        </div>
    )
}

export default FrontPage;