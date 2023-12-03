import pytest
import logging

from fastapi.testclient import TestClient

from animal_app.models.animal_local_model import AnimalLocalIn

from main import app 





logger = logging.getLogger(__name__)


@pytest.fixture()
def user_app_client() -> TestClient:
    logger.info(f"FIXTURE")
    return TestClient(app)

# @pytest.fixture()
# def new_user() -> UserLocalRegistration:
#     return UserLocalRegistration(email="autotest", full_name="autotest", password="autotest")

def test_signup(user_app_client: TestClient,):
    test_client = user_app_client
    logger.info("Test started")
    logger.debug("DEBUG")
    logger.warning("warning")
    logger.error("error")

    logger.info(f"Model to JSON: ")
    # animal: AnimalLocalIn = AnimalLocalIn(name=)
    # response = test_client.get("/api/v1/users/exists/1")
    response  = test_client.post(
                                    "/api/v1/animals/add",
                                   
                                    # json=new_user.model_dump_json(),
                                    json={
                                        "name": "animal_test",
                                        "type": "animal_test",
                                        "sex": "animal_test",
                                        "shelter_id": 5
                                        },
                                )
    logger.info(f"{response=}")

def test_pass():
    logger.info("DUMMY TEST")
    assert True

def test_fail():
    logger.info("DUMMY TEST")
    assert False