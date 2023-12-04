import React, { Component } from 'react';
import catImage from '../img/cat.jpg'; // Шлях до зображення кота
import dogImage from '../img/dog.jpg'; // Шлях до зображення собаки
import { AuthContext } from '../Contexts/AuthContext';
import { withAuth } from '../Wrappers/WithAuth';
import axios from 'axios';

class AnimalTableItem extends Component {
    static contextType = AuthContext;

    handleSubmitApplication = async () => {
        const { user } = this.context;
        const { animal } = this.props;

        try {
            const response = await axios.post('http://127.0.0.1:8080/api/v1/applications/create', {
                shelter_id: animal.shelter_id,
                user_id: user.userID,
                animal_id: animal.id
            });
            console.log(response.data);
            alert('Заявку подано успішно!');
        } catch (error) {
            console.error('Помилка при подачі заявки:', error);
            alert('Сталася помилка при подачі заявки.');
        }
    }
    
    render() {
        const { animal } = this.props;
        const animalImage = animal.type === 'кіт' ? catImage : dogImage;

        return (
            <div className='animal-item-container'>
                <div className='animal-item'>
                    <div>{animal.name}</div>
                    <div >
                        <img src={animalImage} alt={'Фото ' + animal.type} className="animal-photo"/>
                    </div>
                    <div className="grup-animal-info">
                        <div>Вид тваринки: {animal.type}</div>
                        <div>Стать: {animal.sex}</div>
                        <div>Дата народження: {animal.month + "." + animal.year}</div>
                        <div>Деталі: {animal.description}</div>
                    </div>
                    <button className="animal-info-button" onClick={this.handleSubmitApplication}>Подати заявку</button>
                </div>
            </div>
        );
    }
}

export default withAuth(AnimalTableItem);
