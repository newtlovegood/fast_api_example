import React, { Component } from "react";

// send login/email with password to localhost.../token
// change button to logout 
// redirect to previous page
// set global status LOGGED IN to add TOKEN to diff urls 

class LoginButton extends Component{
  render() {
    return <a  className="nav-item nav-link"  href="/login">Login</a>

  }
}

export default LoginButton;