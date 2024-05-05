from typing import Optional
from pydantic import BaseModel
from backend.shelter.models.shelter_local_model import ShelterLocalRegistration, ShelterLocalOutput
from backend.animal.animal_app.models.animal_local_model import AnimalLocalOut
# from backend.animal.main import app 

from backend.user.user_app.models.user_local_model import UserLocalOutput, UserLocalRegistration
# from backend.user.user_app.users import register_user, authorize_user, get_user

from backend.application.application_app.models.application_local_models import ApplicationIn

import pytest
import logging

from backend.tests.utils import ShelterUtils, AnimalsUtils, ApplicationUtils, UserUtils

import requests

from fastapi.security import OAuth2PasswordRequestForm
from typing import Generator
from fastapi import status


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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

user_data = UserLocalRegistration(
                    email="user@gmail.com",
                    name="User",
                    password="user"
                )


@pytest.fixture
def user_registration_dut() -> Generator[UserLocalRegistration, None, None]:
    UserUtils.register_user(user_data=user_data)
    yield user_data
    user_out = UserUtils.get_user_profile(jwt_token=UserUtils.get_jwt_token(OAuth2PasswordRequestForm(username=user_data.email, password=user_data.password)))
    UserUtils.remove_user(user_id=user_out.id)
    # assert get_user(user_id=user_out.id) == None, f"User not removed. Expected None. Got {get_user(user_id=user_out.id)=}"

@pytest.fixture(scope="module", autouse=True)
def host_name() -> str:
    return "http://localhost:8080"

@pytest.fixture
def shelter_registration_dut() -> Generator[ShelterLocalRegistration, None, None]:
    yield shelter_data
    shelter_out = ShelterUtils.shelter_profile(pattern=shelter_data)
    ShelterUtils.remove_shelter(jwt_token=ShelterUtils.get_jwt_token(OAuth2PasswordRequestForm(username=shelter_data.email, password=shelter_data.password)))
    assert ShelterUtils.get_shelter_by_id(shelter_id=shelter_out.id).status_code == 404, f"Shelter not removed. Expected 404. Got {ShelterUtils.get_shelter_by_id(shelter_id=shelter_out.id).status_code=}"


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

@pytest.fixture(scope="module")
def shelter_login_dut_1() -> Generator[ShelterLocalRegistration, None, None]:
    response = ShelterUtils.register_shelter(shelter_data=shelter_data)
    assert response.status_code == 200, f"Registration failed. Expected return code 200. Got {response.status_code=}"


    yield shelter_data
    sheler_out = ShelterUtils.shelter_profile(pattern=shelter_data)
    ShelterUtils.remove_shelter(jwt_token=ShelterUtils.get_jwt_token(OAuth2PasswordRequestForm(username=shelter_data.email, password=shelter_data.password)))
    assert ShelterUtils.get_shelter_by_id(shelter_id=sheler_out.id).status_code == 404, f"Shelter not removed. Expected 404. Got {ShelterUtils.get_shelter_by_id(shelter_id=sheler_out.id).status_code=}"


@pytest.fixture(scope="module")
def shelter_login_dut_2() -> Generator[ShelterLocalRegistration, None, None]:
    response = ShelterUtils.register_shelter(shelter_data=shelter_data2)
    assert response.status_code == 200, f"Registration failed. Expected return code 200. Got {response.status_code=}"

    yield shelter_data2
    sheler_out = ShelterUtils.shelter_profile(pattern=shelter_data2)
    ShelterUtils.remove_shelter(jwt_token=ShelterUtils.get_jwt_token(OAuth2PasswordRequestForm(username=shelter_data2.email, password=shelter_data2.password)))
    assert ShelterUtils.get_shelter_by_id(shelter_id=sheler_out.id).status_code == 404, f"Shelter not removed. Expected 404. Got {ShelterUtils.get_shelter_by_id(shelter_id=sheler_out.id).status_code=}"




