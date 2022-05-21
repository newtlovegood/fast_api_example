import  React, { Component } from  'react';
import { BrowserRouter, Route, Routes } from  'react-router-dom';

import  PostsList  from  './components/PostsList';
import  SinglePost  from  './components/SinglePost';
import MyEditor from './components/Compose';
import Navbar from './components/navbar';

import  './css/App.css';
import Login from './components/Login/login';
import { fetchToken } from './components/Login/login';
import ToDoList from './components/Todo/toDoList';


class  App  extends  Component {

  constructor(props) {
    super(props);
    this.state = {
      token: fetchToken(),
    };
  }


  render() {
      
    return (
      <BrowserRouter>
      <Navbar />
      <div  className="content">
        <Routes>
          <Route  path="/"  exact  element={<PostsList />} />
          <Route  path="/compose" element={<MyEditor />} />
          <Route  path="/todo" element={<ToDoList />} />
          <Route  path="/posts" element={<PostsList />} />
          <Route  path="/posts/:id"  element={<SinglePost />} />
          <Route  path="/login"  element={<Login />} />
        </Routes>
      </div>
      </BrowserRouter>
    );
  }
  }
  export  default  App;