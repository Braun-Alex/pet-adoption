// App.js
import React from 'react';
import { BrowserRouter, Route, Routes} from 'react-router-dom';
import Home from './Pages/Home';
import Contacts from './Pages/Contacts';
import Donate from './Pages/Donate';
import Login from './Pages/Login';
import Signup from './Pages/Signup';
import Header from './Components/Header';

import ShelterAcc from './Pages/ShelterAcc'
import './App.css';
import './css/Signup.css'
import './css/ShelterAcc.css'

function App() {
  return (
    
      <div>
      <Header />
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/donate' element={<Donate />} />
        <Route path='/contacts' element={<Contacts />} />
        <Route path='/login' element={<Login />} />
        <Route path='/signup' element={<Signup />} />
        <Route path='/shelter-account'  element={<ShelterAcc />} />
      </Routes>  
      </div>
    
  );
}

export default App;