import React, { Component } from 'react';
import catImage from '../img/cat.jpg';
import dogImage from '../img/dog.jpg';
import { AuthContext } from '../Contexts/AuthContext';
import axios from 'axios';
import { toast } from "react-toastify";
import Swal from "sweetalert2";

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
            await Swal.fire({
                title: 'Ви впевнені, що хочете подати заявку на прихисток даної тваринки?',
                text: 'Тваринка - це велика відповідальність. Ви маєте це усвідомлювати',
                icon: 'question',
                showConfirmButton: true,
                confirmButtonText: 'Так, подати заявку',
                showCancelButton: true,
                cancelButtonText: 'Ні, відмінити подання'
            }).then(async (finalResult) => {
                if (finalResult.isConfirmed) {
                    await axios.post(`${process.env.REACT_APP_BACKEND_HOSTNAME}/api/v1/applications/create`, {
                        shelter_id: animal.shelter_id,
                        user_id: user.userID,
                        animal_id: animal.id
                    });
                    await tryLoginUser();
                    this.setState( { showAnimal: false } );
                    await Swal.fire({
                        title: 'Заявку на прихисток подано успішно!',
                        icon: 'success',
                        showConfirmButton: false,
                        timer: 5000,
                        timerProgressBar: true
                    });
                } else if (finalResult.isDismissed) {
                    await Swal.fire({
                        title: 'Подачу заявки на прихисток відхилено!',
                        icon: 'error',
                        showConfirmButton: false,
                        timer: 5000,
                        timerProgressBar: true
                    });
                }
            });
        } catch (error) {
            if (error.response) {
                toast.error("Сервер відхилив виконання запиту на прихисток тваринки!");
            } else if (error.request) {
                toast.error("Сервер не відповідає на запити!");
            } else {
                toast.error("Щось пішло не так: " + error.message);
            }
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
