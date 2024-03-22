import React, { Component } from 'react';
import axios from 'axios';
import { AuthContext } from '../Contexts/AuthContext';
import { withShelterAuth } from '../Wrappers/WithShelterAuth';
import '../css/List.css';
import { toast } from "react-toastify";

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
            this.loadUserNames(response.data);
            this.loadAnimalNames(response.data);
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
                users[request.id] = response.data.full_name + " (" + response.data.email + ")";
                console.log(users);
            });
            await Promise.all(userPromises);
            this.setState({ users });
        } catch (error) {
            try {
                await tryLoginShelter();
                await this.loadUserNames(requests);
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
            <div className='request'>
                <ul className='list'>
                    {this.state.requests.map(requestItem => {
                        const userName = this.state.users[requestItem.id] || 'Loading...';
                        const animalName = this.state.animals[requestItem.id] || 'Loading...';
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
                                    requestItem.status === 1 ? <div>прийнято</div> : <div>відхилено</div>
                                }
                            </li>
                        );
                    })}
                </ul>
            </div>
        );
    }
}

export default withShelterAuth(RequestList);
