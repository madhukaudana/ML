import React from 'react'
import '../css/Home.css'
import { useNavigate} from "react-router-dom"
function Home(){
    let navigate =useNavigate();
    return(
        <div className='body'>
            <div className='startDiv'>
                <h1>Welcome</h1>
                <div class="startButton" onClick={() => {
                    navigate("/buying")
                }}>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    Start
                </div>
            </div>
        </div>
    )
}
export default Home