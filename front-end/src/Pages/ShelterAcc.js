import React, { Component, useContext, useState } from 'react';
import { Context } from "../index";
import usericon from '../img/usericon.png';
import animalicon from '../img/animalicon.png';
import editicon from '../img/editicon.png';
import mailicon from '../img/mailicon.png';
import RequestList from '../Components/RequestList';
import AnimalList from '../Components/AnimalList';

import '../css/ShelterAcc.css'

const currentShelterId = 2;


const ShelterAcc = () => {
    const { db } = useContext(Context);
    
    const [photo, setPhoto] = useState(null);
    const [showShelterAcc, setShowShelterAcc] = useState(true);
    const [showEditAcc, setShowEditAcc] = useState(false);
    const [showRequestList, setShowRequestList] = useState(false);
    const [showAnimal, setShowAnimal] = useState(false);

    const toggleShelterAcc = () => {
      setShowShelterAcc(true);
      setShowEditAcc(false);
      setShowRequestList(false);
      setShowAnimal(false);
    };

    const toggleEditAcc = () => {
      setShowShelterAcc(false);
      setShowEditAcc(true);
      setShowRequestList(false);
      setShowAnimal(false);
    };

    const toggleRequest = () => {
      setShowShelterAcc(false);
      setShowEditAcc(false);
      setShowRequestList(true);
      setShowAnimal(false);
    };

    const toggleAnimal = () => {
      setShowShelterAcc(false);
      setShowEditAcc(false);
      setShowRequestList(false);
      setShowAnimal(true);
  };
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        setPhoto(e.target.result);
      };
      reader.readAsDataURL(file);
    }
  };
   const filteredShelter = db.shelters.filter((shel) => shel.id === currentShelterId);

  return (
    <>
      <div className="container">
        
        <div className="shelter-photo-greeting">
          <label className="photo-container">
            <input type="file" accept="image/*" onChange={handleFileChange} style={{ display: 'none' }} />
            {photo ? (
              <img src={photo} alt="Фото" className="selected-photo" style={{ objectFit: 'cover' }} />
            ) : (
              <div>фото</div>
            )}
          </label>
          <div className="shelter-options">
            <button className={`${showShelterAcc ? 'active-shelter-option' : 'inactive-shelter-option'}`} onClick={toggleShelterAcc}>
              <img src={usericon} alt="[ ]" /> Акаунт
            </button>

            <button className={`${showEditAcc ? 'active-shelter-option' : 'inactive-shelter-option'}`} onClick={toggleEditAcc}>
              <img src={editicon} alt="[ ]" /> Редагувати профіль
            </button>

            <button className={`${showRequestList ? 'active-shelter-option' : 'inactive-shelter-option'}`} onClick={toggleRequest}>
              <img src={mailicon} alt="[ ]" /> Список заявок
            </button>

            <button className={`${showAnimal ? 'active-shelter-option' : 'inactive-shelter-option'}`} onClick={toggleAnimal}>
              <img src={animalicon} alt="[ ]" /> Тваринки
            </button>
          </div>
        </div>

        <div className="shelter-options-open">
          <div>
            {showShelterAcc && (
              <div>
                <div className="shelter-greeting">Вітаємо, {filteredShelter[0].name}!</div>
                <div className="shelterInfo">
                  <p>
                    <label>Ім'я: </label>
                    <span id="name">{filteredShelter[0].name}</span>
                  </p>

                  <p>
                    <label>Email: </label>
                    <span id="email">{filteredShelter[0].email}</span>
                  </p>

                  <p>
                    <label>Номер телефону: </label>
                    <span id="phone">{filteredShelter[0].phone}</span>
                  </p>
                  <p>
                    <label>Адреса: </label>
                    <span id="address">{filteredShelter[0].address}</span>
                  </p>

                  <p>
                    <label>Опис: </label>
                    <span id="description">{filteredShelter[0].description}</span>
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
    </>
  );
};

export default ShelterAcc;

