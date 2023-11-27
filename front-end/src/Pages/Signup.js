import React, { Component } from 'react';
import axios from 'axios';
import { withoutAuth } from '../Wrappers/WithoutAuth';

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
        let entity;
        let entityData;
        const { showUserReg, showShelterReg } = this.state;

        if (showUserReg) {
            entity = 'user';
            entityData = {
                full_name: name,
                email: email,
                password: password
            }
        } else if (showShelterReg) {
            entity = 'shelter';
            entityData = {
                shelter_name: name,
                email: email,
                password: password
            }
        }

        const SIGNUP_API_URL = `http://127.0.0.1:8000/${entity}/signup`;

        axios.post(SIGNUP_API_URL, entityData).then(response => {
            console.log('Реєстрацію пройдено успішно:', response.data);
            this.props.navigate("/login");
        }).catch(error => {
            console.error('Користувач із такою електронною поштою вже існує.', error.message);
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
                            <input type="text" />
                        </div>

                        <div className="form-field">
                            <label>Електронна адреса</label>
                            <input type="email" />
                        </div>

                        <div className="form-field">
                            <label>Пароль</label>
                            <input type="password" />
                        </div>

                    </form>}

                    <button className="button-reg" onClick={this.register}>Зареєструватися</button>

                </div>
            </>
        );
    }
}


export default withoutAuth(Signup);
