import  React, { Component } from  'react';
import { BrowserRouter, Route, Routes } from  'react-router-dom'
import  PostsList  from  './components/PostsList'
import  SinglePost  from  './components/SinglePost'
import  './App.css';


const  BaseLayout  = () => (
  <div  className="container-fluid">
    <nav  className="navbar navbar-expand-lg navbar-light bg-light">
      <a  className="navbar-brand"  href="/">Home</a>
      <button  className="navbar-toggler"  type="button"  data-toggle="collapse"  data-target="#navbarNavAltMarkup"  aria-controls="navbarNavAltMarkup"  aria-expanded="false"  aria-label="Toggle navigation">
      <span  className="navbar-toggler-icon"></span>
    </button>
    <div  className="collapse navbar-collapse"  id="navbarNavAltMarkup">
      <div  className="navbar-nav">
        <a  className="nav-item nav-link"  href="/">Compose</a>
        <a  className="nav-item nav-link"  href="/">ToDo</a>
        <a  className="nav-item nav-link"  href="/customer">Log In</a>
      </div>
    </div>
    </nav>
    <div  className="content">
      <Routes>
        <Route  path="/"  exact  element={<PostsList />} />
        <Route  path="/posts" element={<PostsList />} />
        <Route  path="/posts/:id"  element={<SinglePost />} />
      </Routes>
    </div>
  </div>
  )

  class  App  extends  Component {

    render() {
      return (
      <BrowserRouter>
        <BaseLayout/>
      </BrowserRouter>
      );
    }
    }
    export  default  App;