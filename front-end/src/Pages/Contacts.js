import React, { Component } from 'react';
import axios from 'axios';

class Contacts extends Component {
    constructor(props) {
        super(props);
        this.state = {
            accessToken: localStorage.getItem('access_token'),
            userData: ''
        };

        this.setAuthHeader(this.state.accessToken);
        this.getUserData = this.getUserData.bind(this);
        this.refreshAuthentication = this.refreshAuthentication.bind(this);
    }

    componentDidMount() {
        this.getUserData();
    }

    setAuthHeader(accessToken) {
        axios.defaults.headers.common['Authorization'] = accessToken ? `Bearer ${accessToken}` : '';
    }

    getUserData() {
        axios.get('http://127.0.0.1:8080/api/v1/users/profile').then(response => {
            console.log('Дані про користувача успішно отримано:', response.data);
            this.setState({ userData: response.data });
        }).catch(error => {
            if (!this.state.accessToken) {
                this.refreshAuthentication().then(success => {
                    if (success) {
                        this.getUserData();
                    } else {
                        console.log('Неавторизований доступ до захищеного ресурсу без жодного токена авторизації');
                    }
                });
            } else {
                console.error('Неавторизований доступ до захищеного ресурсу із невалідним токеном авторизації.', error.message);
            }
        });
    }

    refreshAuthentication() {
        const refreshToken = localStorage.getItem('refreshToken');
        return axios.post('http://127.0.0.1:8000/token/refresh', { refresh_token: refreshToken }).then(response => {
            console.log('Токен авторизації було успішно оновлено:', response.data);
            localStorage.setItem('access_token', response.data.access_token);
            this.setAuthHeader(response.data.access_token);
            return true;
        }).catch(error => {
            console.error('Неавторизований доступ до захищеного ресурсу.', error.message);
            return false;
        });
    }

    render() {
        const { userData } = this.state;
        return (<div>Дані користувача: {userData}</div>)
    }
}

export default Contacts;
