import React, { Component } from 'react';
import axios from 'axios';
import { AuthContext } from '../Contexts/AuthContext';
import { withoutAuth } from '../Wrappers/WithoutAuth';
import "../css/Auth.css"

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

        const formData = new URLSearchParams();
        formData.append('username', email);
        formData.append('password', password);

        const entity = showUserAuth ? 'users' : 'shelter';
        const AUTH_API_URL = `http://127.0.0.1:8080/api/v1/${entity}/login`;

        try {
            const response = await axios.post(AUTH_API_URL, formData);
            saveTokens(response.data);
            const successAuth = showUserAuth ? await tryLoginUser(): await tryLoginShelter();
            if (successAuth) {
                console.log('Авторизацію пройшдено успішно:', response.data);
                this.setState({ errorMessage: 'Авторизацію пройдено успішно' });
            }
        } catch (error) {
            console.error('Введено некоректну електронну пошту або пароль.', error.message);
            this.setState({ errorMessage: 'Введено некоректну електронну пошту або пароль' });
        }
    }

    render() {
        const { email, password, errorMessage } = this.state;

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

                        {errorMessage && <div className="error-message">{errorMessage}</div>}

                        {/* <Link to={this.state.registrationPath}><button type="submit" className="button-reg" onClick={this.registerUser}>Увійти</button></Link> */}

                        <button type="submit" className="button-login">Увійти</button>
                    </form>
                </div>
            </>
        );
    }
}

export default withoutAuth(Login);
