import React, {useContext} from 'react';
import {Context} from "../index";
import AnimalTableItem from "./AnimalTableItem";
import "../css/AnimalMain.css"

const AnimalTable = () => {
    const {db} = useContext(Context)

    return (
        <div className="animal-table">
            {db.animals.map(animal =>
                <AnimalTableItem key={animal.id} animal={animal}/>
            )}
        </div>
    );
};

export default AnimalTable;
