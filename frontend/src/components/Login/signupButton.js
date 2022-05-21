import React, { Component } from 'react';

class SignupButton extends Component{
    render() {
      return (
        <button
          className="btn btn-primary btn-block"
          onClick={() => {
            console.log('button to SIGNUP')
          }
        }
        >
          Sign Up
        </button>
      );
  }
}
  
export default SignupButton;