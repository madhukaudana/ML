import React from "react"

import Product from "./Product"
import Data from "../data.json"
import "../index.css"
import Timer from "./Timer"

function Buying(){
  
  return (
    
    <div className="mainContainer">
      <div className="one">
         <Timer />
      </div>
      <div className="two">
        {Data.map(post => {
            return(
              <div key={post.id} className='productCardContainer'>
                <img className="ProductCardImage" src={post.image} alt={post.name}/>
                <div className='productCardDetails'>
                  
                  <p className='ProductCardName'>Product Name : {post.name}</p>
                  <p className='ProductCardQty'>Product Quantity : {post.quantity}</p>
                  <p className='ProductCardPrice'>Product Price : Rs {post.price}</p>
                </div>
        
              </div>
            )
          })
          }
      </div>
      <div className="three">
          
         <Product />
      </div>
      {/* <Timer />
      
      <Product />
      <div className="productsContainer">
        {Data.map(post => {
          return(
            <div key={post.id} className='productCardContainer'>
              <img className="ProductCardImage" src={post.image} alt={post.name}/>
              <div className='productCardDetails'>
                
                <p className='ProductCardName'>Product Name : {post.name}</p>
                <p className='ProductCardQty'>Product Quantity : {post.quantity}</p>
                <p className='ProductCardPrice'>Product Price : Rs {post.price}</p>
              </div>
       
            </div>
          )
        })
        }
      </div> */}
      
    </div>
    
  )
}
export default Buying