import React from 'react';
import AuthenticationButton from './Login/authentication-button';
import SignupButton from './Login/signupButton';


const NavBar = () => {
  return (
    <div  className="container-fluid">
        <nav  className="navbar navbar-expand-lg navbar-light bg-light">
        <a  className="navbar-brand"  href="/">Home</a>
        <button  className="navbar-toggler"  type="button"  data-toggle="collapse"  data-target="#navbarNavAltMarkup"  aria-controls="navbarNavAltMarkup"  aria-expanded="false"  aria-label="Toggle navigation">
        <span  className="navbar-toggler-icon"></span>
        </button>
        <div  className="collapse navbar-collapse"  id="navbarNavAltMarkup">
                <div  className="navbar-nav">
                    <a  className="nav-item nav-link"  href="/compose">Compose</a>
                    <a  className="nav-item nav-link"  href="/todo">ToDo</a>
                    <AuthenticationButton />
                    <SignupButton />
                </div>
            </div>
        </nav>
    </div>
  );
};

export default NavBar;