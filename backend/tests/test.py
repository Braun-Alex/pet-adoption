from typing import Optional
from pydantic import BaseModel
from backend.shelter.models.shelter_local_model import ShelterLocalRegistration, ShelterLocalOutput
from backend.animal.animal_app.models.animal_local_model import AnimalLocalOut
# from backend.animal.main import app 

from backend.user.user_app.models.user_local_model import UserLocalOutput, UserLocalRegistration
# from backend.user.user_app.users import register_user, authorize_user, get_user

from backend.application.application_app.models.application_local_models import ApplicationIn, ApplicationStatus, ApplicationUpdate, ApplicationOut

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
    user_jwt = UserUtils.get_jwt_token(OAuth2PasswordRequestForm(username=user_data.email, password=user_data.password))
    user_out = UserUtils.get_user_profile(jwt_token=user_jwt)
    UserUtils.remove_user(jwt_token=user_jwt)

@pytest.fixture
def user_dut() -> Generator[UserLocalRegistration, None, None]:
    yield user_data
    user_jwt = UserUtils.get_jwt_token(OAuth2PasswordRequestForm(username=user_data.email, password=user_data.password))
    user_out = UserUtils.get_user_profile(jwt_token=user_jwt)
    UserUtils.remove_user(jwt_token=user_jwt)
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
    """
    Test case for shelter double registration.

    This test verifies that the shelter registration process correctly handles double registration attempts.
    It checks if the registration fails with a return code of 409 when attempting to register the same shelter twice.

    Also this test checks if registration works fine and the returned shelter data matches the expected values.

    Args:
        shelter_registration_dut (ShelterLocalOutput): The shelter data for registration.

    Raises:
        AssertionError: If the registration fails or the returned shelter data does not match the expected values.

    """
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
    "shelter_login_data, expected_login_status_code",
    [
        pytest.param(OAuth2PasswordRequestForm(username=shelter_data.email, password=shelter_data.password), 200, id="ValidData"),
        pytest.param(OAuth2PasswordRequestForm(username=shelter_data.email, password=shelter_data.password+"1"), 401, id="InvalidData")
    ],
)
def test_shelter_login(shelter_login_dut_1: ShelterLocalRegistration, shelter_login_data: OAuth2PasswordRequestForm, expected_login_status_code: int):
    """
    Test the login functionality for a shelter.
    It consist of two test cases:
        - ValidData: The shelter logs in with the correct credentials.
        - InvalidData: The shelter logs in with incorrect credentials.

    Args:
        shelter_login_dut_1 (ShelterLocalRegistration): A fixture that sets up the test environment for shelter registration.
        shelter_login_date (OAuth2PasswordRequestForm): The login data for the shelter.
        expected_login_status_code (int): The expected HTTP status code for the login request.

    Returns:
        None

    Raises:
        AssertionError: If the actual status code does not match the expected status code.
    """
    logger.info("Testing shelter registration and login") 
    response = ShelterUtils.login_shelter(login_data=shelter_login_data)
    assert response.status_code == expected_login_status_code, f"Expected return code {expected_login_status_code}. Get {response.status_code=}"
    logger.info(f"Shelter logged in: {response.json()=}")



def test_shelter_profile(shelter_login_dut_1: ShelterLocalRegistration):
    """
    Test case to verify the shelter profile.
    Firstly test registers a shelter and then logs in with the registered credentials.
    Then it checks if the returned shelter profile matches the expected values.

    Args:
        shelter_login_dut_1 (ShelterLocalRegistration): An instance of the ShelterLocalRegistration class.

    Raises:
        AssertionError: If the login fails or the shelter profile does not match the expected values.

    Returns:
        None
    """
    response = ShelterUtils.login_shelter(login_data=OAuth2PasswordRequestForm(username=shelter_login_dut_1.email, password=shelter_login_dut_1.password))
    assert response.status_code == 200, f"LogIn failed. Expected return code 200. Got {response.status_code=}"
    shelter_jwt = response.json()['access_token']
    shelter_profile = ShelterUtils.get_shelter(jwt=shelter_jwt)
    assert shelter_profile.email == shelter_login_dut_1.email, f"Shelter email does not match. Expected {shelter_login_dut_1.email=}, Got {shelter_profile.email=}"
    assert shelter_profile.name == shelter_login_dut_1.name, f"Shelter name does not match. Expected {shelter_login_dut_1.name=}, Got {shelter_profile.name=}"



@pytest.mark.parametrize(
    "expected_remove_status_code, expected_check_status_code",
    [
        pytest.param(status.HTTP_200_OK, status.HTTP_404_NOT_FOUND, id="Shelter 1 remove its animal"),
        pytest.param(status.HTTP_403_FORBIDDEN, status.HTTP_200_OK, id="Shelter 1 remove animal of shelter 2"),
    ],
)
def test_animal_add_remove(request, shelter_login_dut_1: ShelterLocalRegistration, shelter_login_dut_2: ShelterLocalRegistration, expected_remove_status_code: int, expected_check_status_code: int):
    """
    Test case for adding and removing an animal.
    The test case consists of two scenarios:
        - Shelter 1 removes its own animal.
            Expects that shelter is able to remove its animal
        - Shelter 1 removes the animal of Shelter 2.
            Expects that shelter is not able to remove the animal of another shelter.

    Args:
        request: The pytest request object.
        shelter_login_dut_1: The first shelter's login details.
        shelter_login_dut_2: The second shelter's login details.
        expected_remove_status_code: The expected status code after removing the animal.
        expected_check_status_code: The expected status code after checking if the animal is removed.
    """
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



