import pytest
from unittest.mock import Mock

from service.shelter_service import ShelterService
from controllers.shelter_controller import ShelterController
from models.shelter_local_model import ShelterLocalRegistration, ShelterLocalOutput, ShelterLocalUpdate
from models.shelter_db_model import ShelterDB   
# from database import SessionLocal   
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import status, HTTPException

import yaml

import logging.config

with open('logger_conf.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)

logger = logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

class ShelterControllerData:
    def __init__(self, create_shelter_ret_val: bool = None, get_shelter_by_email_ret_val: ShelterLocalOutput = None, get_shelter_by_id_ret_val: ShelterLocalOutput = None, 
    _get_shelter_by_email_ret_val: ShelterDB = None):
        self.create_shelter_ret_val = create_shelter_ret_val
        self.get_shelter_by_email_ret_val = get_shelter_by_email_ret_val
        self.get_shelter_by_id_ret_val = get_shelter_by_id_ret_val
        self._get_shelter_by_email_ret_val = _get_shelter_by_email_ret_val
    

@pytest.fixture
def mock_shelter_controller():
    return Mock(spec=ShelterController)


def create_test_specific_mock_shelter_controller(shelter_controller_mock, controller_data: ShelterControllerData):
    shelter_controller_mock.create_shelter.return_value = controller_data.create_shelter_ret_val
    shelter_controller_mock.get_shelter_by_email.return_value = controller_data.get_shelter_by_email_ret_val
    shelter_controller_mock._get_shelter_by_email.return_value = controller_data._get_shelter_by_email_ret_val
    shelter_controller_mock.get_shelter_by_id.return_value = controller_data.get_shelter_by_id_ret_val

@pytest.mark.parametrize(
    "controller_data", 
    [
        pytest.param(ShelterControllerData(get_shelter_by_email_ret_val=None, create_shelter_ret_val=True), id="Good registration"), 
        pytest.param(ShelterControllerData(get_shelter_by_email_ret_val=ShelterLocalOutput(id=1, name="Test Shelter", email = "test@gmail.com")), id="User exists"),
    ],
)
def test_register_shelter(mock_shelter_controller, controller_data: ShelterControllerData):
    """
    Test case for the register_shelter method of the ShelterService class.

    This test case verifies the behavior of the register_shelter method when different controller data is provided.

    Args:
        mock_shelter_controller (Mock): A mock object of the ShelterController class.
        controller_data (ShelterControllerData): The data to be used for the test.

    Test Points:
    - The method should create a new shelter when the create_shelter_ret_val is True and both get_shelter_by_email_ret_val and get_shelter_by_id_ret_val are None.
    - The method should handle a bad registration scenario when the create_shelter_ret_val is True, get_shelter_by_email_ret_val is not None, and get_shelter_by_id_ret_val is None.
    - The method should raise an HTTPException with status code 409 when a conflict occurs during registration.
    """

    logger.info(f"Testing register_shelter with {controller_data=}")

    create_test_specific_mock_shelter_controller(shelter_controller_mock=mock_shelter_controller, controller_data=controller_data)
    service = ShelterService(mock_shelter_controller)
    registration_data = ShelterLocalRegistration(name="Test Shelter", email="test@gmail.com", password="password")

    # Act
    try:
        result = service.register_shelter(registration_data)

        # Assert
        assert result == True, f"Shelter registration failed. Expected True, got {result}"
    except HTTPException as e:
        # Handle the exception as a valid case
        assert e.status_code == status.HTTP_409_CONFLICT, f"Expected status code {status.HTTP_409_CONFLICT}. Got {e.status_code=}"
        mock_shelter_controller.get_shelter_by_email.assert_called_once_with(registration_data.email)
        mock_shelter_controller.create_shelter.assert_not_called()
        logger.info(f"Exception: {e}")


@pytest.mark.parametrize( "controller_data, user_data", 
                         [
                            pytest.param(ShelterControllerData(_get_shelter_by_email_ret_val=None), OAuth2PasswordRequestForm(username="test", password="test"), id="user does not exist"), 
                            pytest.param(ShelterControllerData(_get_shelter_by_email_ret_val=ShelterDB(id=1, email="test@gmail.com", salt="test_salt", password="test")), OAuth2PasswordRequestForm(username="test@gmail.com", password="test1"), id="Invalid password"),
                            pytest.param(ShelterControllerData(_get_shelter_by_email_ret_val=ShelterDB(id=1, email="test@gmail.com", salt="test_salt", password="test")), OAuth2PasswordRequestForm(username="test@gmail.com", password="test"), id="Valid credentials"),
                        ], 
                        )       
def test_authorize_shelter(mock_shelter_controller, controller_data: ShelterControllerData, user_data: OAuth2PasswordRequestForm):
    """
    Test case for the authorize_shelter method of the ShelterService class.

    This test case verifies the behavior of the authorize_shelter method when different controller data is provided.

    Args:
        mock_shelter_controller (Mock): A mock object of the ShelterController class.

    Test Points:
    - The method should authorize a shelter when the provided credentials are correct.
    - The method should raise an HTTPException with status code 401 when the provided credentials are incorrect.
    """

    logger.info("Testing authorize_shelter")

    create_test_specific_mock_shelter_controller(shelter_controller_mock=mock_shelter_controller, controller_data=controller_data)
    service = ShelterService(mock_shelter_controller)
    try:
        result = service.authorize_shelter(user_data)
        
    except HTTPException as e:
        assert e.status_code == status.HTTP_401_UNAUTHORIZED, f"Expected status code {status.HTTP_401_UNAUTHORIZED}. Got {e.status_code=}"
        mock_shelter_controller._get_shelter_by_email.assert_called_once_with(user_data.username)
        logger.info(f"Exception: {e}")


    
