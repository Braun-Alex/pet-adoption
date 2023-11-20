import React from 'react';

const AnimalTableItem = ({animal}) => {
    return (
        <div>
            <div className='animal-item'>
                <div>{animal.name}</div>
                <div class="animal-photo">фото тваринки</div>
                <div>{animal.sex}</div>
                <div>{animal.type}</div>
                <div>{animal.age}</div>
            </div>
        </div>
    );
};

export default AnimalTableItem;