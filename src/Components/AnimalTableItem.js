import React, { Component } from 'react';
import { AuthContext } from '../Contexts/AuthContext';
import axios from 'axios';
import { toast } from 'react-toastify';
import Swal from 'sweetalert2';
import AnimalDetailsModal from './AnimalDetailsModal';
import '../css/AnimalMain.css';

class AnimalTableItem extends Component {
    static contextType = AuthContext;

    constructor(props) {
        super(props);

        this.state = {
            showAnimal: true,
            animalDetails: false
        };

    }

    setAnimalDetails = (isVisible) => {
        this.setState({ animalDetails: isVisible });
    }

    render() {
        const { showAnimal, animalDetails } = this.state;
        const { animal } = this.props;

        return (
            <div>
                {showAnimal && (
                    <>
                        <div className='animal-item' onClick={() => this.setAnimalDetails(true)}>
                            <div>{animal.name}</div>
                            <div className="animal-photo-container">
                                <img src={animal.photo} alt={'Фотографія ' + animal.type} className="animal-photo"/>
                            </div>
                            <div className="group-animal-info">
                                <div>Вид тваринки: {animal.type}</div>
                                <div>Стать: {animal.sex}</div>
                                <div>Дата народження: {animal.month + "." + animal.year}</div>
                            </div>
                            
                        </div>
                        {animalDetails && (<AnimalDetailsModal animal={animal}
                                                               showAnimalDetails={animalDetails}
                                                               closeModal={() => {this.setAnimalDetails(false);}}/>
                                                             )}
                                                             
                    </>
                )}
            </div>
        );
    }
}

export default AnimalTableItem;