def test_shelter_double_registration(shelter_registration_dut: ShelterLocalOutput):

    logger.info("Testing shelter registration and login") 
    response = ShelterUtils.register_shelter(shelter_data=shelter_registration_dut) 
    assert response.status_code == 200, f"Registration failed. Expected return code 200. Got {response.status_code=}"
    shelter_bd = ShelterUtils.shelter_profile(pattern=shelter_registration_dut)

    assert shelter_bd.email == shelter_registration_dut.email, f"Shelter name does not match. Expected {shelter_registration_dut.name=}, Got {shelter_bd.name=}"
    assert shelter_bd.name == shelter_registration_dut.name 


    logger.info("DOUBLE")
    response = ShelterUtils.register_shelter(shelter_data=shelter_registration_dut) 
    assert response.status_code == 409, f"Registration failed. Expected return code 409. Got {response.status_code=}"

@pytest.mark.parametrize(
                            "shelter_login_date, expected_login_status_code",
                            [
                                pytest.param(OAuth2PasswordRequestForm(username=shelter_data.email, password=shelter_data.password), 200, id="ValidData"),
                                pytest.param(OAuth2PasswordRequestForm(username=shelter_data.email, password=shelter_data.password+"1"), 401, id="InvalidData")
                            ],
                        )
def test_shelter_login(shelter_login_dut_1: ShelterLocalRegistration, shelter_login_date: OAuth2PasswordRequestForm, expected_login_status_code: int):
    logger.info("Testing shelter registration and login") 
    response = ShelterUtils.login_shelter(login_data=shelter_login_date)
    assert response.status_code == expected_login_status_code, f"Expected return code {expected_login_status_code}. Get {response.status_code=}"
    logger.info(f"Shelter logged in: {response.json()=}")

def test_shelter_profile(shelter_login_dut_1: ShelterLocalRegistration):
    response = ShelterUtils.login_shelter(login_data=OAuth2PasswordRequestForm(username=shelter_login_dut_1.email, password=shelter_login_dut_1.password))
    assert response.status_code == 200, f"LogIn failede. Expected return code 200. Got {response.status_code=}"
    shelter_jwt = response.json()['access_token']
    shelter_profile = ShelterUtils.get_shelter(jwt=shelter_jwt)
    assert shelter_profile.email == shelter_login_dut_1.email, f"Shelter email does not match. Expected {shelter_login_dut_1.email=}, Got {shelter_profile.email=}"
    assert shelter_profile.name == shelter_login_dut_1.name, f"Shelter name does not match. Expected {shelter_login_dut_1.name=}, Got {shelter_profile.name=}"
    

# @pytest.fixture
# def shelter_data1():
#     return shelter_data_set["valid_data1"]

# @pytest.fixture
# def shelter_data2():
#     return shelter_data_set["valid_data2"]





@pytest.mark.parametrize(
                            "expected_remove_status_code, expected_check_status_code",
                            [
                                pytest.param(status.HTTP_200_OK       , status.HTTP_404_NOT_FOUND,          id="Shelter 1 remove its animal"),
                                pytest.param(status.HTTP_403_FORBIDDEN, status.HTTP_200_OK,                 id="Shelter 1 remove animal of shelter 2"),
                            ],
                        )
