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

    const mounths = ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень'];
    const years = ['2023', '2022', '2021', '2020', '2019', '2018', '2017'];
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
                        <div className="animal-type">
                            <label>Вид тваринки</label>
                            <input type="text" />
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