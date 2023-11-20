import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      showUserReg: true,
      showShelterReg: false,
      registrationPath: '/user-account',
      userEmail: '',
      userPassword: '',
      errorMessage: ''
    };

    this.handleInputChange = this.handleInputChange.bind(this);
    this.loginUser = this.loginUser.bind(this);
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
  handleInputChange(e) {
    const { name, value } = e.target;
    this.setState({ [name]: value });
  }

  async loginUser(e) {
    e.preventDefault();

    const { userEmail, userPassword } = this.state;
    try {
      const response = await fetch('http://127.0.0.1:8000/users/authorize', {
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
      this.setState({ errorMessage: error.message || 'Виникла помилка при спробі входу' });
    }
  }

  render() {
    const { userEmail, userPassword, errorMessage } = this.state;

    return (
      <>
        <h1 className="form-header">ВХІД</h1>
        
        <div className="form">
          <button className={`${this.state.showUserReg ? 'activeToggle' : 'inactiveToggle'}`} onClick={this.toggleUser}>Користувач</button>
          <button className={`${this.state.showShelterReg ? 'activeToggle' : 'inactiveToggle'}`} onClick={this.toggleShelter}>Притулок</button>
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
            
            <Link to={this.state.registrationPath}><button type="submit" className="button-reg" onClick={this.registerUser}>Увійти</button></Link>
          </form>
        </div>                
      </>
    );
  }
}

export default Login;
