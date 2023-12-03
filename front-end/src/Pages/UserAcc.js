import React, { Component } from 'react';
import usericon from '../img/usericon.png';
import editicon from '../img/editicon.png';
import ApplicationList from '../Components/ApplicationList';
import { AuthContext } from '../Contexts/AuthContext';
import { withUserAuth } from '../Wrappers/WithUserAuth';
import animalicon from "../img/animalicon.png";

class UserAcc extends Component {
    static contextType = AuthContext;

    constructor(props) {
        super(props);

        this.state = {
            photo: null,
            showShelterAcc: true,
            showEditAcc: false,
            showRequestList: false,
            showAnimal: false
        };

        this.handleFileChange = this.handleFileChange.bind(this);
        this.toggleShelterAcc = this.toggleShelterAcc.bind(this);
        this.toggleEditAcc = this.toggleEditAcc.bind(this);
        this.toggleAnimal = this.toggleAnimal.bind(this);
    }

    toggleShelterAcc = () => {
        this.setState({
            showShelterAcc: true,
            showEditAcc: false,
            showAnimal: false
        });
    };

    toggleEditAcc = () => {
        this.setState({
            showShelterAcc: false,
            showEditAcc: true,
            showAnimal: false
        });
    };

    toggleAnimal = () => {
        this.setState({
            showShelterAcc: false,
            showEditAcc: false,
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

    render() {
        const { photo, showShelterAcc, showEditAcc, showAnimal } = this.state;
        const { user } = this.context;

        if (!user) {
            return <div>Завантаження...</div>;
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

                        <button className={`${showAnimal ? 'active-shelter-option' : 'inactive-shelter-option'}`} onClick={this.toggleAnimal}>
                            <img src={animalicon} alt="[ ]" /> Заявки на прихисток
                        </button>
                    </div>
                </div>

                <div className="shelter-options-open">
                    <div>
                        {showShelterAcc && (
                            <div>
                                <div className="shelter-greeting">Вітаємо, {user.userFullName}!</div>
                                <div className="shelterInfo">
                                    <p>
                                        <label><strong>Ім'я: </strong></label>
                                        <span id="name">{user.userFullName}</span>
                                    </p>

                                    <p>
                                        <label><strong>Електронна пошта: </strong></label>
                                        <span id="email">{user.userEmail}</span>
                                    </p>
                                </div>
                            </div>
                        )}
                    </div>

                    <div>
                        {showEditAcc && (<div>
                                <form className="shelter-edit-info">
                                    <div className="shelterEditInfo-field">
                                        <label><strong>Ім'я</strong></label>
                                        <input type="text" name="shelterName" />
                                    </div>

                                    <div className="shelterEditInfo-field">
                                        <label><strong>Електронна пошта</strong></label>
                                        <input type="tel" name="shelterPhone" />
                                    </div>
                                    <button className='shelterEditInfo-button'>Зберегти зміни</button>
                                </form>
                            </div>
                        )}
                    </div>

                    <div>{showAnimal && <ApplicationList />}</div>

                </div>
            </div>
        )
    }
}

export default withUserAuth(UserAcc);
