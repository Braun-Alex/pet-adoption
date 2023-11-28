import React from 'react';
import catImage from '../img/cat.jpg'; // Шлях до зображення кота
import dogImage from '../img/dog.jpg'; // Шлях до зображення собаки

const AnimalTableItem = ({animal}) => {
    const animalImage = animal.type == 'кіт' ? catImage : dogImage;

    return (
        <div>
            <div className='animal-item'>
                <div>{animal.name}</div>
                <div class="animal-photo">
                    <img src={animalImage} alt={`Фото ${animal.type}`}/>
                </div>
                <div className="grup-animal-info">
                    <div>Вид тваринки: {animal.type}</div>
                    <div>Стать: {animal.sex}</div>
                    <div>Дата народження: {animal.month+"."+animal.year}</div>
                    <div>Деталі: {animal.description}</div>
                </div>
                <botton className="animal-info-button">Подати заявку</botton>
            </div>
        </div>
    );
};

export default AnimalTableItem;