def test_animal_add_remove(request, shelter_login_dut_1: ShelterLocalRegistration, shelter_login_dut_2: ShelterLocalRegistration, expected_remove_status_code: int, expected_check_status_code: int):    
    test_id = request.node.name


    logger.info("Testing animal add and delete")
    shelter_jwt1 = ShelterUtils.get_jwt_token(OAuth2PasswordRequestForm(username=shelter_login_dut_1.email, password=shelter_login_dut_1.password))
    shelter_jwt2 = ShelterUtils.get_jwt_token(OAuth2PasswordRequestForm(username=shelter_login_dut_2.email, password=shelter_login_dut_2.password))

    jwt_for_animal_remove = shelter_jwt1

    response = AnimalsUtils.add_animal(shelter_id=ShelterUtils.shelter_profile_id(shelter_jwt1))
    logger.info(f"Animal added: {response.json()=}")
    assert response.status_code == 200, f"Animal add failed. Expected return code 200. Got {response.status_code=}"



    if "Shelter 1 remove animal of shelter 2" in test_id:
        logger.info(f"{test_id=}")
        jwt_for_animal_remove = shelter_jwt2
    animal_remove_response = AnimalsUtils.delete_animal(animal_id=response.json()['id'], shelter_jwt_token=jwt_for_animal_remove)
    assert animal_remove_response.status_code == expected_remove_status_code, f"Expected return code {expected_remove_status_code}. Got {animal_remove_response.status_code=}"

    assert AnimalsUtils.get_animal_by_id(animal_id=response.json()['id']).status_code == expected_check_status_code, f"Animal not removed. Expected {expected_check_status_code}. Got {AnimalsUtils.get_animal_by_id(animal_id=response.json()['id']).status_code=}"


# def test_animal_add_remove(request, shelter_login_dut_1: ShelterLocalRegistration, shelter_login_dut_2: ShelterLocalRegistration, expected_remove_status_code: int, expected_check_status_code: int):    
#     test_id = request.node.name

#     logger.info("Testing animal add and delete")
#     shelter_jwt1 = ShelterUtils.get_jwt_token(OAuth2PasswordRequestForm(username=shelter_login_dut_1.email, password=shelter_login_dut_1.password))
#     shelter_jwt2 = ShelterUtils.get_jwt_token(OAuth2PasswordRequestForm(username=shelter_login_dut_2.email, password=shelter_login_dut_2.password))

#     jwt_for_animal_remove = shelter_jwt1

#     response = AnimalsUtils.add_animal(shelter_id=ShelterUtils.shelter_profile_id(shelter_jwt1))
#     logger.info(f"Animal added: {response.json()=}")
#     assert response.status_code == 200, f"Animal add failed. Expected return code 200. Got {response.status_code=}"



#     if "Shelter 1 remove animal of shelter 2" in test_id:
#         logger.info(f"{test_id=}")
#         jwt_for_animal_remove = shelter_jwt2
#     animal_remove_response = AnimalsUtils.delete_animal(animal_id=response.json()['id'], shelter_jwt_token=jwt_for_animal_remove)
#     assert animal_remove_response.status_code == expected_remove_status_code, f"Expected return code {expected_remove_status_code}. Got {animal_remove_response.status_code=}"

#     assert AnimalsUtils.get_animal_by_id(animal_id=response.json()['id']).status_code == expected_check_status_code, f"Animal not removed. Expected {expected_check_status_code}. Got {AnimalsUtils.get_animal_by_id(animal_id=response.json()['id']).status_code=}"



# def test_animal_

def test_application(user_registration_dut: ShelterLocalRegistration, shelter_login_dut_1: ShelterLocalRegistration):
    shelter_jwt = ShelterUtils.get_jwt_token(OAuth2PasswordRequestForm(username=shelter_login_dut_1.email, password=shelter_login_dut_1.password))
    animal_create_response = AnimalsUtils.add_animal(shelter_id=ShelterUtils.shelter_profile_id(shelter_jwt))
    assert animal_create_response.status_code == 200, f"Animal add failed. Expected return code 200. Got {animal_create_response.status_code=}"
    animal_id = animal_create_response.json()['id']

    shelter_id = ShelterUtils.shelter_profile_id(jwt_token=shelter_jwt)
    user_jwt = UserUtils.get_jwt_token(OAuth2PasswordRequestForm(username=user_registration_dut.email, password=user_registration_dut.password))
    user_id = UserUtils.user_id(jwt_token=user_jwt) 
    application = ApplicationIn(user_id=user_id, shelter_id=shelter_id, animal_id=animal_id)
    logger.info(f"{application=}")
    application_response = ApplicationUtils.create_application(application_data=application)
    assert application_response.status_code == 200, f"Application add failed. Expected return code 200. Got {application_response.status_code=}"

# def test_animal_remove()










