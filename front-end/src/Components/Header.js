import React, {useContext} from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from "../Contexts/AuthContext";
import '../css/Header.css';

function Header() {
    const { isAuthenticated, entityType, entityName, logout } = useContext(AuthContext);
    let registrationPath;
    {entityType === "shelter" ? registrationPath = '/shelter-account': registrationPath = '/user-account'}
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
                        <Link to={registrationPath} className="userName-header">{entityName}</Link>
                        <Link to="/" className="logout-button" onClick={logout}>Вийти</Link>
                    </>
                ): (
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
