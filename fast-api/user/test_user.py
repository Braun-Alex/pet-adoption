from httpx import Response
import pytest
import logging

import json

from fastapi.testclient import TestClient

from user_app.models.user_local_model import UserLocalRegistration, UserLocalAuthorization, UserLocalOutput

import random
import string

from fastapi.security import OAuth2PasswordRequestForm

from user_app.dependencies.dependencies import get_current_user

from pytest_lazyfixture import lazy_fixture

from main import app 


logger = logging.getLogger(__name__)

@pytest.fixture(scope="module")
def client() -> TestClient:
    logger.info(f"FIXTURE")
    yield TestClient(app)

@pytest.fixture(scope="function")
def signup_user_fixture():
    return UserLocalRegistration(
                                    email=''.join(random.choice(string.ascii_lowercase) for _ in range(5)),
                                    full_name=''.join(random.choice(string.ascii_lowercase) for _ in range(5)),
                                    password="autotest"
                                )
    

@pytest.fixture(scope="function")
def login_user_valid_fixture(signup_user_fixture: UserLocalRegistration):
    return {
                "username": signup_user_fixture.email,
                "password": signup_user_fixture.password,
            }

@pytest.fixture(scope="function")
def login_user_invalid_fixture(signup_user_fixture: UserLocalRegistration):
    return {
                "username": signup_user_fixture.email,
                "password": "shit",
            }

def sign_up(user: UserLocalRegistration, client: TestClient)->Response:
    logger.info(f"Registrating user: {user=}")
    return client.post("/api/v1/users/signup/", json=user.model_dump())

def log_in(user:dict, client:TestClient) ->Response:
    logger.info(f"Authorizating user: {user=}")

    return client.post(
        "/api/v1/users/login/", data=user, 
    )

@pytest.mark.parametrize(
                            "signup_user, login_user, registration_status_code, login_status_code", 
                            [
                                pytest.param(lazy_fixture("signup_user_fixture"), lazy_fixture("login_user_valid_fixture"),200,200, id="ValidLogIn"),
                                pytest.param(lazy_fixture("signup_user_fixture"), lazy_fixture("login_user_invalid_fixture"),200,401, id="InValidLogIn"),
                            ],
                        )
def test_registration_and_login(client: TestClient, signup_user: UserLocalRegistration, login_user, registration_status_code, login_status_code):
    # Registration test

    logger.info(f"{signup_user= }, \n{login_user=}\n{registration_status_code=}\n {login_status_code=}")

    registration_response = sign_up(user=signup_user, client=client)
    assert registration_response.status_code == registration_status_code, f"Sign Up procedure failed. \n Expected code: {registration_status_code=},  Recieved code: {registration_response=}"

    # If registration was successful, proceed to login
    login_response = log_in(user=login_user, client=client)
    assert login_response.status_code == login_status_code, f"LogIn Procedure failed.\nExpeceted code {login_status_code}, Recieved: {login_response=}"

@pytest.fixture(scope="function") 
def jwt_token(signup_user_fixture: UserLocalRegistration, login_user_valid_fixture, client: TestClient)->str:
    sign_up_data = signup_user_fixture
    log_in_data = login_user_valid_fixture
    assert sign_up(user=sign_up_data, client=client).status_code ==200, "Sign Up procedure failed"
    log_in_response = log_in(user=log_in_data, client=client)
    assert log_in_response.status_code ==200, "Log In procedure failed"

    token = log_in_response.json()['access_token']
    logger.debug(f"{token=}")
    return token

@pytest.fixture(scope="function") 
def authorization_header(jwt_token:str) -> str:
    return {  "Authorization": f"Bearer {jwt_token}" }

@pytest.fixture(scope="function") 
def expected_user_profile(jwt_token:str, signup_user_fixture:UserLocalRegistration):
    user_id=get_current_user(token=jwt_token).sub
    return UserLocalOutput(id=user_id, email=signup_user_fixture.email, full_name=signup_user_fixture.full_name)


def test_get_info_by_token(authorization_header:dict, client: TestClient, expected_user_profile: UserLocalOutput):
    logger.info(f"test_get_info_by_token")

    logger.info(f"{expected_user_profile=}")

    profile_response = client.get("/api/v1/users/profile", headers=authorization_header)
    assert profile_response.json() == expected_user_profile.model_dump(), f"Expected: {expected_user_profile}\nReceived: {profile_response}"
