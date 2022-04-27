import React, {Component, component} from 'react'
import "../App.css"

class Timer extends Component{
    state ={
        date: new Date()
    };
    callMe(){
        setInterval(() => {
            this.setState({date: new Date()});
        }, 1000);
    }
    render(){
        return(<div>
                <h4 className='time'>{this.state.date.toLocaleTimeString()}{this.callMe()}</h4>
                <hr />
            </div>);
        
    }
}


export default Timer