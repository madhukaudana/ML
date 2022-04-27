import React from "react"

import Product from "./components/Product"
import Data from "./data.json"

import Timer from "./components/Timer"
import {BrowserRouter as Router, Route, Routes } from 'react-router-dom'

import Checkout from "./components/Checkout"
import Home from "./components/Home"
import Buying from "./components/Buying"

function App(){
  return (
    <Router>
      <Routes> 
        <Route path="/" element={<Home />} />
        <Route path="/checkout" element={<Checkout />} />
        <Route path="/buying" element={<Buying />} />
      </Routes>
    </Router>
    
  )
}
export default App