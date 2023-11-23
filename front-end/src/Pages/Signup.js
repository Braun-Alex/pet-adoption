import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

class Signup extends Component {
  constructor() {
    super();
    this.state = {
      showUserReg: true,
      showShelterReg: false,
      registrationPath: '/user-account',
      full_name: '',
      email: '',
      password: '',
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

    registerUser = () => {
        const { full_name, email, password, showUserReg } = this.state;
        const userType = showUserReg ? 'user' : 'shelter';
  /*registerUser = async () => {
    try {
      console.log('ABOBA');
      const { full_name, email, password, showUserReg } = this.state;
      const userType = showUserReg ? 'user' : 'shelter';
      console.log(full_name);
      console.log(email);
      console.log(password);
      const response = await fetch('http://127.0.0.1:8080/api/v1/users/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          full_name,
          email,
          password,
        }),
      });*/

        const SIGNUP_API_URL = 'http://127.0.0.1:8080/api/v1/users/signup';

        axios.post(SIGNUP_API_URL, {
            full_name,
            email,
            password,
        }).then(response => {
            console.log('Реєстрація пройшла успішно:', response.data);
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
            onChange={(e) => this.handleInputChange('full_name', e.target.value)}
          />
        </div>

        <div className="form-field">
          <label>Електронна адреса</label>
          <input
            type="email"
            onChange={(e) => this.handleInputChange('email', e.target.value)}
          />
        </div>

        <div className="form-field">
          <label>Пароль</label>
          <input
            type="password"
            onChange={(e) => this.handleInputChange('password', e.target.value)}
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

      <Link to={this.state.registrationPath}><button className="button-reg" onClick={this.registerUser}>Зареєструватися</button></Link>

      </div>
    </>
    );
  }
}


export default Signup;
