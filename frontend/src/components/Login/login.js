import React, { useState } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';
import { useNavigate } from 'react-router';

export const fetchToken = ()=> {
  return localStorage.getItem('saved_token')
}

export const setToken = (token)=>{
  localStorage.setItem('saved_token', token)// make up your own token
}

export const isLoggedIn = () => {
  if (fetchToken()) {
    return true
  }
  return false
}


export default function Login() {
  
  const navigate = useNavigate();
  const [username, setUserName] = useState('');
  const [password, setPassword] = useState('');
  //check to see if the fields are not empty
  const login = () => {
    if ((username == "") & (password == "")) {
      return;
    } else {
      // make api call to our backend. we'll leave thisfor later
      axios.post('http://127.0.0.1:8000/token', {
        username: username,
        password: password,
      }).then(response => {
        setToken(response.data.access_token);
      }).then(
        navigate('/')
      ).catch(function (error) {
        console.log(error, "error");
      });
    }
  };

  return(

    <div className='login-wrapper'>
      <form>
      {/* <!-- Email input --> */}
      <div className="form-outline mb-4">
          <input type="text" id="form2Example1" className="form-control" onChange={e => setUserName(e.target.value)} />
          <label className="form-label" htmlFor="form2Example1">Email address</label>
      </div>

      {/* <!-- Password input --> */}
      <div className="form-outline mb-4">
          <input type="password" id="form2Example2" className="form-control" onChange={e => setPassword(e.target.value)} />
          <label className="form-label" htmlFor="form2Example2">Password</label>
      </div>

      {/* <!-- 2 column grid layout htmlFor inline styling --> */}
      <div className="row mb-4">
          <div className="col d-flex justify-content-center">
          </div>

          <div className="col">
          {/* <!-- Simple link --> */}
          <a href="#!">Forgot password?</a>
          </div>
      </div>

      {/* <!-- Submit button --> */}
      <button type="submit" className="btn btn-primary btn-block mb-4" onClick={login}>Sign in</button>

      </form>
    </div>
    

  )
}

Login.propTypes = {
  setToken: PropTypes.func.isRequired
};