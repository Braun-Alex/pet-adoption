import React, { Component } from 'react';
import axios from 'axios';
import { AuthContext } from '../Contexts/AuthContext';
import { withoutAuth } from '../Wrappers/WithoutAuth';
import { toast } from "react-toastify";
import "../css/Auth.css";

class Login extends Component {
    static contextType = AuthContext;

    constructor(props) {
        super(props);
        this.state = {
            showUserAuth: true,
            showShelterAuth: false,
            registrationPath: '/user-account',
            email: '',
            password: '',
            errorMessage: ''
        };

        this.handleInputChange = this.handleInputChange.bind(this);
        this.login = this.login.bind(this);
    }

    toggleUser = () => {
        this.setState({
            showUserAuth: true,
            showShelterAuth: false,
            registrationPath: '/user-account',
        });
    }

    toggleShelter = () => {
        this.setState({
            showUserAuth: false,
            showShelterAuth: true,
            registrationPath: '/shelter-account',
        });
    }

    handleInputChange = (field, value) => {
        this.setState({ [field]: value } );
    }

    login = async (event) => {
        event.preventDefault();

        const { saveTokens, tryLoginUser, tryLoginShelter } = this.context;
        const { email, password, showUserAuth } = this.state;

        if (email === '' || password === '') {
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

        const formData = new URLSearchParams();
        formData.append('username', email);
        formData.append('password', password);

        const entity = showUserAuth ? 'users' : 'shelter';
        const AUTH_API_URL = `${process.env.BACKEND_HOSTNAME}:${process.env.BACKEND_PORT}/api/v1/${entity}/login`;

        try {
            const response = await axios.post(AUTH_API_URL, formData);
            saveTokens(response.data);
            const successAuth = showUserAuth ? await tryLoginUser(): await tryLoginShelter();
            if (successAuth) {
                toast.success("Вас успішно авторизовано!");
            }
        } catch (error) {
            if (error.response) {
                toast.error("Введено некоректні автентифікаційні дані!");
            } else if (error.request) {
                toast.error("Сервер не відповідає на запити!");
            } else {
                toast.error("Щось пішло не так: " + error.message);
            }
        }
    }

    render() {
        const { email, password } = this.state;

        return (
            <>
                <h1 className="form-header">ВХІД</h1>

                <div className="form">
                    <button className={`${this.state.showUserAuth ? 'activeToggle' : 'inactiveToggle'}`} onClick={this.toggleUser}>Користувач</button>
                    <button className={`${this.state.showShelterAuth ? 'activeToggle' : 'inactiveToggle'}`} onClick={this.toggleShelter}>Притулок</button>
                    <form className="login-form" onSubmit={this.login}>
                        <div className="form-field">
                            <label>Електронна адреса</label>
                            <input
                                type="email"
                                value={email}
                                onChange={(event) => this.handleInputChange('email', event.target.value)}
                            />
                        </div>

                        <div className="form-field">
                            <label>Пароль</label>
                            <input
                                type="password"
                                value={password}
                                onChange={(event) => this.handleInputChange('password', event.target.value)}
                            />
                        </div>

                        <button type="submit" className="button-login">Увійти</button>
                    </form>
                </div>
            </>
        );
    }
}

export default withoutAuth(Login);
