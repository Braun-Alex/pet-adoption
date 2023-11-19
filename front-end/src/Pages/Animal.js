// AnimalDetail.js
import React from 'react';

const AnimalDetail = ({ match }) => {
  // Використовуйте match.params.animalId для отримання id тваринки з URL
  const animalId = match.params.animalId;

  // Отримайте дані тваринки і відобразіть їх
  // Замість цього коду вам слід отримати дані тваринки зі свого джерела даних
  const animalData = {
    id: animalId,
    name: 'Ім\'я тваринки',
    description: 'Опис тваринки...',
  };

  return (
    <div>
      <h2>{animalData.name}</h2>
      <p>{animalData.description}</p>
    </div>
  );
};

export default AnimalDetail;
