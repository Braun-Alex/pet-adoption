import React from 'react';
import '../css/AnimalMain.css';
import AnimalTable from "../Components/AnimalTable.js"

const AnimalMain = () => {
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
