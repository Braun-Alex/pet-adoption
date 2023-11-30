import React, { Component } from 'react';
import axios from 'axios';
import { AuthContext } from '../Contexts/AuthContext';
import { withAuth } from '../Wrappers/WithAuth';
import '../css/List.css';

class RequestList extends Component {
  static contextType = AuthContext;

  constructor(props) {
    super(props);
    this.state = {
      requests: [], // This will hold the requests after we fetch them
      users: [],
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
      const response = await axios.get(`http://127.0.0.1:8080/api/v1/applications/get/?shelter_id=${shelterId}`);
      this.setState({ requests: response.data });
      console.log(response.data);
      this.loadUserNames(response.data);
      /*const userId = response.data.user_id;
      const response1 = await axios.get(`http://127.0.0.1:8080/api/v1/users/exists/${userId}`);
      this.setState({ users: response1.data });*/
    } catch (error) {
      console.error('Error fetching requests:', error);
    }
  };

  loadUserNames = async (requests) => {
    // Load user names for each request
    const users = {};
    const userPromises = requests.map(async (request) => {
        const response = await axios.get(`http://127.0.0.1:8080/api/v1/users/exists/${request.user_id}`);
        users[request.id] = response.data.full_name; // Assuming the response contains the user's name
        console.log(users);
    });
    await Promise.all(userPromises);
    this.setState({ users });
};

  handleAcceptReject = async (requestId, status) => {
    console.log(`Updating request ${requestId} with status ${status}`);
    
    const { shelter } = this.context; // Get shelter context
    const shelterId = shelter.shelterID; // Assuming shelterID is available in the context

    try {
        // Make the POST request to the API to update the status
        const response = await axios.post('http://127.0.0.1:8080/api/v1/applications/update_status', {
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
            return (
              <li key={requestItem.id} className='list-item-2'>
                <div className='user-animal'>
                  {`${userName} хоче прихистити ${requestItem.animal_id}`}
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

export default withAuth(RequestList);
