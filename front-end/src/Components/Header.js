import React, {useContext, useState} from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from "../Contexts/AuthContext";
import '../css/Header.css';
import Menu from './Menu';

function Header() {
    const [menuActive, setMenuActive] = useState(false);
    const { isAuthenticated, entityType, entityName, logout } = useContext(AuthContext);
    let registrationPath;
    {entityType === "shelter" ? registrationPath = '/shelter-account': registrationPath = '/user-account'}
    return (
        <>
            <header>
                <div className='header-container'>
                    <div className="mob-menu">
                    <div class="burger-btn" onClick={() => setMenuActive(!menuActive)}> 
                        <span/>
                    </div>
                    </div>

                    <div className="header-left">
                <Link to="/">Головна</Link>
                <Link to="/animal-main">Знайти друга</Link>
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
            </div>
        </header>        
            <Menu menuActive={menuActive} setMenuActive={setMenuActive}/>
        </>
        
    );
}

export default Header;
