from abc import ABC, abstractmethod
from typing import Optional, Union
from animal_app.models.animal_local_model import AnimalLocalIn
from animal_app.models.animal_db_model import AnimalDB
from sqlalchemy.orm import Session

import logging

logger = logging.getLogger(__name__)


class AnimalControllerInterface(ABC):
    @abstractmethod
    def create_animal(self, animal: AnimalLocalIn) -> Optional[AnimalDB]:
        pass

    @abstractmethod
    def get_animal(self, animal_id: int) -> Optional[AnimalDB]:
        pass

    @abstractmethod
    def get_all_animals(self) -> list[AnimalDB]:
        pass


    @abstractmethod
    def update_animal(self, animal_id: int, updated_data: dict) -> Optional[AnimalDB]:
        pass

    @abstractmethod
    def delete_animal(self, animal_id: int) -> bool:
        pass


class AnimalController(AnimalControllerInterface):
    def __init__(self, db: Session) -> None:
        super().__init__()
        self._db = db

    def create_animal(self, animal: AnimalLocalIn) -> Optional[AnimalDB]:
        # animal_db = AnimalDB(
        #                 name=animal.name,
        #                 breed=animal.breed,
        #                 shelter_id=animal.shelter_id,
        #                 description=animal.description,
        #             )
        animal_db = AnimalDB(**animal.model_dump())
        self._db.add(animal_db)
        self._db.commit()
        self._db.refresh(animal_db)
        return animal_db

    def update_animal(self, animal_id: int, updated_data: dict) -> Optional[AnimalDB]:
        return super().update_animal(animal_id, updated_data)

    def get_animal(self, animal_id: int) -> Optional[AnimalDB]:
        return self._db.query(AnimalDB).filter(AnimalDB.id == animal_id).first()

    def get_all_animals(self) -> list[AnimalDB]:
        return self._db.query(AnimalDB).all()

    def get_animals_by_shelter_id(self, shelter_id: int) -> list[AnimalDB]:
        return self._db.query(AnimalDB).filter(AnimalDB.shelter_id == shelter_id).all()

    def delete_animal(self, animal_id: int) -> bool:
        return super().delete_animal(animal_id)
    
    def delete_all_animals_by_shelter(self, shelter_id: int):
        amount = self._db.query(AnimalDB).filter(AnimalDB.shelter_id == shelter_id).delete()
        self._db.commit()
        logger.info(f"Deleted {amount} animals from shelter with id: {shelter_id}")
