import React, { Component } from 'react';
import '../css/List.css';
import { Link } from 'react-router-dom';
import { AuthContext } from '../Contexts/AuthContext';
import { withUserAuth } from '../Wrappers/WithUserAuth';
import axios from 'axios';

class ApplicationList extends Component {
    static contextType = AuthContext;

    constructor(props) {
        super(props);
        this.state = {
            applications: []
        };
    }

    componentDidMount() {
        this.fetchApplications();
    }

    fetchApplications = async () => {
        const { user } = this.context;
        try {
            const applicationsResponse = await axios.get(`http://127.0.0.1:8080/api/v1/applications/get/?user_id=${user.userID}`);
            const applications = applicationsResponse.data;
            for (const application of applications) {
                const animalResponse = await axios.get(`http://127.0.0.1:8080/api/v1/animals/animal/${application.animal_id}`);
                application.name = animalResponse.data.name;
                application.type = animalResponse.data.type;
                application.sex = animalResponse.data.sex;
                application.month = animalResponse.data.month;
                application.year = animalResponse.data.year;
                application.description = animalResponse.data.description;
            }
            this.setState({ applications });
        } catch (error) {
            console.error('Помилка при завантаженні даних заявок:', error);
        }
    }

    render() {
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
                <ul class="list">
                    {this.state.applications.map(animal =>
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

            </div>
        );
    }

}
export default withUserAuth(ApplicationList);
