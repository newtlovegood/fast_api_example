import React, { Component } from 'react';

import LoginButton from './loginButton';
import LogoutButton from './logoutButton';
import { isLoggedIn } from './login';


class AuthenticationButton extends Component {
    render() {
        return (
            <>
            {isLoggedIn() ? <LogoutButton /> : <LoginButton />}
            </>
        )
    }
}

export default AuthenticationButton;