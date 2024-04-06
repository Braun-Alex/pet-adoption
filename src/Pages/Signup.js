import React, { Component } from 'react';
import axios from 'axios';
import { withoutAuth } from '../Wrappers/WithoutAuth';
import { toast } from 'react-toastify';
import Swal from 'sweetalert2';
import "../css/Auth.css"

class Signup extends Component {
    constructor(props) {
        super(props);
        this.state = {
            showUserReg: true,
            showShelterReg: false,
            registrationPath: '/user-account',
            name: '',
            email: '',
            password: ''
        };
    }

    toggleUser = () => {
        this.setState({
            showUserReg: true,
            showShelterReg: false,
            registrationPath: '/user-account',
        });
    }

    toggleShelter = () => {
        this.setState({
            showUserReg: false,
            showShelterReg: true,
            registrationPath: '/shelter-account',
        });
    }

    handleInputChange = (field, value) => {
        this.setState({ [field]: value });
    }

    register = () => {
        const { name, email, password } = this.state;

        if (name === '' || email === '' || password === '') {
            toast.error("Всі поля є обов'язковими до заповнення!");
            return;
        }

        const EMAIL_REGEX = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;

        if (!EMAIL_REGEX.test(email)) {
            toast.error("Введено некоректний формат електронної пошти!");
            return;
        }

        const PASSWORD_MINIMAL_LENGTH = 9;

        if (password.length < PASSWORD_MINIMAL_LENGTH) {
            toast.error("Пароль має містити не менше 9 символів!");
            return;
        }

        let entity;
        let entityData;
        const { showUserReg, showShelterReg } = this.state;

        if (showUserReg) {
            entity = 'users';
            entityData = {
                full_name: name,
                email: email,
                password: password
            }
        } else if (showShelterReg) {
            entity = 'shelter';
            entityData = {
                name: name,
                email: email,
                password: password
            }
        }

        const SIGNUP_API_URL = `${process.env.REACT_APP_BACKEND_HOSTNAME}/api/v1/${entity}/signup`;

        axios.post(SIGNUP_API_URL, entityData).then(async () => {
            await Swal.fire({
                title: 'Вітаємо, ' + name + ', Вас успішно зареєстровано!',
                icon: 'success',
                showConfirmButton: false,
                timer: 5000,
                timerProgressBar: true
            });
            this.props.navigate("/login");
        }).catch((error) => {
            if (error.response) {
                toast.error("Користувач із такою електронною поштою вже існує!");
            } else if (error.request) {
                toast.error("Сервер не відповідає на запити!");
            } else {
                toast.error("Щось пішло не так: " + error.message);
            }
        });
    }


    render() {
        return (
            <>
                <h1 className="form-header">РЕЄСТРАЦІЯ</h1>

                <div className="form">

                    <button className={`${this.state.showUserReg ? 'activeToggle' : 'inactiveToggle'}`} onClick={this.toggleUser}>Користувач</button>
                    <button className={`${this.state.showShelterReg ? 'activeToggle' : 'inactiveToggle'}`} onClick={this.toggleShelter}>Притулок</button>

                    {this.state.showUserReg &&
                        <form className="registration-form">

                            <div className="form-field">
                                <label>Ім'я користувача</label>
                                <input
                                    type="text"
                                    onChange={(event) => this.handleInputChange('name', event.target.value)}
                                />
                            </div>

                            <div className="form-field">
                                <label>Електронна адреса</label>
                                <input
                                    type="email"
                                    onChange={(event) => this.handleInputChange('email', event.target.value)}
                                />
                            </div>

                            <div className="form-field">
                                <label>Пароль</label>
                                <input
                                    type="password"
                                    onChange={(event) => this.handleInputChange('password', event.target.value)}
                                />
                            </div>

                        </form>}


                    {this.state.showShelterReg && <form className="registration-form">

                        <div className="form-field">
                            <label>Ім'я притулку</label>
                            <input type="text"
                            onChange={(event) => this.handleInputChange('name', event.target.value)}/>
                        </div>

                        <div className="form-field">
                            <label>Електронна адреса</label>
                            <input type="email"
                            onChange={(event) => this.handleInputChange('email', event.target.value)} />
                        </div>

                        <div className="form-field">
                            <label>Пароль</label>
                            <input type="password"
                            onChange={(event) => this.handleInputChange('password', event.target.value)} />
                        </div>

                    </form>}

                    <button className="button-reg" onClick={this.register}>Зареєструватися</button>

                </div>
            </>
        );
    }
}


export default withoutAuth(Signup);
