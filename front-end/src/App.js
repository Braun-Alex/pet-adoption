// App.js
import React, { useState } from 'react';
import { BrowserRouter, Route, Routes, useNavigate} from 'react-router-dom';
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
  const navigate = useNavigate(); // Отримуємо функцію navigate

  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [username, setUsername] = useState("");

  const handleLoginSuccess = () => {
    setIsAuthenticated(true);
    navigate('/');
  };

  const handleLogout = () => {
    setIsAuthenticated(false);
    setUsername('');
    navigate('/login'); // Редірект на сторінку входу
  };

  return (
    
      <div>
      <Header isAuthenticated={isAuthenticated} handleLogout={handleLogout} username={username} />
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/donate' element={<Donate />} />
        <Route path='/contacts' element={<Contacts />} />
        <Route path='/login' element={<Login onLoginSuccess={handleLoginSuccess} />} />
        <Route path='/signup' element={<Signup />} />
        <Route path='/shelter-account'  element={<ShelterAcc />} />
      </Routes>  
      </div>
    
  );
}

export default App;