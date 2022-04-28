import React from 'react'
import '../css/checkout.css'
import data from "../data.json"
import { useNavigate} from "react-router-dom"
function Checkout(){
    let navigate =useNavigate();
    var lastIndex= data.length - 1
    return(
        <div className='checkoutBody'>
            <div className='containerOne'>
                <h3 className='textOne'>Thank You</h3>
                <h3 className='tPrice'>Your Total Price is Rs{data[lastIndex].totalPrice}</h3>
                <div className="homeButton" onClick={() => {
                    navigate("/")
                }}>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    HOME
                </div>
            </div>
            
        </div>
    )
}
export default Checkout