import React, { Component } from 'react';
import usericon from '../img/usericon.png';
import animalicon from '../img/animalicon.png';
import editicon from '../img/editicon.png';
import RequestList from '../Components/RequestList';
import AnimalList from '../Components/AnimalList';
import DB from '../List/DB';

var sheltername = " назва притулку";
var shelterEmail = " example@ex.ex";
var shelterPhone = " +380777777777";
var shelterAddress = " адреса, м. Місто";
var shelterDescription = " Опис притулку.";

class ShelterAcc extends Component {
  constructor() {
    super();
    this.state = {
      photo: null,
      showShelterAcc: false,
      showEditAcc: false,
      showRequestList: true,
      showAnimal: false,
    };
  }
  toggleShelterAcc = () => {
    this.setState({
      showShelterAcc: true,
      showEditAcc: false,
      showRequestList: false,
      showAnimal: false,
    });
  }
  toggleEditAcc = () => {
    this.setState({
      showShelterAcc: false,
      showEditAcc: true,
      showRequestList: false,
      showAnimal: false,
    });
  }
  toggleRequest = () => {
    this.setState({
      showShelterAcc: false,
      showEditAcc: false,
      showRequestList: true,
      showAnimal: false,
    });
  }
  toggleAnimal = () => {
    this.setState({
      showShelterAcc: false,
      showEditAcc: false,
      showRequestList: false,
      showAnimal: true,
    });
  }
  handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        this.setState({ photo: e.target.result });
      };
      reader.readAsDataURL(file);
    }
  }

  render() {
    const { photo } = this.state;
    return (
      <>        
        
        <div class="shelter-photo-greeting">
          <label className="photo-container">
             <input type="file" accept="image/*" onChange={this.handleFileChange} style={{ display: 'none' }}/>
              {photo ? (
                <img src={photo} alt="Фото" className="selected-photo"  style={{ objectFit: 'cover' }}/>
              ) : (
                <div>фото</div>
              )}
          </label>
          <div className='shelter-greeting'>Вітаємо, {sheltername}!</div>
        </div>

        <div class="shelter-options-open">
          <div className="shelter-options">   
          
          <button className={`${this.state.showShelterAcc ? 'active-shelter-option' : 'inactive-shelter-option'}`} onClick={this.toggleShelterAcc}>
            <img src={usericon} alt="[ ]" /> Акаунт
          </button>

          <button className={`${this.state.showEditAcc ? 'active-shelter-option' : 'inactive-shelter-option'}`} onClick={this.toggleEditAcc}>
            <img src={editicon} alt="[ ]" /> Редагувати профіль
            </button>
            
          <button className={`${this.state.showRequestList ? 'active-shelter-option' : 'inactive-shelter-option'}`} onClick={this.toggleRequest}>
            <img src={editicon} alt="[ ]" /> Список заявок
          </button>

          <button className={`${this.state.showAnimal ? 'active-shelter-option' : 'inactive-shelter-option'}`} onClick={this.toggleAnimal}>
            <img src={animalicon} alt="[ ]" /> Тваринки
          </button>
          
        </div>
        
          <div>
            {this.state.showShelterAcc && <div class="shelterInfo">
              <p>
                <label>Ім'я:</label>
                <span id="name">{sheltername}</span>
              </p>

              <p>
                <label >Email:</label>
                <span id="email">{shelterEmail}</span>
              </p>

              <p>
                <label>Номер телефону:</label>
                <span id="phone">{shelterPhone}</span>
              </p>
              <p>
                <label >Адреса:</label>
                <span id="address">{shelterAddress}</span>
              </p>
              
              <p>
                <label >Опис:</label>
                <span id="description">{shelterDescription}</span>
              </p>

            </div>}
          </div>      
      
          <div>            
            {this.state.showEditAcc && <form class="shelterEditInfo">
              <div className="shelterEditInfo-field">
                <label>Ім'я</label>
                <input type="text" name="shelterName"/>
              </div>
          
              <div className="shelterEditInfo-field">
                <label>Адреса</label>
                <input type="text" name="shelterAddress"/>
              </div>
            
              <div className="shelterEditInfo-field">
                <label>Номер телефону</label>
                <input type="tel" name="shelterPhone"/>
              </div>
              
              <div className="shelterEditInfo-field">
                <label>Опис</label>
                <input type="text" name="shelterDescription"/>
              </div>

            </form>}
          </div>

          <div>
            {this.state.showRequestList && <RequestList />
              
            }
          </div>
           
          <div>
            {this.state.showAnimal && <div>

              <AnimalList />
              

            </div>            
            }
          </div>
        </div>
        
      </>     

    );
  }
}

export default ShelterAcc;
