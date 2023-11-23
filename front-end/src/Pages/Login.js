import React, { useContext, Component } from 'react';
import axios from 'axios';
import { AuthContext } from '../Contexts/AuthContext';
import {useNavigate} from "react-router-dom";

class Login extends Component {
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
  handleInputChange(e) {
    const { name, value } = e.target;
    this.setState({ [name]: value });
  }

    setAuthHeader(accessToken) {
        axios.defaults.headers.common['Authorization'] = accessToken ? `Bearer ${accessToken}` : '';
  /*async loginUser(e) {
    e.preventDefault();

    const { userEmail, userPassword } = this.state;
    try {
      const response = await fetch('http://127.0.0.1:8080/api/v1/users/authorize/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          email: userEmail,
          password: userPassword
        })
      });

      const data = await response.json();
      if (response.status === 200) {
        console.log('Успішно увійшли:', data);
        // Виклик функції, переданої через пропси, для оновлення стану авторизації в App.js
        this.props.onLoginSuccess(); // передаємо ім'я користувача або іншу інформацію
        //this.props.navigate('/'); // Редірект на основну сторінку
      } else {
        throw new Error(data.message || 'Не вдалося увійти');
      }
    } catch (error) {
      console.log('Виникла помилка при спробі входу');
      this.setState({ errorMessage: error.message || 'Виникла помилка при спробі входу' });*/
    }



  login = (e) => {
      e.preventDefault();

      const { saveTokens, loginUser, loginShelter } = useContext(AuthContext);

      const { email, password } = this.state;
      let entity = '';
      const formData = new URLSearchParams();

      formData.append('username', email);
      formData.append('password', password);

      const { showUserAuth, showShelterAuth } = this.state;

      if (showUserAuth) {
          entity = 'user';
      } else if (showShelterAuth) {
          entity = 'shelter';
      }

      const AUTH_API_URL = `http://127.0.0.1:8080/api/v1/${entity}/login`;

      axios.post(AUTH_API_URL, formData).then(response => {
          console.log('Авторизація пройшла успішно:', response.data);
          saveTokens(response);
          const { showUserAuth, showShelterAuth } = this.state;
          if (showUserAuth) {
              loginUser();
          } else if (showShelterAuth) {
              loginShelter();
          }
          this.setState({ errorMessage: 'Авторизацію пройдено успішно' });
          const navigate = useNavigate();
          navigate("/");
      }).catch((error) => {
          console.error('Введено некоректну електронну пошту або пароль.', error.message);
          this.setState({ errorMessage: 'Введено некоректну електронну пошту або пароль' });
      });
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
                onChange={this.handleInputChange}
              />
            </div>

            <div className="form-field">
              <label>Пароль</label>
              <input
                type="password"
                value={password}
                onChange={this.handleInputChange}
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

export default Login;
