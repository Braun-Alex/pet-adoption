from typing import Union
from backend.shelter.models.shelter_local_model import ShelterLocalRegistration, ShelterLocalOutput
from backend.application.application_app.models.application_local_models import ApplicationIn, ApplicationOut, ApplicationUpdate

import logging
import requests
from fastapi.security import OAuth2PasswordRequestForm



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

shelter1 = ShelterLocalRegistration(
    email="test1@gmail.com",
    name="Test Shelter 1",
    password="test1"
)



class ShelterUtils:
    def __init__(self):
        pass

    @staticmethod
    def register_shelter(shelter_data: ShelterLocalRegistration):
        logger.info(f"Registering shelter: {shelter_data=}")
        return requests.post(url=f"http://localhost:8080/api/v1/shelter/signup", json=shelter_data.model_dump())
    
    @staticmethod
    def get_shelter(jwt: str) -> ShelterLocalOutput:
        header = {  "Authorization": f"Bearer {jwt}" }
        response = requests.get(url="http://localhost:8080/api/v1/shelter/profile", headers=header)
        logger.info(f"{response.__dict__=}")
        return ShelterLocalOutput(**response.json())
    
    @staticmethod
    def get_shelter_by_id(shelter_id: int) -> ShelterLocalOutput:
        logger.info(f"Getting shelter by id: {shelter_id=}")
        return requests.get(url=f"http://localhost:8080/api/v1/shelter/{shelter_id}")
    @staticmethod
    def login_shelter(login_data: OAuth2PasswordRequestForm):
        logger.info(f"Logging in shelter: {login_data=}")
        return requests.post(url=f"http://localhost:8080/api/v1/shelter/login", data=login_data.__dict__)

    @staticmethod
    def remove_shelter(jwt_token: str):
        logger.info(f"Removing shelter: {jwt_token=}")
        header = {  "Authorization": f"Bearer {jwt_token}" }
        return requests.delete(url="http://localhost:8080/api/v1/shelter/delete", headers=header)

    @staticmethod
    def get_jwt_token(login_data: OAuth2PasswordRequestForm):
        logger.info(f"Getting JWT token: {login_data=}")
        response = __class__.login_shelter(login_data=login_data)
        logger.info(f"{response.json()=}")
        if 'access_token' not in response.json():
            raise RuntimeError(f"Invalid login credentials. Response does not contain access_token. LogIn credentials: {login_data.username=}, {login_data.password=}")

        return response.json()['access_token']
    

    @staticmethod
    def shelter_profile_id(jwt_token: str):
        return __class__.get_shelter(jwt=jwt_token).id

    @staticmethod
    def shelter_profile(pattern: Union[str, ShelterLocalRegistration]) -> ShelterLocalOutput:
        if isinstance(pattern, str):
            return __class__.get_shelter(jwt=pattern)
        elif isinstance(pattern, ShelterLocalRegistration):
            shelter_jwt = __class__.get_jwt_token(OAuth2PasswordRequestForm(username=pattern.email, password=pattern.password))
            return __class__.get_shelter(jwt=shelter_jwt)
        else:
            raise TypeError("Invalid argument type for jwt_token")
        
class AnimalsUtils:
    def __init__(self):
        pass

    @staticmethod
    def add_animal(shelter_id: int):
        with open("./dog.jpeg", "rb") as f:
            files = {"image": f}
            data = {
                "name": "Animal Name",
                "type": "Animal Type",
                "sex": "Animal Sex",
                "month": "Animal Month",
                "year": "Animal Year",
                "shelter_id": shelter_id,
                "description": "Animal Description"
            }
            return requests.post(url="http://localhost:8080/api/v1/animals/add", files=files, data=data)
        
    @staticmethod
    def delete_animal(animal_id: int, shelter_jwt_token: str):
        header = {  "Authorization": f"Bearer {shelter_jwt_token}" }
        return requests.delete(url=f"http://localhost:8080/api/v1/animals/delete/{animal_id}", headers=header)
    
    @staticmethod
    def get_animal_by_id(animal_id: int):
        return requests.get(url=f"http://localhost:8080/api/v1/animals/animal/{animal_id}")
    
class ApplicationUtils:
    def __init__(self):
        pass

    @staticmethod
    def create_application(application_data: ApplicationIn):
        return requests.post(url="http://localhost:8080/api/v1/applications/create", json=application_data.model_dump())
    
    @staticmethod
    def get_application(application_id: int):
        return requests.get(url=f"http://localhost:8080/api/v1/applications/{application_id}")
    
class UserUtils:
    def __init__(self):
        pass

    @staticmethod
    def register_user(user_data: ShelterLocalRegistration):
        return requests.post(url="http://localhost:8080/api/v1/users/signup", json=user_data.model_dump())
    
    @staticmethod
    def get_user(user_id: int):
        return requests.get(url=f"http://localhost:8080/api/v1/users/{user_id}")
    
    @staticmethod
    def login_user(login_data: OAuth2PasswordRequestForm):
        return requests.post(url="http://localhost:8080/api/v1/users/login", data=login_data.__dict__)
    
    @staticmethod
    def get_jwt_token(login_data: OAuth2PasswordRequestForm):
        response = __class__.login_user(login_data=login_data)
        if 'access_token' not in response.json():
            raise RuntimeError(f"Invalid login credentials. Response does not contain access_token. LogIn credentials: {login_data.username=}, {login_data.password=}")

        return response.json()['access_token']
    
    @staticmethod
    def get_user_profile(jwt_token: str) -> ShelterLocalOutput:
        header = {  "Authorization": f"Bearer {jwt_token}" }
        response = requests.get(url="http://localhost:8080/api/v1/users/profile", headers=header)
        return ShelterLocalOutput(**response.json())

    @staticmethod
    def user_id(jwt_token: str):
        return __class__.get_user_profile(jwt_token=jwt_token).json()['id']

    @staticmethod
    def remove_user(jwt_token: str):
        header = {  "Authorization": f"Bearer {jwt_token}" }
        return requests.delete(url="http://localhost:8080/api/v1/users/delete", headers=header)
    