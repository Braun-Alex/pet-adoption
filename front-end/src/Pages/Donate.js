import React, { Component } from 'react';
import '../css/Donate.css';
import qrcode from "../img/QR-code.png"

class Donate extends Component {
  render() {
    return (
      <div className="donate-container">
        <div className="donate-title">ПІДТРИМАТИ ПРОЄКТ</div>
        <div className="donate-details">
          <div className="qr-code">
            <img className="qr-code-img" src={qrcode} alt="qr-code" />
            <div className="qr-code-text">за QR-кодом</div>
          </div>        
          <div className="payment-details">
            <div className="payment-details-lists-container">
              <ul className="details-titles">
                <li>IBAN</li>
                <li>Назва банку</li>
                <li>ЄДРПОУ</li>
              </ul>
              <ul className="details-values">
                <li>№ UA643052990000026003000105068</li>
                <li>АТ КБ "ПРИВАТБАНК"</li>
                <li>38266276</li>
              </ul>
            </div>            
            <div className="payment-details-text">за реквізитами</div>
          </div>
        </div>        
      </div>
      
    )
  }
}

export default Donate;