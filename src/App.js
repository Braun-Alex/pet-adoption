import React from 'react';
import { Route, Routes } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import Home from './Pages/Home';
import Contacts from './Pages/Contacts';
import Donate from './Pages/Donate';
import Login from './Pages/Login';
import Signup from './Pages/Signup';
import Header from './Components/Header';
import UserAcc from './Pages/UserAcc';
import ShelterAcc from './Pages/ShelterAcc';
import Animal from './Pages/Animal';
import AnimalMain from './Pages/AnimalMain';
import './App.css';
import 'react-toastify/dist/ReactToastify.css';

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
              <Route path='/user-account' element={<UserAcc />} />
              <Route path='/shelter-account' element={<ShelterAcc />} />
              <Route path="/animal/:animalId" element={<Animal />} />
              <Route path="/animal-main" element={<AnimalMain />} />
          </Routes>
          <ToastContainer position="top-center" autoClose={5000} />
      </div>
  );
}

export default App;
