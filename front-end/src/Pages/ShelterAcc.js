import React, { Component, useContext, useState } from 'react';
import { Context } from "../index";
import usericon from '../img/usericon.png';
import animalicon from '../img/animalicon.png';
import editicon from '../img/editicon.png';
import mailicon from '../img/mailicon.png';
import RequestList from '../Components/RequestList';
import AnimalList from '../Components/AnimalList';
import { AuthContext } from '../Contexts/AuthContext';
import { withAuth } from '../Wrappers/WithAuth';

const currentShelterId = 2;

class ShelterAcc extends Component {
    static contextType = AuthContext;

    constructor(props) {
      super(props);
      this.state = {
          photo: null,
          showShelterAcc: true,
          showEditAcc: false,
          showRequestList: false,
          showAnimal: false,
          // інші змінні стану
      };
      // Прив'язування методів до контексту класу
      this.handleFileChange = this.handleFileChange.bind(this);
      this.toggleShelterAcc = this.toggleShelterAcc.bind(this);
      this.toggleEditAcc = this.toggleEditAcc.bind(this);
      this.toggleRequest = this.toggleRequest.bind(this);
      this.toggleAnimal = this.toggleAnimal.bind(this);
    }
    //const { db } = useContext(Context);
    
    /*const [photo, setPhoto] = useState(null);
    const [showShelterAcc, setShowShelterAcc] = useState(true);
    const [showEditAcc, setShowEditAcc] = useState(false);
    const [showRequestList, setShowRequestList] = useState(false);
    const [showAnimal, setShowAnimal] = useState(false);*/

    toggleShelterAcc = () => {
      this.setState({
        showShelterAcc: true,
        showEditAcc: false,
        showRequestList: false,
        showAnimal: false
    });
    };

    toggleEditAcc = () => {
      this.setState({
        showShelterAcc: false,
        showEditAcc: true,
        showRequestList: false,
        showAnimal: false
    });
    };

    toggleRequest = () => {
      this.setState({
        showShelterAcc: false,
        showEditAcc: false,
        showRequestList: true,
        showAnimal: false
    });
    };

    toggleAnimal = () => {
      this.setState({
        showShelterAcc: false,
        showEditAcc: false,
        showRequestList: false,
        showAnimal: true
    });
  };
  handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        this.setState({ photo: e.target.result });
      };
      reader.readAsDataURL(file);
    }
  };

   //const filteredShelter = db.shelters.filter((shel) => shel.id === currentShelterId);

  render() {
    const { photo, showShelterAcc, showEditAcc, showRequestList, showAnimal } = this.state;
    const { user, shelter } = this.context;

    if (!shelter) {
      console.log(shelter);
      return <div>Завантаження...</div>; // або будь-який інший варіант заповнення
    }

    return (
      <div className="container">
        <div className="shelter-photo-greeting">
          <label className="photo-container">
            <input type="file" accept="image/*" onChange={this.handleFileChange} style={{ display: 'none' }} />
            {photo ? (
              <img src={photo} alt="Фото" className="selected-photo" style={{ objectFit: 'cover' }} />
            ) : (
              <div>фото</div>
            )}
          </label>
          <div className="shelter-options">
            <button className={`${showShelterAcc ? 'active-shelter-option' : 'inactive-shelter-option'}`} onClick={this.toggleShelterAcc}>
              <img src={usericon} alt="[ ]" /> Акаунт
            </button>

            <button className={`${showEditAcc ? 'active-shelter-option' : 'inactive-shelter-option'}`} onClick={this.toggleEditAcc}>
              <img src={editicon} alt="[ ]" /> Редагувати профіль
            </button>

            <button className={`${showRequestList ? 'active-shelter-option' : 'inactive-shelter-option'}`} onClick={this.toggleRequest}>
              <img src={mailicon} alt="[ ]" /> Список заявок
            </button>

            <button className={`${showAnimal ? 'active-shelter-option' : 'inactive-shelter-option'}`} onClick={this.toggleAnimal}>
              <img src={animalicon} alt="[ ]" /> Тваринки
            </button>
          </div>
        </div>

        <div className="shelter-options-open">
          <div>
            {showShelterAcc && (
              <div>
                <div className="shelter-greeting">Вітаємо, {shelter.shelterName}!</div>
                <div className="shelterInfo">
                  <p>
                    <label>Ім'я: </label>
                    <span id="name">{shelter.shelterName}</span>
                  </p>

                  <p>
                    <label>Email: </label>
                    <span id="email">{shelter.shelterEmail}</span>
                  </p>

                  <p>
                    <label>Номер телефону: </label>
                    <span id="phone">{"Немає"}</span>
                  </p>
                  <p>
                    <label>Адреса: </label>
                    <span id="address">{"Немає"}</span>
                  </p>

                  <p>
                    <label>Опис: </label>
                    <span id="description">{"Немає"}</span>
                  </p>
                </div>
              </div>
            )}
          </div>

          <div>
            {showEditAcc && (<div>
                <form className="shelter-edit-info">
                <div className="shelterEditInfo-field">
                  <label>Ім'я</label>
                  <input type="text" name="shelterName" />
                </div>
                
                <div className="shelterEditInfo-field">
                  <label>Електронна пошта</label>
                  <input type="tel" name="shelterPhone" />
                </div>

                <div className="shelterEditInfo-field">
                  <label>Номер телефону</label>
                  <input type="tel" name="shelterPhone" />
                </div>

                <div className="shelterEditInfo-field">
                  <label>Адреса</label>
                  <input type="text" name="shelterAddress" />
                </div>                               

                <div className="shelterEditInfo-field-desc">
                  <label>Опис</label>
                  <textarea rows="4"></textarea>
                </div>  
                <button className='shelterEditInfo-button'>Зберегти зміни</button>
              </form>
            </div>              
            )}            
          </div>

          <div>{showRequestList && <RequestList />}</div>

          <div>{showAnimal && <AnimalList />}</div>
          
        </div>
      </div>
    )
  }
};

export default withAuth(ShelterAcc);