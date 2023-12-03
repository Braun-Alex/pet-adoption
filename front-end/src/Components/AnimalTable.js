import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import { AuthContext } from "../Contexts/AuthContext";
import AnimalTableItem from "./AnimalTableItem";
import "../css/AnimalMain.css";

const AnimalTable = () => {
    const { user, userApplications, tryLoginUser } = useContext(AuthContext);
    const [animals, setAnimals] = useState([]);

    useEffect(() => {
        const fetchAnimals = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8080/api/v1/animals/all');
                console.log(response);
                await tryLoginUser();
                let allAnimals = [];
                if (user && userApplications) {
                    response.data.forEach((animal) => {
                        let isUserAnimal = false;
                        userApplications.forEach((application) => {
                            if (application.animal_id === animal.id) {
                                isUserAnimal = true;
                            }
                        })
                        if (!isUserAnimal) {
                            allAnimals.push(animal);
                        }
                    })
                    setAnimals(allAnimals);
                } else {
                    setAnimals(response.data);
                }
            } catch (error) {
                console.error('Помилка при завантаженні даних про тварин:', error);
            }
        };

        fetchAnimals();
    }, []);

    if (animals.length !== 0) {
        return (
            <div className="animal-table">
                {animals.map(animal =>
                    <AnimalTableItem key={animal.id} animal={animal}/>
                )}
            </div>
        );
    } else {
        return (
            <div>Тваринки для прихистку є відсутніми.</div>
        )
    }
};

export default AnimalTable;
