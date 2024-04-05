import React, { Component } from 'react';
import Modal from 'react-modal';
import '../css/AnimalDetailsModal.css';
import axios from 'axios';
import { toast } from 'react-toastify';
import Swal from 'sweetalert2';
import { AuthContext } from '../Contexts/AuthContext';

class AnimalDetailsModal extends Component {
    static contextType = AuthContext;

    constructor(props) {
        super(props);
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
                        timer: 1000,
                        // timerProgressBar: true
                    });
                } else if (finalResult.isDismissed) {
                    await Swal.fire({
                        title: 'Подачу заявки на прихисток відхилено!',
                        icon: 'error',
                        showConfirmButton: false,
                        timer: 1000,
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
        const { animal, showAnimalDetails, closeModal } = this.props;
        const { user } = this.context;
        return (
                <div className="animal-details-overlay">
                    <Modal
                        isOpen={showAnimalDetails}
                        onRequestClose={closeModal}
                        className="animal-details-modal"
                        centered
                    >
                        <div className="animal-details-modal-content">
                            <span className="animal-details-close" onClick={closeModal}>&times;</span>
                            
                            <div>
                                <h3>{animal.name}</h3>

                                    <img src={animal.photo} alt={'Фото ' + animal.type} className="animal-details-photo-modal"/>

                               
                                <p><strong>Вид тваринки:</strong> {animal.type}</p>
                                <p><strong>Стать:</strong> {animal.sex}</p>
                                <p><strong>Дата народження:</strong> {animal.month + "." + animal.year}</p>
                                <p><strong>Деталі:</strong> {animal.description}</p>
                            </div>
                        </div>
                        {user && (
                            <div className="create-appl-button-container">
                                {/* <button className="create-appl-button" onClick={() => { this.handleSubmitApplication(); closeModal(); }}>Подати заявку</button> */}
                                <button className="create-appl-button" onClick={this.handleSubmitApplication}>Подати заявку</button>
                            </div>
                        )}
                       
                    </Modal>
                </div>
        )
    }
}

export default AnimalDetailsModal;