@pytest.mark.parametrize(
                            "expected_new_application_status",
                            [
                                pytest.param(ApplicationStatus.ACCEPTED, id="Approve"),
                                pytest.param(ApplicationStatus.REJECTED, id="Reject"),
                            ],
)
def test_application(user_registration_dut: ShelterLocalRegistration, shelter_login_dut_1: ShelterLocalRegistration, expected_new_application_status: ApplicationStatus):
    """
    Test the application process by creating and updating an application.
    The test case consists of two scenarios:
        - Approve: The shelter approves the application.
            Shelter accepts the application. The application status is updated to ACCEPTED.
        - Reject: The shelter rejects the application.
            Shelter rejects the application. The application status is updated to REJECTED.

    Args:
        user_registration_dut (ShelterLocalRegistration): The user registration data for the test.
        shelter_login_dut_1 (ShelterLocalRegistration): The shelter login data for the test.
        expected_new_application_status (ApplicationStatus): The expected status of the updated application.

    Returns:
        None
    """
    shelter_jwt = ShelterUtils.get_jwt_token(OAuth2PasswordRequestForm(username=shelter_login_dut_1.email, password=shelter_login_dut_1.password))

    logger.info(f" {expected_new_application_status=}")
    animal_create_response = AnimalsUtils.add_animal(shelter_id=ShelterUtils.shelter_profile_id(shelter_jwt))
    assert animal_create_response.status_code == 200, f"Animal add failed. Expected return code 200. Got {animal_create_response.status_code=}"
    animal_id = animal_create_response.json()['id']

    shelter_id = ShelterUtils.shelter_profile_id(jwt_token=shelter_jwt)
    user_jwt = UserUtils.get_jwt_token(OAuth2PasswordRequestForm(username=user_registration_dut.email, password=user_registration_dut.password))
    user_id = UserUtils.user_id(jwt_token=user_jwt) 
    application = ApplicationIn(user_id=user_id, shelter_id=shelter_id, animal_id=animal_id)
    
    application_response = ApplicationUtils.create_application(application_data=application)
    
    assert application_response.status_code == 200, f"Application add failed. Expected return code 200. Got {application_response.status_code=}"
    logger.info(f"application_response: {application_response.json()}")
    application_id = application_response.json()
    logger.info(f"Created application with id {application_id}")

    application_update_data = ApplicationUpdate(id=application_id, status=expected_new_application_status, user_id=user_id, shelter_id=shelter_id, animal_id=animal_id)

    update_response_json = ApplicationUtils.update_application(application_data=application_update_data).json()
    logger.info(f"After updating application {update_response_json=}")

    updated_application = ApplicationOut(**ApplicationUtils.get_application(application_id=application_id).json()[0])
    logger.info(f"application after updating {updated_application=}")

    assert updated_application.status == expected_new_application_status, f"Application status does not match. Expected {expected_new_application_status}. Got {update_response_json['status']=}"

def test_user_double_registration(user_dut: UserLocalRegistration):
    """
    Test case for user double registration.

    This test verifies that the user registration process correctly handles double registration attempts.
    It checks if the registration fails with a return code of 409 when attempting to register the same user twice.

    Also this test checks if registration works fine and the returned user data matches the expected values.

    Args:
        user_registration_dut (UserLocalRegistration): The user data for registration.

    Raises:
        AssertionError: If the registration fails or the returned user data does not match the expected values.

    """
    logger.info("Testing user registration and login") 
    response = UserUtils.register_user(user_data=user_dut) 
    assert response.status_code == 200, f"Registration failed. Expected return code 200. Got {response.status_code=}"
    user_jwt = UserUtils.get_jwt_token(OAuth2PasswordRequestForm(username=user_dut.email, password=user_dut.password))
    user_local = UserUtils.get_user_profile(jwt_token=user_jwt)

    assert user_local.email == user_dut.email, f"User email does not match. Expected {user_dut.email=}, Got {user_local.email=}"
    assert user_local.name == user_dut.name, f"User name does not match. Expected {user_dut.name=}, Got {user_local.name=}"

    logger.info("DOUBLE")
    response = UserUtils.register_user(user_data=user_dut) 
    assert response.status_code == 409, f"Registration failed. Expected return code 409. Got {response.status_code=}"



@pytest.mark.parametrize(
    "user_login_data, expected_login_status_code",
    [
        pytest.param(OAuth2PasswordRequestForm(username=user_data.email, password=user_data.password) ,200, id="ValidData"),
        pytest.param(OAuth2PasswordRequestForm(username=user_data.email, password=user_data.password+"1"), 401, id="InvalidData"),
    ],
)
def test_user_login(user_registration_dut: UserLocalRegistration, expected_login_status_code: int, user_login_data: OAuth2PasswordRequestForm):
    """
    Test the login functionality for a user.
    It consist of two test cases:
        - ValidData: The user logs in with the correct credentials.
        - InvalidData: The user logs in with incorrect credentials.

    Args:
        user_dut (UserLocalRegistration): A fixture that sets up the test environment for user registration.
        expected_login_status_code (int): The expected HTTP status code for the login request.
        user_login_data (OAuth2PasswordRequestForm): The login data for the user.

    Returns:
        None

    Raises:
        AssertionError: If the actual status code does not match the expected status code.
    """
    logger.info("Testing user registration and login") 
    response = UserUtils.login_user(login_data=user_login_data)
    assert response.status_code == expected_login_status_code, f"Expected return code {expected_login_status_code}. Get {response.status_code=}"
    logger.info(f"User logged in: {response.json()}")









