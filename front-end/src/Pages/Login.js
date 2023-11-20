import React, { Component } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      userEmail: '',
      userPassword: '',
      errorMessage: ''
    };

    this.handleInputChange = this.handleInputChange.bind(this);
    this.loginUser = this.loginUser.bind(this);
  }

  handleInputChange(e) {
    const { name, value } = e.target;
    this.setState({ [name]: value });
  }

    setAuthHeader(accessToken) {
        axios.defaults.headers.common['Authorization'] = accessToken ? `Bearer ${accessToken}` : '';
    }

  loginUser = (e) => {
      e.preventDefault();

      const { userEmail, userPassword } = this.state;
      const AUTH_API_URL = 'http://127.0.0.1:8000/user/login';
      const formData = new URLSearchParams();

      formData.append('username', userEmail);
      formData.append('password', userPassword);

      axios.post(AUTH_API_URL, formData).then(response => {
          console.log('Авторизація пройшла успішно:', response.data);
          localStorage.setItem('access_token', response.data.access_token);
          localStorage.setItem('refresh_token', response.data.refresh_token);
          this.setAuthHeader(response.data.access_token);
          this.setState({ errorMessage: 'Авторизація пройшла успішно' });
      }).catch((error) => {
          console.error('Введено некоректну електронну пошту або пароль.', error.message);
          this.setState({ errorMessage: 'Введено некоректну електронну пошту або пароль' });
      });
  }

  render() {
    const { userEmail, userPassword, errorMessage } = this.state;

    return (
      <>
        <h1 className="form-header">ВХІД</h1>

        <div className="form">
          <form className="login-form" onSubmit={this.loginUser}>
            <div className="form-field">
              <label>Електронна адреса</label>
              <input
                type="email"
                name="userEmail"
                value={userEmail}
                onChange={this.handleInputChange}
              />
            </div>

            <div className="form-field">
              <label>Пароль</label>
              <input
                type="password"
                name="userPassword"
                value={userPassword}
                onChange={this.handleInputChange}
              />
            </div>

            {errorMessage && <div className="error-message">{errorMessage}</div>}

            <button type="submit" className="button-login">Увійти</button>
          </form>
        </div>
      </>
    );
  }
}

export default Login;
