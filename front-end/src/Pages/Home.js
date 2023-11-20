import React, {useState} from 'react';
import { Link } from 'react-router-dom';
import mainphoto2 from '../img/mainphoto2.JPG';
import animalicon from '../img/animalicon.png';
import '../css/Home.css';


const Home = () => {
  const [searchTerm, setSearchTerm] = useState('');
  return (
    <div className="main-container">

      <div className="left-side">
        <img className="main-photo" src={mainphoto2} alt="main-photo" />
      </div>
      
      <div className="right-side">
        <button className='view-shelter'>Переглянути притулки</button>
        <Link to="/animal-main" className='view-animal'>
          Знайти друга <img src={animalicon} alt="animalicon"/> </Link>
      </div>
      
    </div>
  );
};

export default Home;
