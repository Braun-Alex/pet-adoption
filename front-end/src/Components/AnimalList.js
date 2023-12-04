import React, { Component } from 'react';
import '../css/List.css';
import CreateAnimal from "./CreateAnimal";
import { Link } from 'react-router-dom';
import { AuthContext } from '../Contexts/AuthContext';
import { withShelterAuth } from '../Wrappers/WithShelterAuth';
import axios from 'axios';

class AnimalList extends Component {
    static contextType = AuthContext;

    constructor(props) {
      super(props);
      this.state = {
        createAnimalVisible: false,
        animals: [], // Стан для зберігання списку тварин
        }
    }

    componentDidMount() {
        this.fetchAnimals();
    }

    fetchAnimals = async () => {
        const { shelter } = this.context;
        const shelterId = shelter.shelterID; // ID притулку
        try {
            const response = await axios.get(`http://127.0.0.1:8080/api/v1/animals/get/?shelter_id=${shelterId}`);
            this.setState({ animals: response.data });
            console.log(this.state.animals);
        } catch (error) {
            console.error('Помилка при завантаженні даних:', error);
        }
    }

    setCreateAnimalVisible = (isVisible) => {
        this.setState({ createAnimalVisible: isVisible });
    }

    render() {
        const { createAnimalVisible } = this.state;

    return (
        <div class="animal-from-shelter">
            <button
                aria-controls=''
                onClick={() => this.setCreateAnimalVisible(true)}
                className='add-animal-button'
            >
                Додати нову тваринку
            </button>
            <CreateAnimal show={createAnimalVisible} onHide={() => {this.setCreateAnimalVisible(false); this.fetchAnimals();}}/>
            <ul class="list">
                {this.state.animals.map(animal =>
                    <Link to={`/animal/${animal.id}`} className="no-underline">
                        <li class="list-item">
                            <p><strong>Ім'я:</strong> {animal.name}</p>
                            <p><strong>Вид тваринки:</strong> {animal.type}</p>
                            <p><strong>Стать:</strong> {animal.sex}</p>
                            <p><strong>Місяць народження:</strong> {animal.month + "." + animal.year}</p>
                            <p><strong>Деталі:</strong> {animal.description}</p>
                        </li>
                    </Link>

                )}
            </ul>

        </div>
    );
    }

}
export default withShelterAuth(AnimalList);
