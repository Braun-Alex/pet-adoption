import React from 'react';
import { Link } from 'react-router-dom';
var isAuthenticated = false;
var username = "ім'я користувача";

function Header({ isAuthenticated, username, handleLogout }) {
  return (
    <header>
      <div className="header-left">
        <Link to="/">Головна</Link>          
        <Link to="/donate">Допомогти</Link>
        <Link to="/contacts">Контакти</Link>
      </div>
      
      <div className="header-right">
        {isAuthenticated ? (
          <>
            <span className="userName-header">{username}</span>
            <button className="logout-button" onClick={handleLogout}>Вийти</button>
          </>
        ) : (
          <>
            <Link to="/login" className="login-button">Увійти</Link>
            <Link to="/signup" className="signup-button">Зареєструватися</Link>
          </>
        )}
      </div>
    </header>
  );
}

export default Header;
