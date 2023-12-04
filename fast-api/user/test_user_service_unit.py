import pytest
from unittest.mock import Mock, patch
from user_app.service.user_service import UserService 
from user_app.controllers.user_controller import UserController
from fastapi import HTTPException  

from user_app.models.user_local_model import UserLocalAuthorization, UserLocalRegistration

from fastapi.security import OAuth2PasswordRequestForm

from pytest_lazyfixture import lazy_fixture

import logging

logger = logging.getLogger(__name__)



# Create a mock UserController for testing
@pytest.fixture
def mock_user_controller():
    logger.info(f"CREATING MOCK OBJECT")
    mock_user_controller: UserController = Mock()
    return mock_user_controller

@pytest.fixture
def mock_user_controller_good_reg(mock_user_controller:UserController):
    logger.info("SETTING UP REGISTRATION SUCCESS MOCK BEHAVIOUR")
    success_reg_mock = mock_user_controller
    success_reg_mock.get_user_by_email.return_value =  None
    success_reg_mock.create_user.return_value = True
    return success_reg_mock

@pytest.fixture
def mock_user_controller_adding_fail(mock_user_controller:UserController):
    logger.info("SETTING UP REGISTRATION ADDING FAIL MOCK BEHAVIOUR")
    success_reg_mock = mock_user_controller
    success_reg_mock.get_user_by_email.return_value =  None
    success_reg_mock.create_user.return_value = False
    return success_reg_mock

@pytest.fixture
def mock_user_controller_bad_reg(mock_user_controller:UserController):
    logger.info("SETTING UP REGISTRATION FAIL MOCK BEHAVIOUR")
    success_reg_mock = mock_user_controller
    success_reg_mock.get_user_by_email.return_value =  "Aboba"
    success_reg_mock.create_user.return_value = True
    return success_reg_mock

# Create a UserService instance with the mock UserController
@pytest.fixture
def user_service(mock_user_controller_good_reg: UserController)->UserService:
    return UserService(mock_user_controller_good_reg)

# Test registering a user


@pytest.mark.parametrize(
                            "user_controller_mock, expected_result, user", 
                            [
                                pytest.param(lazy_fixture("mock_user_controller_good_reg"),    True,   UserLocalRegistration(email="test@example.com", password="test", full_name="test"), id="Registration successfull"),
                                pytest.param(lazy_fixture("mock_user_controller_adding_fail"), False,  UserLocalRegistration(email="aboba@example.com", password="aboba", full_name="aboba"), id="Adding to DB fail"),
                            ],
                        )
def test_register_user_successful(user_service:UserService, user_controller_mock: UserController, expected_result:bool, user:UserLocalRegistration):

   

    result = user_service.register_user(user)

    logger.info(f"RESULT: {result=}, EXPECTED_RESULT: {expected_result=}")

    assert result is expected_result
    user_controller_mock.get_user_by_email.assert_called_once_with(user.email)
    user_controller_mock.create_user.assert_called_once_with(user)




def test_register_fail_user_exists(user_service:UserService, mock_user_controller_bad_reg: UserController):

    user = UserLocalRegistration(email="test@example.com", password="test", full_name="test")
    try:
        result = user_service.register_user(user)
    except HTTPException as e:
        logger.info(f"EXCEPTION caught {e=}")
        assert e.status_code == 409, f"Expected error code: 409\nReceived: {e.status_code}. Exception: {e}"
        mock_user_controller_bad_reg.get_user_by_email.assert_called_once_with("test@example.com")
        mock_user_controller_bad_reg.create_user.assert_not_called()
    else:   
        assert False, f"Expected 409 error code."

# Test authorizing a user
def test_authorize_user(user_service, mock_user_controller:UserController):
    user = OAuth2PasswordRequestForm(username="test@example.com", password="password")
    mock_user_controller.get_user_by_email.return_value = Mock(
        id=1, email="test@example.com", password="hashed_password", salt="salt"
    )
    mock_user_controller._hasher.hash_data.return_value = "hashed_password"  # Mock the hasher method

    result = user_service.authorize_user(user)

    assert result is not None

# Test authorizing a user with incorrect credentials
def test_authorize_user_invalid_credentials(user_service, mock_user_controller):
    user = OAuth2PasswordRequestForm(username="test@example.com", password="wrong_password")
    mock_user_controller.get_user_by_email.return_value = Mock(
        id=1, email="test@example.com", password="hashed_password", salt="salt"
    )
    mock_user_controller._hasher.hash_data.return_value = "hashed_password"  # Mock the hasher method

    try:
        user_service.authorize_user(user)

    except HTTPException as e:
        assert e.status_code == 401, f"Expected error code 401.\nReceived: {e}"

def test_authorize_user_doesnt_exist(user_service, mock_user_controller):
    user = OAuth2PasswordRequestForm(username="test@example.com", password="wrong_password")
    mock_user_controller.get_user_by_email.return_value = None
    mock_user_controller._hasher.hash_data.return_value = None  
    try:
        user_service.authorize_user(user)

    except HTTPException as e:
        assert e.status_code == 401, f"Expected error code 401.\nReceived: {e}"
    else: assert False, "Expected error code 401"

# # Test getting a user by ID
def test_get_user(user_service:UserService, mock_user_controller: UserController):
    user_id = 1
    user_db = Mock(id=user_id, email="test@example.com", full_name="John Doe")
    mock_user_controller.get_user_by_id.return_value = user_db

    result = user_service.get_user(user_id)
    logger.info(f"{result=}")
    assert result.id == user_id
    assert result.email == "test@example.com"
    assert result.full_name == "John Doe"

# Test getting a user by ID when the user doesn't exist
def test_get_user_not_found(user_service: UserService, mock_user_controller: UserController):
    user_id = 1
    mock_user_controller.get_user_by_id.return_value = None

    try:
        user_service.get_user(user_id)

    except HTTPException as e: 
        assert e.status_code == 404,  f"Expected error code 404.\nReceived: {e}"
    else: assert False, "Expected error code 404."