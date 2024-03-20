# session = SessionLocal()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# def create_user(user: UserLocal) -> UserDB:
#     db = get_db()
#     #db = SessionLocal()
#     db_item = ShelterDB(**shelter.model_dump())
#     db.add(db_item)
#     db.commit()
#     return db_item

import os

import logging

from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session
from models.shelter_db_model import ShelterDB
from models.shelter_local_model import ShelterLocal, ShelterLocalRegistration, ShelterLocalOutput, ShelterLocalUpdate, ShelterErrors

from utilities.utilities import hash_data
from utilities.converter import convert_from_shelter_db_to_local
from uuid import uuid4

logger = logging.getLogger(__name__)


class ShelterControllerInterface(ABC):
    @abstractmethod
    def create_shelter(self, shelter: ShelterLocal) -> bool:
        pass

    @abstractmethod
    def get_shelter_by_id(self, shelter_id: str) -> Optional[ShelterDB]:
        pass

    @abstractmethod
    def get_shelter_by_name(self, shelter_name: str) -> Optional[ShelterDB]:
        pass

    @abstractmethod
    def get_shelter_by_email(self, email: str) -> Optional[ShelterDB]:
        pass

    @abstractmethod
    def get_all_shelters(self, skip: int = 0, limit: int = 100) -> List[ShelterDB]:
        pass

    @abstractmethod
    def update_shelter_info(self, shelter_id: str, shelter_data: dict) -> bool:
        pass

    @abstractmethod
    def delete_shelter(self, shelter_id: str) -> bool:
        pass


class ShelterController(ShelterControllerInterface):
    def __init__(self, db: Session) -> None:
        super().__init__()
        self._db = db

    def create_shelter(self, shelter: ShelterLocalRegistration) -> bool:
        random_salt = os.urandom(32).hex()
        random_id = str(uuid4())
        user_db = ShelterDB(
                                email=shelter.email,
                                name=shelter.name,
                                password=shelter.password,
                                # password=hash_data(shelter.password + random_salt),
                                salt=random_salt
                            )
        self._db.add(user_db)
        self._db.commit()
        self._db.refresh(user_db)
        return True
    
    def _get_shelter_by_id(self, shelter_id: int) -> Optional[ShelterDB]:
        return self._db.query(ShelterDB).filter(ShelterDB.id == shelter_id).first()

    def get_shelter_by_id(self, shelter_id: int) -> Optional[ShelterLocalOutput]:
        shelter_bd = self._get_shelter_by_id(shelter_id)
        return convert_from_shelter_db_to_local(shelter_db=shelter_bd)

    def get_shelter_by_name(self, shelter_name: str) -> Optional[ShelterDB]:
        return self._db.query(ShelterDB).filter(ShelterDB.name == shelter_name).first()

    def get_shelter_by_email(self, email: str) -> Optional[ShelterDB]:
        return self._db.query(ShelterDB).filter(ShelterDB.email == email).first()

    def get_all_shelters(self, skip: int = 0, limit: int = 100) -> List[ShelterDB]:
        return self._db.query(ShelterDB).offset(skip).limit(limit).all()

    def update_shelter_info(self, shelter_data: ShelterLocalUpdate) -> bool:
        logger.info(f"Updating shelter with id: {shelter_data.id}")
        db_shelter = self._get_shelter_by_id(shelter_id=shelter_data.id)
        logger.debug(f"{str(db_shelter)=}")
        if not db_shelter:
            raise(RuntimeError(ShelterErrors.SHELTER_NOT_FOUND.name))
        for key, value in shelter_data.model_dump().items():
            logger.debug(f"Changing {key} --> {value} ")
            if value is not None:
                logger.info(f"Setting {key} to {value}")
                setattr(db_shelter, key, value)
        self._db.commit()
        logger.debug(f"{str(db_shelter)=} after updating")
        self._db.refresh(db_shelter)
        return True
    

    # def update_shelter_info(self, shelter_id: str, new_shelter: dict) -> Optional[ShelterDB]:
    #     return self.update_shelter(shelter_id, new_shelter) #проксі до update_shelter
    

    def delete_shelter(self, shelter_id: str) -> bool:
        db_shelter = self.get_shelter_by_id(shelter_id)
        if db_shelter:
            self._db.delete(db_shelter)
            self._db.commit()
            return True
        return False
