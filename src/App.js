import React from "react"

import Product from "./components/Product"
import ProductCard from "./components/ProductCard"
import "./index.css"



function App(){
  return (
    <div className="mainContainer">
      <Product />
      <div className="productsContainer">
        <ProductCard /> 
      </div>
      
    </div>
    
  )
}
export default App