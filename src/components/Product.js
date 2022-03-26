import React, {useState, useEffect } from 'react';
import "../App.css"

function Product(props) {
  const [data, setData]=useState([{}])

  useEffect(() => {
    fetch("/productDetails").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])
  
  
  return (
    <div className='mainProductContainer'>
      {/* {(typeof data.members === 'undefined') ? (
        <p>Loading..</p>
      ):(
        data.members.map((member, i) => (
          <p key={i}>{member}</p>
        ))
      )}
       */}
       <img className="mainProductImage" src={data.imgPath} />
       <div>
        <p className='mainProductName'>Product Name : {data.name}</p>
        <p className='mainProductQty'>Product Quantity : {data.productQuantity}</p>
        <p className='mainProductPrice'>Product Price : Rs {data.productPrice}</p>
       </div>
       
    </div>
  );
}
export default Product