import './App.css';
import './css/Signup.css'

import React from 'react';
import { Router, Routes, Route } from 'react-router-dom'
/*import Home from './Pages/Home';
import Contacts from './Pages/Contacts';
import Donate from './Pages/Donate';
import Login from './Pages/Login';*/
import  Signup from './Pages/Signup';
import Header from './Components/Header';


function App() {
  return (
    <>
      <Header />   
      <Signup />
    </>
    
  );
}

export default App;
