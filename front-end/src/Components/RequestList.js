import React, { useContext, useState } from 'react';
import { Context } from '../index';
import '../css/List.css';

const currentShelterId = 2;

const RequestList = () => {
  const { db } = useContext(Context);
  const [updatedRequests, setUpdatedRequests] = useState([...db.requests]);

  const getRequestDetails = (requestId) => {
    const requestInfo = db.requests.find(req => req.id === requestId);
    if (requestInfo) {
      const animalInfo = db.animals.find(animal => animal.id === requestInfo.animalId);
      const userInfo = db.users.find(user => user.id === requestInfo.userId);
      if (animalInfo && userInfo) {
        return { animal: animalInfo, user: userInfo };
      }
    }
    return null;
  };

  const handleAcceptReject = (requestId, status) => {
  console.log(`Updating request ${requestId} with status ${status}`);
  const updatedRequestsList = updatedRequests.map(request => {
    if (request.id === requestId) {
      return { ...request, status };
    }
    return request;
  });
  console.log("Updated requests list:", updatedRequestsList);
  setUpdatedRequests(updatedRequestsList);
};


  return (
    <div className='request'>
      <ul className='list'>
        {updatedRequests.map(requestItem => {
          const { animal, user } = getRequestDetails(requestItem.id);
          if (animal && user) {
            return (
              <li key={requestItem.id} className='list-item'>
                <div className='user-animal'>
                  {`${user.name} хоче прихистити ${animal.name}`}
                </div>

                {requestItem.status === 2 ? (
                  <div className='accept-reject'>
                    <button className='accept' onClick={() => handleAcceptReject(requestItem.id, 1)}>
                      &#x2713;
                    </button>
                    <button className='reject' onClick={() => handleAcceptReject(requestItem.id, 0)}>
                      &#x2716;
                    </button>
                  </div>
                ) : 
                    (requestItem.status === 1 && <div>прийнято</div>) ||
                    (requestItem.status === 0 && <div>відхилено</div>)
                }
              </li>
            );
          }
          return null;
        })}
      </ul>
    </div>
  );
};

export default RequestList;
