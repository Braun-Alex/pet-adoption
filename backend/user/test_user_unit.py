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



# Test registering a user
user = UserLocalRegistration(email="test@example.com", password="test", name="test")

"""
This module contains unit tests for the `register_user` method in the `UserService` class.

The `register_user` method is responsible for registering a new user. It takes a `UserLocalRegistration` object as input and performs the following steps:
1. Calls the `get_user_by_email` method of the `UserController` to check if a user with the same email already exists.
2. If a user with the same email exists, it raises an HTTPException with status code 409 (Conflict).
3. If a user with the same email does not exist, it calls the `create_user` method of the `UserController` to create a new user.
4. If the user creation is successful, it returns True. Otherwise, it returns False.

The unit tests in this module use the `pytest.mark.parametrize` decorator to define multiple test cases for the `register_user` method. Each test case consists of the following parameters:
- `user_controller_data`: An instance of `UserControllerData` that represents the data to be used for mocking the `UserController` methods.
- `expected_result`: The expected result of the `register_user` method.
- `user`: An instance of `UserLocalRegistration` that represents the user to be registered.

The `test_register_use` function is decorated with the `pytest.mark.parametrize` decorator to run the test cases defined in the decorator. It performs the following steps for each test case:
1. Sets up the mock for the `UserController` using the `setup_user_controller_mock` function.
2. Creates an instance of `UserService` with the mock `UserController`.
3. Calls the `register_user` method of the `UserService` with the `user` parameter.
4. Asserts that the result is equal to the `expected_result`.
5. If an HTTPException is raised, asserts that the status code of the exception is equal to the `expected_result`.
6. Asserts that the `get_user_by_email` method of the `UserController` is called with the correct email.
7. If the `expected_result` is a boolean, asserts that the `create_user` method of the `UserController` is called with the correct user.
8. If the `expected_result` is an HTTPException, asserts that the `create_user` method of the `UserController` is not called.

"""
@pytest.mark.parametrize(
    "user_controller_data, expected_result, user", 
    [
        pytest.param(UserControllerData(get_user_by_email=None, create_user=True), True, user, id="Registration successful"),
        pytest.param(UserControllerData(get_user_by_email=None, create_user=False), False, user, id="Adding to DB fail"),
        pytest.param(UserControllerData(get_user_by_email=UserLocalOutput(id=1, email="test@example.com", name="test"), create_user=False), status.HTTP_409_CONFLICT, user, id="User already exists")
    ],
)
def test_register_use(user_controller_data, mock_user_controller, expected_result, user: UserLocalRegistration):
    """
    Test the `register_user` method of the `UserService` class.

    Parameters:
    - user_controller_data: An instance of `UserControllerData` representing the data to be used for mocking the `UserController` methods.
    - mock_user_controller: A mock object of the `UserController` class.
    - expected_result: The expected result of the `register_user` method.
    - user: An instance of `UserLocalRegistration` representing the user to be registered.

    Returns:
    - None
    """
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





