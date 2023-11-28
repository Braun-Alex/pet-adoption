import React from 'react';

const AnimalTableItem = ({animal}) => {
    return (
        <div>
            <div className='animal-item'>
                <div>{animal.name}</div>
                <div class="animal-photo">фото тваринки</div>
                <div className="grup-animal-info">
                    <div>Тип тварини: {animal.sex}</div>
                    <div>Вид тваринки: {animal.type}</div>
                    <div>Вік: {animal.age}</div>
                </div>
                <botton className="animal-info-button">Подати заявку</botton>
                
            </div>
        </div>
    );
};

export default AnimalTableItem;