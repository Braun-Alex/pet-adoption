import React, { Component } from 'react';
import catImage from '../img/cat.jpg';
import dogImage from '../img/dog.jpg';
import { AuthContext } from '../Contexts/AuthContext';
import axios from 'axios';

class AnimalTableItem extends Component {
    static contextType = AuthContext;

    constructor(props) {
        super(props);

        this.state = {
            showAnimal: true
        };

        this.handleSubmitApplication = this.handleSubmitApplication.bind(this);
    }

    handleSubmitApplication = async () => {
        const { user, tryLoginUser } = this.context;
        const { animal } = this.props;

        try {
            await axios.post('http://127.0.0.1:8080/api/v1/applications/create', {
                shelter_id: animal.shelter_id,
                user_id: user.userID,
                animal_id: animal.id
            });
            await tryLoginUser();
            this.setState( { showAnimal: false } );
            alert('Заявку подано успішно!');
        } catch (error) {
            alert('Сталася помилка при подачі заявки.');
        }
    }

    render() {
        const { showAnimal } = this.state;
        const { animal } = this.props;
        const { user } = this.context;
        const animalImage = animal.type === 'кіт' ? catImage : dogImage;

        return (
            <div className='animal-item-container'>
                {showAnimal && (
                    <div className='animal-item'>
                        <div>{animal.name}</div>
                        <div>
                            <img src={animalImage} alt={'Фото ' + animal.type} className="animal-photo"/>
                        </div>
                        <div className="grup-animal-info">
                            <div>Вид тваринки: {animal.type}</div>
                            <div>Стать: {animal.sex}</div>
                            <div>Дата народження: {animal.month + "." + animal.year}</div>
                            <div>Деталі: {animal.description}</div>
                        </div>
                        {user && (
                            <button className="animal-info-button" onClick={this.handleSubmitApplication}>Подати заявку</button>
                        )}
                    </div>
                )}
            </div>
        );
    }
}

export default AnimalTableItem;
