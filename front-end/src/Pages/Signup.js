import React, { Component } from 'react';

class Signup extends Component {
  constructor() {
    super();
    this.state = {
      showUserReg: true,
      showShelterReg: false,
      buttonUser: true, 
      buttonShelter: false,
      full_name: '',
      email: '',
      password: '',
    };
  }
  toggleUser = () => {
    this.setState({
      showUserReg: true,
      showShelterReg: false,
      buttonUser: true, 
      buttonShelter: false,
    });
  }

  toggleShelter = () => {
    this.setState({
      showUserReg: false,
      showShelterReg: true,
      buttonUser: false, 
      buttonShelter: true,
    });
  }

  handleInputChange = (field, value) => {
    this.setState({ [field]: value });
  }

  registerUser = async () => {
    try {
      console.log('ABOBA');
      const { full_name, email, password, showUserReg } = this.state;
      const userType = showUserReg ? 'user' : 'shelter';
      console.log(full_name);
      console.log(email);
      console.log(password);
      const response = await fetch('http://127.0.0.1:8000/users/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          full_name,
          email,
          password,
        }),
      });

      const data = await response.json();

      if (response.status === 200) {
        console.log('Успішно зареєстровано:', data);
        // Тут можете перенаправити користувача на іншу сторінку або вивести повідомлення про успіх
      } else {
        console.error('Помилка реєстрації:', data);
      }
    } catch (error) {
      console.error('Помилка з\'єднання:', error);
    }
  }

  render() {
    return (
    <>
    <h1 className="form-header">РЕЄСТРАЦІЯ</h1>
    <div className="form">
      
      <button className={`${this.state.buttonUser ? 'active' : 'inactive'}`} onClick={this.toggleUser}>Користувач</button>
      <button className={`${this.state.buttonShelter ? 'active' : 'inactive'}`} onClick={this.toggleShelter}>Притулок</button>
      <div className={`${this.state.buttonUser ? 'hr-line-user' : 'hr-line-shelter'}`} onClick={this.toggleContent1}></div>

      {this.state.showUserReg && 
      <div className="registration-form">

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

        </div>}
          

      {this.state.showShelterReg && <div className="registration-form">
      
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

      </div>}
          


      <button className="button-reg" onClick={this.registerUser}>Зареєструватися</button>
      
      </div> 
    </>
    );
  }
}


export default Signup;