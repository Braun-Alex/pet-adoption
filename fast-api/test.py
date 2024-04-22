from typing import Optional
from pydantic import BaseModel
from shelter.models.shelter_local_model import ShelterLocalRegistration
import requests
import pytest
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

shelter1 = ShelterLocalRegistration(
    email="test1@gmail.com",
    name="Test Shelter 1",
    password="test1"
)

@pytest.fixture(scope="module", autouse=True)
def host_name() -> str:
    return "http://localhost:8080"

def register_shelter(shelter_data: ShelterLocalRegistration):
    logger.info(f"Registering shelter: {shelter_data=}")
    return requests.post(url=f"http://localhost:8080/api/v1/shelter/signup", json=shelter_data.model_dump())

def login_shelter(login_data: dict ):
    logger.info(f"Logging in shelter: {login_data=}")
    return requests.post(url=f"http://localhost:8080/api/v1/shelter/login", data=login_data)

def remove_shelter(jwt_token: str):
    header = {  "Authorization": f"Bearer {jwt_token}" }
    return requests.delete(url="http://localhost:8080/api/v1/shelter/delete", headers=header)

def get_jwt_token(login_data: dict):
    logger.info(f"Getting JWT token: {login_data=}")
    response = login_shelter(login_data=login_data)
    return response.json()['access_token']

def sheler_profile_id(jwt_token: str):
    header = {  "Authorization": f"Bearer {jwt_token}" }
    response = requests.get(url="http://localhost:8080/api/v1/shelter/profile", headers=header)
    assert response.status_code == 200, f"Expected return code 200. Got {response.status_code=}"
    return response.json()["id"]

shelter_data = ShelterLocalRegistration(
                    email="test1@gmail.com",
                    name="Test Shelter 1",
                    password="test1"
                )

shelter_data2 = ShelterLocalRegistration(
                    email="test2@gmail.com",
                    name="Test Shelter 2",
                    password="test2"
                )


shelter_data_set = {
    "valid_data1":   [shelter_data, {"username":  shelter_data.email, "password": shelter_data.password}],
    "invalid_data1": [shelter_data, {"username":  shelter_data.email, "password": shelter_data.password + "1"}],
    "valid_data2":   [shelter_data2, {"username":  shelter_data2.email, "password": shelter_data2.password}],
    "invalid_data2": [shelter_data2, {"username":  shelter_data2.email, "password": shelter_data2.password + "1"}]
}

@pytest.fixture
def shelter_data1():
    reg_data =  ShelterLocalRegistration(
        email="test1@gmail.com",
        name="Test Shelter 1",
        password="test1"
    )
    login_data ={
        "username": reg_data.email,
        "password": reg_data.password
    }
    return reg_data, login_data

@pytest.mark.parametrize(
    "shelter_data, expected_login_status_code", 
    [
        pytest.param(shelter_data_set["valid_data1"], 200 ,id="ValidData"),
        pytest.param(shelter_data_set["invalid_data1"], 401, id="InvalidData"),
    ]
)
def test_shelter_registration_and_login(host_name: str, shelter_data: ShelterLocalRegistration, expected_login_status_code: int):
    print("TEST SHELTER REGISTRATION AND LOGIN")
    reg_data = shelter_data[0]
    login_data = shelter_data[1]
    logger.info("Testing shelter registration and login") 
    response = register_shelter(shelter_data=reg_data) 
    assert response.status_code == 200, f"Registration failed. Expected return code 200. Got {response.status_code=}"

    response = login_shelter(login_data=login_data)
    logger.info(f"Shelter registration: {response.json()=}")
    assert response.status_code == expected_login_status_code, f"Expected return code {expected_login_status_code}. Get {response.status_code=}"
    logger.info(f"Shelter logged in: {response.json()=}")

    remove_shelter(jwt_token=get_jwt_token(login_data={"username": reg_data.email, "password": reg_data.password}))

@pytest.fixture
def shelter_data1():
    return shelter_data_set["valid_data1"]

@pytest.fixture
def shelter_data2():
    return shelter_data_set["valid_data2"]



def add_animal(shelter_id: int):
    with open("dog.jpeg", "rb") as f:
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
    
def delete_animal(animal_id: int, shelter_jwt_token: str):
    header = {  "Authorization": f"Bearer {shelter_jwt_token}" }
    return requests.delete(url=f"http://localhost:8080/api/v1/animals/delete/{animal_id}", headers=header)

def test_animal_add_delete(shelter_data1, shelter_data2):
    logger.info("Testing animal add and delete")
    response = register_shelter(shelter_data=shelter_data1[0])
    assert response.status_code == 200, f"Registration failed. Expected return code 200. Got {response.status_code=}"
    jwt1 = get_jwt_token(login_data={"username": shelter_data1[0].email, "password": shelter_data1[0].password})
    response = register_shelter(shelter_data=shelter_data2[0])
    assert response.status_code == 200, f"Registration failed. Expected return code 200. Got {response.status_code=}"
    jwt2 = get_jwt_token(login_data={"username": shelter_data2[0].email, "password": shelter_data2[0].password})
    
    response = add_animal(shelter_id=sheler_profile_id(jwt_token=jwt1))
    logger.info(f"Animal added: {response.json()=}")
    assert response.status_code == 200, f"Animal add failed. Expected return code 200. Got {response.status_code=}"
    animal_id = response.json()["id"]

    response = delete_animal(animal_id=animal_id, shelter_jwt_token=jwt2)
    assert response.status_code == 403, f"Animal delete failed. Expected return code 403. Got {response.status_code=}"

    response = remove_shelter(jwt_token=jwt1)
    response = remove_shelter(jwt_token=jwt2)











