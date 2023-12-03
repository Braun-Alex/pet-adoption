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
            <div class="animal-from-shelter">
                <Link to="/animal-main">
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
                    <ul class="list">
                        {userApplications.map(animal =>
                            <li class="list-item">
                                <p><strong>Ім'я тваринки:</strong> {animal.name}</p>
                                <p><strong>Вид тваринки:</strong> {animal.type}</p>
                                <p><strong>Стать тваринки:</strong> {animal.sex}</p>
                                <p><strong>Місяць народження тваринки:</strong> {animal.month + "." + animal.year}</p>
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
