import React, { Component } from 'react';
import { AuthContext } from '../Contexts/AuthContext';

class Contacts extends Component {
    static contextType = AuthContext;

    constructor(props) {
        super(props);
        this.state = {
            entityData: null
        };
    }

    componentDidMount() {
        const { user, shelter } = this.context;
        const entityData = user || shelter;
        this.setState({ entityData });
    }

    render() {
        const { entityData } = this.state;
        return (
            <div>Дані сутності: {entityData ? JSON.stringify(entityData): 'дані є відсутніми'}</div>
        );
    }
}

export default Contacts;
