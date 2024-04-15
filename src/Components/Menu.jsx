import React from 'react';
import { Link } from 'react-router-dom';
import "../css/Menu.css"

const Menu = ({menuActive, setMenuActive}) => {
    return (
        <div className={menuActive ? "menu active" : "menu"} onClick={() => setMenuActive(false)}>
            <div className='blur'/>
            <div className='menu-content'>
                <Link to="/" className="menu-item">Головна</Link>
                <Link to="/animal-main" className="menu-item">Знайти друга</Link>
                <Link to="/donate" className="menu-item">Підтримати проєкт</Link>
            </div>
        </div>
    );
}

export default Menu;