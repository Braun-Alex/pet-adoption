import React, { Component } from 'react';
import axios from 'axios';
import { AuthContext } from '../Contexts/AuthContext';
import { withShelterAuth } from '../Wrappers/WithShelterAuth';
import '../css/List.css';

const currentShelterId = 2;

class RequestList extends Component {
  static contextType = AuthContext;

  constructor(props) {
    super(props);
    this.state = {
      requests: [], // This will hold the requests after we fetch them
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
    const shelterId = shelter.shelterID; // Assuming shelterID is available in the context

    try {
      const response = await axios.get(`${process.env.BACKEND_HOSTNAME}:${process.env.BACKEND_PORT}/api/v1/applications/get/?shelter_id=${shelterId}`);
      this.setState({ requests: response.data });
      console.log(response.data);
      this.loadUserNames(response.data);
      this.loadAnimalNames(response.data);
    } catch (error) {
      console.error('Error fetching requests:', error);
    }
  };

  loadUserNames = async (requests) => {
    // Load user names for each request
    const users = {};
    try {
    const userPromises = requests.map(async (request) => {
        const response = await axios.get(`${process.env.BACKEND_HOSTNAME}:${process.env.BACKEND_PORT}/api/v1/users/exists/${request.user_id}`);
        users[request.id] = response.data.full_name; // Assuming the response contains the user's name
        console.log(users);
    });
    await Promise.all(userPromises);
    this.setState({ users });
  } catch (error) {
    console.error('No requests available');
  }
  };

  loadAnimalNames = async (requests) => {
    // Load user names for each request
    const animals = {};
    try {
    const animalPromises = requests.map(async (request) => {
        const response = await axios.get(`${process.env.BACKEND_HOSTNAME}:${process.env.BACKEND_PORT}/api/v1/animals/animal/${request.animal_id}`);
        animals[request.id] = response.data.name; // Assuming the response contains the user's name
        console.log(animals);
    });
    await Promise.all(animalPromises);
    this.setState({ animals });
  } catch (error) {
    console.error('No requests available');
  }
  }

  handleAcceptReject = async (requestId, status) => {
    console.log(`Updating request ${requestId} with status ${status}`);

    const { shelter } = this.context; // Get shelter context
    const shelterId = shelter.shelterID; // Assuming shelterID is available in the context

    try {
        // Make the POST request to the API to update the status
        const response = await axios.post(`${process.env.BACKEND_HOSTNAME}:${process.env.BACKEND_PORT}/api/v1/applications/update_status`, {
            id: requestId,
            status: status,
            shelter_id: shelterId
        });

        // If the request was successful, update the state
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
        console.error('Error updating request status:', error);
    }
  };


  render() {
    return (
      <div className='request'>
        <ul className='list'>
          {this.state.requests.map(requestItem => {
            // Assuming the requestItem includes the user and animal data
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
                ) :
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
