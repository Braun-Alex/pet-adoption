/*import React, { Component } from 'react';
import { AuthContext } from '../Contexts/AuthContext';
import { withAuth } from '../Wrappers/WithAuth';

class Contacts extends Component {
    static contextType = AuthContext;

    render() {
        const { user, shelter } = this.context;

        return (
            <div>
                {user && (
                    <div>
                        <h2>Дані користувача</h2>
                        <p>Повне ім'я: {user.userFullName}</p>
                        <p>Електронна пошта: {user.userEmail}</p>
                    </div>
                )}
                {shelter && (
                    <div>
                        <h2>Дані притулку</h2>
                        <p>Назва: {shelter.shelterName}</p>
                        <p>Електронна адреса: {shelter.shelterEmail}</p>
                    </div>
                )}
                {!user && !shelter && (
                    <div>Дані завантажуються...</div>
                )}
            </div>
        );
    }
}

export default withAuth(Contacts);*/

import React, { Component } from 'react';
import { AuthContext } from '../Contexts/AuthContext';
import { withAuth } from '../Wrappers/WithAuth';
import axios from 'axios';

class Contacts extends Component {
    static contextType = AuthContext;

    constructor(props) {
        super(props);
        this.state = {
            applications: [], // Додавання стану для заявок
        };
    }

    componentDidMount() {
        this.fetchUserApplications();
    }

    fetchUserApplications = async () => {
        const { user } = this.context;
        if (user) {
            try {
                const applicationsResponse = await axios.get(`http://127.0.0.1:8080/api/v1/applications/get/?user_id=${user.userID}`);
                const applications = applicationsResponse.data;

                // Отримання деталей кожної тварини
                for (const application of applications) {
                    const animalResponse = await axios.get(`http://127.0.0.1:8080/api/v1/animals/animal/${application.animal_id}`);
                    application.animalName = animalResponse.data.name; // Додайте ім'я тварини до об'єкта заявки
                }

                this.setState({ applications });
            } catch (error) {
                console.error('Помилка при завантаженні даних заявок:', error);
            }
        }
    }

    renderApplications() {
        const { applications } = this.state;
        return applications.map(app => (
            <div key={app.id}>
                <p>Заявка на: {app.animalName}</p>
                <p>Статус: {
                app.status === 2 ? "Заявку подано" :
                app.status === 1 ? "Заявку прийнято" :
                app.status === 0 ? "Заявку відхилено" : "Статус невідомий"
                }</p>
                {/* Інші деталі заявки */}
            </div>
        ));
    }

    render() {
        const { user, shelter } = this.context;

        return (
            <div>
                {user && (<div style={{ height: '40px' }}></div>)}
                {user && (<h2>Заявки користувача {user.userFullName}</h2>)}
                {/* Ваш код для відображення даних користувача та притулку */}
                {user && this.renderApplications()}
            </div>
        );
    }
}

export default withAuth(Contacts);

