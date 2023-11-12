// App.js
import React from 'react';
import { BrowserRouter, Route, Routes} from 'react-router-dom';
import Home from './Pages/Home';
import Contacts from './Pages/Contacts';
import Donate from './Pages/Donate';
import Login from './Pages/Login';
import Signup from './Pages/Signup';
import Header from './Components/Header';
import './App.css';
import './css/Signup.css'

function App() {
  return (
    
      <div>
      <Header />
      <Routes>
          <Route path='/signup' element={<Signup />}/>
      </Routes>  
      </div>
    
  );
}

export default App;