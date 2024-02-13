import React, { Component } from 'react';
import '../css/Modal.css'
import Modal from 'react-modal';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';
import { AuthContext } from '../Contexts/AuthContext';
import { withAuth } from '../Wrappers/WithAuth';
import axios from 'axios';
import { toast } from 'react-toastify';
import Swal from 'sweetalert2';

class CreateAnimal extends Component {
    static contextType = AuthContext;
    constructor(props) {
        super(props);
        this.state = {
            animalData: {
                name: '',
                type: '',
                sex: '',
                month: '',
                year: '',
                description: '',
                shelter_id: 0
            }
        };
    }

    handleInputChange = (field, value) => {
        this.setState(prevState => ({
            animalData: { ...prevState.animalData, [field]: value }
        }));
    };

    registerAnimal = async () => {
        const { name, type, sex, month, year, description } = this.state.animalData;
        const API_URL = 'http://127.0.0.1:8080/api/v1/animals/add';
        const { shelter } = this.context;
        const shelterId = shelter.shelterID;
        try {
            await Swal.fire({
                title: 'Ви впевнені, що хочете додати дану тваринку?',
                text: 'Впевніться, що всі дані про тваринку є достовірними',
                icon: 'question',
                showConfirmButton: true,
                confirmButtonText: 'Так, додати тваринку',
                showCancelButton: true,
                cancelButtonText: 'Ні, відмінити додавання'
            }).then(async (finalResult) => {
                if (finalResult.isConfirmed) {
                    await axios.post(API_URL, {
                        name,
                        type,
                        sex,
                        month,
                        year,
                        description,
                        shelter_id: shelterId
                    });
                    await Swal.fire({
                        title: 'Тваринку було успішно додано!',
                        icon: 'success',
                        showConfirmButton: false,
                        timer: 5000,
                        timerProgressBar: true
                    });
                } else if (finalResult.isDismissed) {
                    await Swal.fire({
                        title: 'Додавання тваринки було скасовано!',
                        icon: 'error',
                        showConfirmButton: false,
                        timer: 5000,
                        timerProgressBar: true
                    });
                }
            });
            this.props.onHide();
        } catch (error) {
            if (error.response) {
                toast.error("Сервер відхилив виконання запиту на додавання тваринки!");
            } else if (error.request) {
                toast.error("Сервер не відповідає на запити!");
            } else {
                toast.error("Щось пішло не так: " + error.message);
            }
        }
    };

    render() {
        const { show, onHide } = this.props;

        const modalStyles = {
            display: show ? 'block' : 'none',
        };
        const overlayStyles = {
            display: show ? 'block' : 'none',
        };

        const types = ['кіт', 'пес'];
        const sex = ['хлопчик', 'дівчинка'];
        const mounths = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'];
        const years = ['2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015'];
        const defaultOption = null;

        return (
            <>
                <div className="overlay" style={overlayStyles}>
                    <Modal
                        isOpen={show}
                        onRequestClose={onHide}
                        className="modal"
                        style={modalStyles}
                        centered
                    >
                        <div className='modal-content'>
                            <span className="close" onClick={onHide}>&times;</span>

                            <div>
                                <div className="add-animal-header">
                                    Додати тваринку
                                </div>
                            </div>

                            <div>
                                <form className='add-animal-container'>
                                    <div className="animal-name">
                                        <label>Ім'я тваринки</label>
                                        <input type="text" onChange={(e) => this.handleInputChange('name', e.target.value)}/>
                                    </div>

                                    <div>
                                        <Dropdown
                                            options={types}
                                            value={defaultOption}
                                            placeholder="вид тваринки"
                                            className="animal-type"
                                            onChange={(option) => this.handleInputChange('type', option.value)}
                                        />
                                    </div>

                                    <div>
                                        <Dropdown
                                            options={sex}
                                            value={defaultOption}
                                            placeholder="стать"
                                            className="animal-sex"
                                            onChange={(option) => this.handleInputChange('sex', option.value)}/>
                                    </div>

                                    <div class="select-date" >
                                        <Dropdown options={mounths}
                                                  value={defaultOption}
                                                  placeholder="місяць"
                                                  onChange={(option) => this.handleInputChange('month', option.value)}/>
                                        <Dropdown
                                            options={years}
                                            value={defaultOption}
                                            placeholder="рік"
                                            className='year'
                                            onChange={(option) => this.handleInputChange('year', option.value)}/>
                                    </div>

                                    <div className="animal-desc">
                                        <label>Опис</label>
                                        <textarea rows="4" onChange={(e) => this.handleInputChange('description', e.target.value)}></textarea>
                                    </div>
                                </form>
                            </div>

                            <button className="create-animal-button" onClick={this.registerAnimal}>Додати</button>
                        </div>
                    </Modal>
                </div>
            </>
        )
    }
}

export default withAuth(CreateAnimal);
