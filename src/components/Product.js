import React from "react"
import "../App.css"
import data from "../data.json"

function Product() {
  
  var lastIndex= data.length - 1
  return (
    <div className='mainProductContainer'>
     
       <img className="mainProductImage" src={data[lastIndex].image} />
       <div className='mainProductDetails'>

        <p className='mainProductName'>Product Name : {data[lastIndex].name}</p>
        <p className='mainProductQty'>Product Quantity : {data[lastIndex].quantity}</p>
        <p className='mainProductPrice'>Product Price : Rs {data[lastIndex].price}</p>
       </div>
       <div className="lastContainer">
          <div className='totalPriceContainer'>
          <p className='totalPrice'>Total Price : Rs {data[lastIndex].totalPrice}</p> 
          </div>
          <div className="checkoutButton">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            CHECKOUT
          </div>
       </div>
       
    </div>
  );
}
export default Product