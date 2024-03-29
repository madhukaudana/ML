import React from "react"

import Product from "./components/Product"
import Data from "./data.json"
import "./index.css"



function App(){
  return (
    <div className="mainContainer">
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
      </div>
      
    </div>
    
  )
}
export default App