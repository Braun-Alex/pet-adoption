import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import { AuthContext } from "../Contexts/AuthContext";
import AnimalTableItem from "./AnimalTableItem";
import "../css/AnimalMain.css";
import { toast } from "react-toastify";

const AnimalTable = () => {
    const { user, userApplications, tryLoginUser } = useContext(AuthContext);
    const [animals, setAnimals] = useState([]);

    useEffect(() => {
        const fetchAnimals = async () => {
            try {
                const response = await axios.get(`${process.env.REACT_APP_BACKEND_HOSTNAME}:${process.env.REACT_APP_BACKEND_PORT}/api/v1/animals/all`);
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
                if (error.response) {
                    toast.error(`Сервер відхилив у запиті на завантаження даних про тваринок на головній сторінці. Back-End hostname: ${process.env.REACT_APP_BACKEND_HOSTNAME}, Back-End port: ${process.env.REACT_APP_BACKEND_PORT}, error: ` + error);
                } else if (error.request) {
                    toast.error(`Сервер не відповідає на запити. Back-End hostname: ${process.env.REACT_APP_BACKEND_HOSTNAME}, Back-End port: ${process.env.REACT_APP_BACKEND_PORT}, error: ` + error);
                } else {
                    toast.error(`Щось пішло не так. Back-End hostname: ${process.env.REACT_APP_BACKEND_HOSTNAME}, Back-End port: ${process.env.REACT_APP_BACKEND_PORT}, error: ` + error);
                }
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
            <div>Тваринки для прихистку відсутні.</div>
        )
    }
};

export default AnimalTable;
