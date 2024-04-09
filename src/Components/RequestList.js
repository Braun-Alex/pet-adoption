import React, { Component } from 'react';
import axios from 'axios';
import { AuthContext } from '../Contexts/AuthContext';
import { withShelterAuth } from '../Wrappers/WithShelterAuth';
import '../css/List.css';
import { toast } from 'react-toastify';

class RequestList extends Component {
    static contextType = AuthContext;

    constructor(props) {
        super(props);
        this.state = {
            requests: [],
            users: [],
            animals: [],
            applications: [],
        };
    }

    componentDidMount() {
        this.fetchRequests();
    }

    fetchRequests = async () => {
        const { shelter } = this.context;
        const shelterId = shelter.shelterID;
        try {
            const response = await axios.get(`${process.env.REACT_APP_BACKEND_HOSTNAME}/api/v1/applications/get/?shelter_id=${shelterId}`);
            this.setState({ requests: response.data });
            if (response.data.length > 0 && response.data[0].id !== null) {
                this.loadUserNames(response.data);
                this.loadAnimalNames(response.data);
            }
        } catch (error) {
            toast.error("Помилка при отриманні даних заявок!");
        }
    };

    loadUserNames = async (requests) => {
        const { tryLoginShelter } = this.context;
        const users = {};
        try {
            const userPromises = requests.map(async (request) => {
                const response = await axios.get(`${process.env.REACT_APP_BACKEND_HOSTNAME}/api/v1/users/user/${request.user_id}`);
                users[request.id] = response.data.name + " (" + response.data.email + ")";
            });
            await Promise.all(userPromises);
            this.setState({ users });
        } catch (error) {
            try {
                const success = await tryLoginShelter();
                if (success) {
                    await this.loadUserNames(requests);
                } else {
                    toast.error("Ви вийшли з облікового запису. Вам необхідно знову увійти!");
                }
            } catch (error) {
                toast.error("Помилка при отриманні даних користувачів, що подали заявки!");
            }
        }
    };

    loadAnimalNames = async (requests) => {
        const animals = {};
        try {
            const animalPromises = requests.map(async (request) => {
                const response = await axios.get(`${process.env.REACT_APP_BACKEND_HOSTNAME}/api/v1/animals/animal/${request.animal_id}`);
                animals[request.id] = response.data.name;
            });
            await Promise.all(animalPromises);
            this.setState({ animals });
        } catch (error) {
            toast.error("Помилка при отриманні даних тваринок!");
        }
    }

    handleAcceptReject = async (requestId, status) => {
        const { shelter } = this.context;
        const shelterId = shelter.shelterID;

        try {
            const response = await axios.post(`${process.env.REACT_APP_BACKEND_HOSTNAME}/api/v1/applications/update_status`, {
                id: requestId,
                status: status,
                shelter_id: shelterId
            });

            if (response.status === 200) {
                const updatedRequestsList = this.state.requests.map(request => {
                    if (request.id === requestId) {
                        return { ...request, status };
                    }
                    return request;
                });
                this.setState({ requests: updatedRequestsList });
            }
        } catch (error) {
            toast.error("Помилка при оновленні статусу заявки!");
        }
    };


    render() {
        return (
            <div>
                {this.state.requests.length > 0 && this.state.requests[0].id ? (
                    <ul className='list'>
                        {this.state.requests.map(requestItem => {
                            const userName = this.state.users[requestItem.id] || 'Завантаження...';
                            const animalName = this.state.animals[requestItem.id] || 'Завантаження...';
                            return (
                                <li key={requestItem.id} className='list-item-2'>
                                    <div className='user-animal'>
                                        {`${userName} хоче прихистити ${animalName}`}
                                    </div>

                                    {requestItem.status === 2 ? (
                                            <div className='accept-reject'>
                                                <button className='accept' onClick={() => this.handleAcceptReject(requestItem.id, 1)}>
                                                    &#x2713;
                                                </button>
                                                <button className='reject' onClick={() => this.handleAcceptReject(requestItem.id, 0)}>
                                                    &#x2716;
                                                </button>
                                            </div>
                                        ):
                                        requestItem.status === 1 ? <div>схвалено</div> : <div>відхилено</div>
                                    }
                                </li>
                            );
                        })}
                    </ul>
                ): (
                    <div>
                        Заявки на прихисток тваринок є відсутніми.
                    </div>
                )}
            </div>
        );
    }
}

export default withShelterAuth(RequestList);
