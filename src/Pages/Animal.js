// Animal.js
import React, { useContext, useState } from 'react';
import { Context } from '../index';
import {useParams} from 'react-router-dom'
//import axios from "axios";

/*const $host = axios.create({
    baseURL: process.env.REACT_APP_API_URL
})

const fetchOneAnimal = async (id) => {
    const {data} = await $host.get('api/animal/' + id)
    return data
}*/

const Animal = () => {
  const [animal, setAnimal] = useState( {info :[]})
  const {id} = useParams()
  /*useEffect(() => {
        fetchOneAnimal(id).then(data => setDevice(data))
    }, [])*/
  
  return (
    <div>
      <h2>Ім'я тваринки: {animal.name}</h2>
      <p>Тип: {animal.type}</p>
      <p>Стать: {animal.sex}</p>
      <p>Вік: {animal.age}</p>
    </div>
  );
};

export default Animal;
