import React, {createContext} from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import DB from './DB/DB';
import { AuthProvider } from './Contexts/AuthContext';

export const Context = createContext(null);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <AuthProvider>
  <Context.Provider value={{
    db: new DB(),
  }}>
    <BrowserRouter>
    <Routes>
      <Route path="/*" element={<App />} />
    </Routes>
  </BrowserRouter>
  </Context.Provider>
    </AuthProvider>
);
reportWebVitals();
