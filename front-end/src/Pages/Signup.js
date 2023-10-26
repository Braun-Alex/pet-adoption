import React from "react";

function Signup() {
  return <div className="site">
  <h1 className="form-header">РЕЄСТРАЦІЯ</h1>
    <div className="form">
      
      <button className="shelter-role">Притулок</button>
      <button className="user-role">Користувач</button>

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

      </div>
      
      <button className="button-reg">Зареєструватися</button>
      
      </div>
    </div>
}

export default Signup;