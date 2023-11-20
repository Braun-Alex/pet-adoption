import React, {useState} from 'react';
import '../css/Modal.css'
import Modal from 'react-modal';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';

const CreateAnimal = ({ show, onHide }) => {

    const modalStyles = {
        display: show ? 'block' : 'none',
    };
    const overlayStyles = {
        display: show ? 'block' : 'none',
    };

    const types = ['кіт', 'пес'];
    const sex = ['хлопчик', 'дівчинка'];
    const mounths = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'];
    const years = ['2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015'];
    const defaultOption = null;
    
    return (
        <>        
        <div className="overlay" style={overlayStyles}>
            <Modal
            isOpen={show}
            onRequestClose={onHide}
            className="modal"
            style={modalStyles}
            centered
            >
            <div className='modal-content'>
                <span className="close" onClick={onHide}>&times;</span>
                <div>
                    <div className="add-animal-header">
                        Додати тваринку
                    </div>
                </div>
                <div>                    
                    <form className='add-animal-container'>
                        <div className="animal-name">
                            <label>Ім'я тваринки</label>
                            <input type="text" />
                        </div>
                        <div>
                             <Dropdown options={types} value={defaultOption} placeholder="вид тваринки"  className="animal-type"/>                        
                        </div>
                        <div>
                            <Dropdown options={sex} value={defaultOption} placeholder="стать" className="animal-sex"/>
                        </div>
                        <div class="select-date" >
                            <Dropdown options={mounths} value={defaultOption} placeholder="місяць" />
                            <Dropdown options={years} value={defaultOption} placeholder="рік" className='year'/>
                        </div>
                        <div className="animal-desc">
                            <label>Опис</label>
                            <textarea rows="4" ></textarea>
                        </div>
                    </form>
                </div>

                <button className="create-animal-button">Додати</button>

            </div>
            
        </Modal>

        </div>
        </>
        
        
  );
}

export default CreateAnimal;