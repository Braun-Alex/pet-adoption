import React from 'react';
import { Link } from 'react-router-dom';
var isAuthenticated = true;
var username = "ім'я користувача";

function Header({showButton}) {
  return (
    <header>
      <div className="header-left">
        <Link to="/"><a>Головна</a></Link>          
        <Link to="/donate"><a>Допомогти</a></Link>
        <Link to="/contacts"><a>Контакти</a></Link>
      </div>
      
      <div className="header-right">
        {isAuthenticated ? (
          <>
            <span className="userName-header"> {username} </span>
            <button className="logout-button"> Вийти </button>
          </>
        ) : (
          <>
            <Link to="/login">
              <a className="login-button">Увійти</a>
            </Link>
            <Link to="/signup">
              <a className="signup-button">Зареєструватися</a>
            </Link>
          </>
        )}
      </div>
    </header>
    
  );
}

export default Header;