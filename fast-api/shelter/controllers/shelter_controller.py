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

from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session
from models.shelter_db_model import ShelterDB
from models.shelter_local_model import ShelterLocal
from utilities.utilities import hash_data


class ShelterControllerInterface(ABC):
    @abstractmethod
    def create_shelter(self, user: ShelterLocal) -> ShelterDB:
        pass

    @abstractmethod
    def get_shelter_by_id(self, shelter_id: int) -> Optional[ShelterDB]:
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
    def update_shelter(self, shelter_id: int, shelter_data: dict) -> Optional[ShelterDB]:
        pass

    @abstractmethod
    def delete_shelter(self, shelter_id: int) -> bool:
        pass


class ShelterController(ShelterControllerInterface):
    def __init__(self, db: Session) -> None:
        super().__init__()
        self._db = db

    def create_shelter(self, shelter: ShelterLocal) -> ShelterDB:
        random_salt = os.urandom(32).hex()
        shelter_db = ShelterDB(email=shelter.email, name=shelter.name,
                               password=hash_data(shelter.password + random_salt), salt=random_salt)
        self._db.add(shelter_db)
        self._db.commit()
        self._db.refresh(shelter_db)
        return shelter_db

    def get_shelter_by_id(self, shelter_id: int) -> Optional[ShelterDB]:
        return self._db.query(ShelterDB).filter(ShelterDB.id == shelter_id).first()

    def get_shelter_by_name(self, shelter_name: str) -> Optional[ShelterDB]:
        return self._db.query(ShelterDB).filter(ShelterDB.id == shelter_name).first()

    def get_shelter_by_email(self, email: str) -> Optional[ShelterDB]:
        return self._db.query(ShelterDB).filter(ShelterDB.email == email).first()

    def get_all_shelters(self, skip: int = 0, limit: int = 100) -> List[ShelterDB]:
        return self._db.query(ShelterDB).offset(skip).limit(limit).all()

    def update_shelter(self, shelter_id: int, shelter_data: dict) -> Optional[ShelterDB]:
        db_shelter = self.get_shelter_by_id(shelter_id)
        if db_shelter:
            for key, value in shelter_data.items():
                setattr(db_shelter, key, value)
            self._db.commit()
            self._db.refresh(db_shelter)
        return db_shelter

    def delete_shelter(self, shelter_id: int) -> bool:
        db_shelter = self.get_shelter_by_id(shelter_id)
        if db_shelter:
            self._db.delete(db_shelter)
            self._db.commit()
            return True
        return False
