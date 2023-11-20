import React from 'react';
import { Link } from 'react-router-dom';

function Header({isAuthenticated, username, handleLogout, usertype}) {
  var registrationPath = '';
  {usertype == "shelter" ? registrationPath = '/shelter-account' : registrationPath = '/user-account'}
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
            <Link to={registrationPath} className="userName-header">{username}</Link>
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
