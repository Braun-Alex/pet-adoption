import React, {useContext} from 'react';
import { Context } from "../index";
import '../css/List.css';

const RequestList = () => {
    const { db } = useContext(Context);
    const filteredRequests = db.requests.filter(req => req.status === 2);

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

    return (
        <ul>
            {filteredRequests.map(requestItem => {
                const { animal, user } = getRequestDetails(requestItem.id);
                if (animal && user) {
                    return (
                        <li key={requestItem.id} className="request">
                            {`${animal.name} - ${user.name}`}
                        </li>
                    );
                }
                return null;
            })}
        </ul>
    );
}

export default RequestList;