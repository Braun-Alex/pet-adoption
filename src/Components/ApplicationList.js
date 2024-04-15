import React, { Component } from 'react';
import '../css/List.css';
import { Link } from 'react-router-dom';
import { AuthContext } from '../Contexts/AuthContext';
import { withUserAuth } from '../Wrappers/WithUserAuth';

class ApplicationList extends Component {
    static contextType = AuthContext;

    render() {
        const { userApplications } = this.context;
        return (
            <div className="animal-from-shelter">
                <Link to="/animal-main" className="link">
                    <button
                        aria-controls=''
                        className='add-animal-button'
                    >
                        Прихистити нову тваринку
                    </button>
                </Link>
                {!userApplications && (
                    <div>Заявки на прихисток є відсутніми.</div>
                )}
                {userApplications && (
                    <ul className="list">
                        {userApplications.map(animal =>
                            <li className="list-item">
                                <p><strong>Ім'я тваринки:</strong> {animal.name}</p>
                                <p><strong>Фотографія тваринки:</strong></p>
                                <div>
                                    <img src={animal.photo} alt={'Фото ' + animal.type} className="animal-photo" />
                                </div>
                                <p><strong>Вид тваринки:</strong> {animal.type}</p>
                                <p><strong>Стать тваринки:</strong> {animal.sex}</p>
                                <p><strong>Дата народження тваринки:</strong> {animal.month + "." + animal.year}</p>
                                <p><strong>Деталі про тваринку:</strong> {animal.description}</p>
                                <p><strong>Статус заявки:</strong> {
                                    animal.status === 2 ? "надіслано до розгляду" :
                                        animal.status === 1 ? "схвалено притулком" :
                                            animal.status === 0 ? "відхилено притулком" : "помилка обробки"
                                }</p>
                            </li>
                        )}
                    </ul>
                )}
            </div>
        );
    }
}

export default withUserAuth(ApplicationList);
