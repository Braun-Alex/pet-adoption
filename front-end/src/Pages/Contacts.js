import React, { Component } from 'react';
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

export default withAuth(Contacts);

