import React from 'react';
import { Link } from 'react-router-dom';
import Signup from '../Pages/Signup';

function Header() {
  return (
    <header>
        <div className="header-left">
          <a href="/">Головна</a>
          <a href="/donate">Допомогти</a>
          <a href="/contacts">Контакти</a>
        </div>
        <div className="header-right">
              <button className="login-button">Увійти</button>
              
                  <button className="signup-button">Зареєструватися</button>
                      
        </div>   
        
    </header>
    
  );
}

export default Header;