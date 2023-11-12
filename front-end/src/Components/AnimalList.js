import React, {useContext} from 'react';
import { Context } from "../index";
import '../css/List.css';

const AnimalList = () => {
    const { db } = useContext(Context);
    const filteredAnimals = db.animals.filter(anim => anim.shelterId === 2);
    return (
        <ul>
            {filteredAnimals.map(animal =>
                <li key={animal.id} class="request">
                    {animal.name}
                </li>
                )}
        </ul>
    );
}
export default AnimalList;