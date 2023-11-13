import React from 'react';
import { Link } from 'react-router-dom';

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
          <Link to="/signup">
            <button className="signup-button">Зареєструватися</button>
          </Link> 
        </div>
    </header>
    
  );
}

export default Header;