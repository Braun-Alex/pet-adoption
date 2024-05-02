import pytest
from unittest.mock import Mock
from user_app.service.user_service import UserService 
from user_app.controllers.user_controller import UserController
from fastapi import HTTPException , status

from user_app.models.user_local_model import  UserLocalRegistration, UserLocalOutput


# from pytest_lazyfixture import lazy_fixture

import logging

logger = logging.getLogger(__name__)


class UserControllerData:
    def __init__(self, get_user_by_email, create_user) -> None:
        self.get_user_by_email = get_user_by_email
        self.create_user = create_user

# Create a mock UserController for testing
@pytest.fixture
def mock_user_controller():
    logger.info(f"CREATING MOCK OBJECT")
    return Mock(spec=UserController)

def setup_user_controller_mock(mock_user_controller, controller_data:UserControllerData):
    mock_user_controller.get_user_by_email.return_value = controller_data.get_user_by_email
    mock_user_controller.create_user.return_value = controller_data.create_user

# Create a UserService instance with the mock UserController
# @pytest.fixture
# def user_service(mock_user_controller_good_reg: UserController)->UserService:
#     return UserService(mock_user_controller_good_reg)

# Test registering a user
user = UserLocalRegistration(email="test@example.com", password="test", name="test")

@pytest.mark.parametrize(
                            "user_controller_data, expected_result, user", 
                            [
                                pytest.param( UserControllerData(get_user_by_email=None, create_user=True), True,  user , id="Registration successfull"),
                                pytest.param(UserControllerData(get_user_by_email=None, create_user=False), False,  user, id="Adding to DB fail"),
                                pytest.param(UserControllerData(get_user_by_email=UserLocalOutput(id=1, email="test@example.com", name="test"), create_user=False), status.HTTP_409_CONFLICT,  user, id="User already exists")
                            ],
                        )
def test_register_use( user_controller_data, mock_user_controller, expected_result, user:UserLocalRegistration):

    setup_user_controller_mock(mock_user_controller, controller_data=user_controller_data)
    user_service = UserService(mock_user_controller)
    try:
        result = user_service.register_user(user)
        assert result is expected_result, f"Expected {expected_result}, but got {result}"
    except HTTPException as e:
        assert e.status_code == expected_result, f"Expected {expected_result}, but got {e.status_code}"

    mock_user_controller.get_user_by_email.assert_called_once_with(user.email)
    if isinstance(expected_result, bool):
        mock_user_controller.create_user.assert_called_once_with(user)
    elif isinstance(expected_result, HTTPException):
        mock_user_controller.create_user.assert_not_called()





