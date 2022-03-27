import React, {useState, useEffect } from 'react';
import "../App.css"

// var boughtProductList;
// function getBoughtProducts(){
//   boughtProductList=JSON.parse(localStorage.getItem("boughtProducts"));
  
// }
// getBoughtProducts();

// console.log(boughtProductList);



function ProductCard(props) {
  
  const [boughtProducts, setBoughtProducts] = useState([{}]);

  useEffect(() => {
    const boughtProducts = JSON.parse(localStorage.getItem('boughtProducts'));
    if (boughtProducts) {
    setBoughtProducts(boughtProducts);
    }
  }, []);

  return (
    <div className='productCardContainer'>
        <img className="ProductCardImage" src={boughtProducts.imgPath} />
       <div className='productCardDetails'>
                
        <p className='ProductCardName'>Product Name : {boughtProducts.name}</p>
        <p className='ProductCardQty'>Product Quantity : {boughtProducts.productQuantity}</p>
        <p className='ProductCardPrice'>Product Price : Rs {boughtProducts.productPrice}</p>
       </div>
       
    </div>
  );
}
export default ProductCard