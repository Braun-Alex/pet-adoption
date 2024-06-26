from abc import abstractmethod
from typing import Optional
from animal_app.models.animal_local_model import AnimalLocalIn, AnimalLocalOut

from animal_app.controllers.animal_controller import AnimalController
from fastapi import APIRouter, HTTPException

import os
import httpx

import logging

logger = logging.getLogger(__name__)

class AnimaServicelInterface:
    @abstractmethod
    def add_animal(self, animal_local: AnimalLocalIn) -> Optional[AnimalLocalOut]:
        pass

    @abstractmethod
    def delete_animal(self, id: int, shelter_id: int) -> bool:
        pass

    @abstractmethod
    def get_all_animals(self) -> list[AnimalLocalOut] :
        pass

    @abstractmethod
    def is_shelter_presented(shelter_id:int) -> bool:
        pass
    def delete_all_animals_by_shelter(self, shelter_id: int):
        pass

class AnimalService(AnimaServicelInterface):
    def __init__(self, animal_controller: AnimalController) -> None:
        super().__init__()
        self._animal_controller = animal_controller
        self._shelter_url = os.getenv('SHELTER_SERVICE_HOST_URL')

    def add_animal(self, animal_local: AnimalLocalIn) -> Optional[AnimalLocalOut]:
        # logger.info(f"Verifying if shelter with shelter_id: {animal_local.shelter_id} exists...")
        # if not self.is_shelter_presented(animal_local.shelter_id):
            # logger.warn(f"Shelter with shelter_id: {animal_local.shelter_id} doesn't exist")
            # raise HTTPException(status_code=404, detail=f"Shelter with shelter_id: {animal_local.shelter_id} doesn't exist")

        logger.info(f"Shelter with shelter_id: {animal_local.shelter_id} exists")
        animal_db = self._animal_controller.create_animal(animal=animal_local)
        logger.info(f"{animal_db=}")
        # return AnimalLocalOut(id=animal_db.id, name=animal_db.name, breed=animal_db.breed, shelter_id=animal_db.shelter_id, description=animal_db.description)
        return AnimalLocalOut(**animal_db.__dict__)

    def get_all_animals(self) -> list[AnimalLocalOut]:
        # Retrieve all animals from the database using the AnimalController
        animals_db = self._animal_controller.get_all_animals()

        # Convert each AnimalDB object to AnimalLocalOut
        animals_local = [
            AnimalLocalOut(**animal_db.__dict__)
            for animal_db in animals_db
        ]

        return animals_local

    def get_animal(self, animal_id: int) -> AnimalLocalOut:
        # Retrieve animal from the database using the AnimalController
        animal_db = self._animal_controller.get_animal(animal_id)

        # Convert AnimalDB object to AnimalLocalOut
        animal_local = AnimalLocalOut(**animal_db.__dict__)

        return animal_local

    def get_animals_by_shelter_id(self, id: int) -> list[AnimalLocalOut]:
        # Retrieve all animals from the database using the AnimalController
        animals_db = self._animal_controller.get_animals_by_shelter_id(shelter_id=id)

        # Convert each AnimalDB object to AnimalLocalOut
        animals_local = [
            AnimalLocalOut(**animal_db.__dict__)
            for animal_db in animals_db
        ]

        return animals_local

    def is_shelter_presented(self, shelter_id: int) -> bool:
        request = f'{self._shelter_url}{shelter_id}'
        logger.info(f"{__name__} : Sending request {request=}")
        r = httpx.get(request)
        logger.info(f"{__name__} : {r.content=}")
        return True if r.status_code == 200 else False

    def delete_animal(self, id: int, shelter_id: int) -> bool:
        logger.info(f"Deleting animal with id: {id} and shelter_id: {shelter_id}")
        animal_db = self._animal_controller.get_animal(id)
        if animal_db is not None and animal_db.shelter_id != shelter_id:
            logger.warn(f"Shelter with shelter_id: {shelter_id} doesn't have an animal with id: {id}")
            raise HTTPException(status_code=403, detail=f"Shelter with shelter_id: {shelter_id} doesn't have a permission to remove animal with id: {id}")
        return self._animal_controller.delete_animal(animal_id=id)

    def delete_all_animals_by_shelter(self, shelter_id: int):
        logger.info(f"Deleting all animals by shelter_id: {shelter_id}")
        return self._animal_controller.delete_all_animals_by_shelter(shelter_id=shelter_id)
