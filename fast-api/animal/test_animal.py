import pytest
import logging.config

from fastapi.testclient import TestClient
from fastapi import HTTPException, status

from animal_app.service.animal_service import AnimalService
from animal_app.controllers.animal_controller import AnimalController

from unittest.mock import patch, Mock

from animal_app.models.animal_local_model import AnimalLocalIn, AnimalLocalOut

from main import app 

import yaml




with open('/app/logger_conf.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)

logging.config.dictConfig(config)
logger = logging.getLogger(__name__)


class AnimalControllerData:
    def __init__(self, get_animal,  delete_animal):
        self.get_animal = get_animal
        self.delete_animal = delete_animal


@pytest.fixture
def mock_animal_controller():
    return Mock(spec=AnimalController)

animal = AnimalLocalOut(id=1, name="animal_test", type="animal_tes", shelter_id=1)

def setup_animal_controller_mock(mock_animal_controller, animal_controller_data: AnimalControllerData):
    mock_animal_controller.get_animal.return_value = animal_controller_data.get_animal
    mock_animal_controller.delete_animal.return_value = animal_controller_data.delete_animal

@pytest.mark.parametrize(
    "animal_controller_data, animal_id, sheler_id ,expected_result",
    [
        pytest.param(AnimalControllerData(get_animal=animal, delete_animal=True), 1, 1, True, id="Delete animal happy path"),
        pytest.param(AnimalControllerData(get_animal=animal, delete_animal=False), 1, 2, status.HTTP_403_FORBIDDEN, id="Unauthorized delete animal"),
        pytest.param(AnimalControllerData(get_animal=None, delete_animal=False), 1, None, True, id="Shelter is None"),
       
    ]
)
def test_delete_animal(mock_animal_controller, animal_controller_data: AnimalControllerData, animal_id, sheler_id, expected_result):
    """
    Test the delete_animal method of the AnimalService class.

    Parameters:
    - mock_animal_controller: A mock object of the AnimalController class.
    - animal_controller_data: An instance of the AnimalControllerData class containing data for the animal controller.
    - animal_id: The ID of the animal to be deleted.
    - shelter_id: The ID of the shelter where the animal is located.
    - expected_result: The expected result of the delete operation.

    Returns:
    - None

    Raises:
    - AssertionError: If the result of the delete operation does not match the expected result.
    - HTTPException: If an HTTP exception occurs during the delete operation.

    Test Points:
    - Shelter who owned an animal should be able to delete an animal successfully.
    - Shelter who does not own an animal should not be able to delete the animal.
    - Shelter who does not exist should not be able to delete the animal.

    """
    setup_animal_controller_mock(mock_animal_controller, animal_controller_data)
    animal_service = AnimalService(animal_controller=mock_animal_controller)
    try:
        result = animal_service.delete_animal(id=animal_id, shelter_id=sheler_id)
        assert result == expected_result, f"Expected {expected_result}, but got {result}"
    except HTTPException as e:
        assert e.status_code == expected_result, f"Expected {expected_result}, but got {e.status_code}"
