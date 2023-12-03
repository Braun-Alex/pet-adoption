import pytest
import logging

import json

from fastapi.testclient import TestClient

from user_app.models.user_local_model import UserLocalRegistration, UserLocalAuthorization\

import random
import string

from fastapi.security import OAuth2PasswordRequestForm

from main import app 





logger = logging.getLogger(__name__)


@pytest.fixture()
def client() -> TestClient:
    logger.info(f"FIXTURE")
    return TestClient(app)

# @pytest.fixture()
# def new_user() -> UserLocalRegistration:
#     email=random.choices(string.ascii_lowercase)
#     return UserLocalRegistration(email="autotest", full_name="autotest", password="autotest")

# def test_signup(user_app_client: TestClient, new_user:UserLocalRegistration):
#     test_client = user_app_client
#     # logger.info("Test started")
#     # logger.debug("DEBUG")
#     # logger.warning("warning")
#     # logger.error("error")

#     logger.debug(f"Model to JSON: {new_user.model_dump()}")

#     # response = test_client.get("/api/v1/users/exists/1")
#     response  = test_client.post(
#                                     "/api/v1/users/signup/",
#                                     json=new_user.model_dump(),
#                                 )
#     logger.info(f"{response=}")


VALID_NAME = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
VALID_EMAIL = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))

VALID_NAME2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
VALID_EMAIL2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))

test_data = [
    (
        UserLocalRegistration(email=VALID_EMAIL, full_name=VALID_NAME, password="autotest"), 
        # OAuth2PasswordRequestForm(username=VALID_EMAIL, password="autotest"),
        {
            "username": VALID_EMAIL,
            "password":"autotest",
        },
        200,  # Expected status code for registration
        200,  # Expected status code for login

    ),
    (
        UserLocalRegistration(email=VALID_NAME2, full_name=VALID_NAME2, password="autotest1"), 
        {
            "username": VALID_EMAIL,
            "password":"shit",
        },
        200,  # Expected status code for registration
        401,  # Expected status code for login
    ),
    # Add more test cases here as needed
]

@pytest.mark.parametrize("signin_user, login_user, registration_status_code, login_status_code", test_data, ids=["ValidLogIn", "NonValidLogIn"])
def test_registration_and_login(client: TestClient, signin_user: UserLocalRegistration, login_user, registration_status_code, login_status_code):
    # Registration test

    logger.info(f"{signin_user= }, \n{login_user=}\n{registration_status_code=}\n {login_status_code=}")

    registration_response = client.post("/api/v1/users/signup/", json=signin_user.model_dump())
    assert registration_response.status_code == registration_status_code, f"Sign Up procedure failed. \n Expected code: {registration_status_code=},  Recieved code: {registration_response=}"

    # If registration was successful, proceed to login
    login_response = client.post(
        "/api/v1/users/login/", data=login_user, 
    )
    assert login_response.status_code == login_status_code, f"LogIn Procedure failed.\nExpeceted code {login_status_code}, Recieved: {login_response=}"
