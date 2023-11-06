import React, { Component } from 'react';

class Signup extends Component {
  constructor() {
    super();
    this.state = {
      showUserReg: true,
      showShelterReg: false,
      buttonUser: true, 
      buttonShelter: false,
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
          


      <button className="button-reg">Зареєструватися</button>
      
      </div> 
    </>
    );
  }
}


export default Signup;