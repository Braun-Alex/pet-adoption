import React from 'react';
import { Link } from 'react-router-dom';
import "../css/Menu.css"

const Menu = ({menuActive, setMenuActive}) => {
    return (
        <div className={menuActive ? "menu active" : "menu"} onClick={() => setMenuActive(false)}>
            <div className='blur'/>
            <div className='menu-content'>
                <Link to="/" className="menu-item">Головна</Link>
                <Link to="/donate" className="menu-item">Допомогти</Link>
                <Link to="/contacts" className="menu-item">Контакти</Link>
            </div>
        </div>
    );
}

export default Menu;