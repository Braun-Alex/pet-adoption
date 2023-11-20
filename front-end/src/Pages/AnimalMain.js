import React, {useState, useContext} from 'react';
import { Link } from 'react-router-dom';
import '../css/AnimalMain.css';
import { Context } from "../index";
import AnimalTable from "../Components/AnimalTable.js"

const AnimalMain = () => {
    const { db } = useContext(Context);
    return (
        <div className="animal-main-container">     
            <div className='title-animal-main'>ЗНАЙТИ ДРУГА</div>

            <div className="animal-table-container">
                <AnimalTable/>
            </div>
        </div>
    );
};

export default AnimalMain;
