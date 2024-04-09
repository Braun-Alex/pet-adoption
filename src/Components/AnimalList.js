import React, { Component } from 'react';
import '../css/List.css';
import CreateAnimal from './CreateAnimal';
import { AuthContext } from '../Contexts/AuthContext';
import { withShelterAuth } from '../Wrappers/WithShelterAuth';
import axios from 'axios';
import { toast } from 'react-toastify';

class AnimalList extends Component {
    static contextType = AuthContext;

    constructor(props) {
        super(props);
        this.state = {
            createAnimalVisible: false,
            animals: []
        }
    }

    componentDidMount() {
        this.fetchAnimals();
    }

    fetchAnimals = async () => {
        const { shelter } = this.context;
        const shelterId = shelter.shelterID;
        try {
            const response = await axios.get(`${process.env.REACT_APP_BACKEND_HOSTNAME}/api/v1/animals/get/?shelter_id=${shelterId}`);
            this.setState({ animals: response.data });
        } catch (error) {
            if (error.response) {
                toast.error("Сервер відхилив виконання запиту на завантаження даних про тваринок притулку!");
            } else if (error.request) {
                toast.error("Сервер не відповідає на запити!");
            } else {
                toast.error("Щось пішло не так: " + error.message);
            }
        }
    }

    setCreateAnimalVisible = (isVisible) => {
        this.setState({ createAnimalVisible: isVisible });
    }

    render() {
        const { createAnimalVisible } = this.state;

        return (
            <div className="animal-from-shelter">
                <button
                    aria-controls=''
                    onClick={() => this.setCreateAnimalVisible(true)}
                    className='add-animal-button'
                >
                    Додати нову тваринку
                </button>
                <CreateAnimal show={createAnimalVisible} onHide={() => {this.setCreateAnimalVisible(false); this.fetchAnimals();}}/>
                <ul className="list">
                    {this.state.animals.map(animal =>
                        <div className="no-underline">
                            <li className="list-item">
                                <p><strong>Ім'я:</strong> {animal.name}</p>
                                <p><strong>Фотографія:</strong></p>
                                <div>
                                    <img src={animal.photo} alt={'Фото ' + animal.type} className="animal-photo" />
                                </div>
                                <p><strong>Вид тваринки:</strong> {animal.type}</p>
                                <p><strong>Стать:</strong> {animal.sex}</p>
                                <p><strong>Місяць народження:</strong> {animal.month + "." + animal.year}</p>
                                <p><strong>Деталі:</strong> {animal.description}</p>
                            </li>
                        </div>
                    )}
                </ul>

            </div>
        );
    }
}

export default withShelterAuth(AnimalList);
