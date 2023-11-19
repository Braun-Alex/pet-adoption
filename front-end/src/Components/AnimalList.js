import React, {useContext, useState} from 'react';
import { Context } from "../index";
import '../css/List.css';
import CreateAnimal from "./CreateAnimal";
import { Link } from 'react-router-dom';

const currentShelterId = 2;

const AnimalList = () => {
    const [createAnimalVisible, setCreateAnimalVisible] = useState(false);
    const { db } = useContext(Context);
   
    const filteredAnimals = db.animals.filter(anim => anim.shelterId === currentShelterId);
    return (
        <div class="animal-from-shelter">
            <button
                onClick={() => setCreateAnimalVisible(true)}
                className='add-animal-button'
            >
                Додати нову тваринку
            </button>
            <CreateAnimal show={createAnimalVisible} onHide={() => setCreateAnimalVisible(false)}/>
            <ul class="list">
                {filteredAnimals.map(animal =>
                    <Link to={`/animal/${animal.id}`}>
                        <li key={animal.id} class="list-item">
                     {animal.name}
                </li>
                </Link>
                
                )}
            </ul>
            
        </div>
        
    );
}
export default AnimalList;