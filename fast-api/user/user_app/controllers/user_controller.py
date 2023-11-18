import os

from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session
from user_app.models.user_db_model import UserDB
from user_app.models.user_local_model import UserLocalRegistration, UserLocalOtput, UserLocalAuthorization
from user_app.utilities.utilities import hash_data, AES_SECRET_KEY, deterministic_encrypt_data
from uuid import uuid4
import logging

logger = logging.getLogger(__name__)


class UserControllerInterface(ABC):
    @abstractmethod
    def create_user(self, user: UserLocalRegistration) -> bool:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> Optional[UserDB]:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[UserDB]:
        pass

    @abstractmethod
    def update_user(self, user_id: str, user_data: dict) -> Optional[UserDB]:
        pass

    @abstractmethod
    def delete_user(self, user_id: str) -> bool:
        pass


class UserController(UserControllerInterface):
    def __init__(self, db: Session) -> None:
        super().__init__()
        self._db = db

    def create_user(self, user: UserLocalRegistration) -> bool:
        random_salt = os.urandom(32).hex()
        random_id = str(uuid4())
        user_db = UserDB(
                            email=deterministic_encrypt_data(user.email, AES_SECRET_KEY),
                            password=hash_data(user.password + random_salt),
                            salt=random_salt
                        )            
        try:
            self._db.add(user_db)
            self._db.commit()
            self._db.refresh(user_db)
        except Exception as e:
            logger.error(msg:= f"Adding user with {user.email} failed")
            return False
        return True

    def get_user_by_id(self, user_id: int) -> Optional[UserDB]:
        return self._db.query(UserDB).filter(UserDB.id == user_id).first()

    def get_user_by_email(self, email: str) -> Optional[UserDB]:
        deterministically_encrypted_email = deterministic_encrypt_data(email, AES_SECRET_KEY)
        return self._db.query(UserDB).filter(UserDB.email == deterministically_encrypted_email).first()

    def update_user(self, user_id: str, user_data: dict) -> Optional[UserDB]:
        db_user = self.get_user_by_id(user_id)
        if db_user:
            for key, value in user_data.items():
                setattr(db_user, key, value)
            self._db.commit()
            self._db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: str) -> bool:
        db_user = self.get_user_by_id(user_id)
        if db_user:
            self._db.delete(db_user)
            self._db.commit()
            return True
        return False
