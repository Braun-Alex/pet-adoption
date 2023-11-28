import React, { useState, useEffect } from 'react';
import axios from 'axios';
import AnimalTableItem from "./AnimalTableItem";
import "../css/AnimalMain.css"

const AnimalTable = () => {
    const [animals, setAnimals] = useState([]); // Стан для зберігання даних про тварин

    useEffect(() => {
        // Функція для завантаження даних про тварин
        const fetchAnimals = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8080/api/v1/animals/all'); // URL вашого API
                console.log(response);
                setAnimals(response.data); // Оновлення стану тварин даними з сервера
            } catch (error) {
                console.error('Помилка при завантаженні даних про тварин:', error);
            }
        };

        fetchAnimals();
    }, []);

    return (
        <div className="animal-table">
            {animals.map(animal =>
                <AnimalTableItem key={animal.id} animal={animal}/>
            )}
        </div>
    );
};

export default AnimalTable;
