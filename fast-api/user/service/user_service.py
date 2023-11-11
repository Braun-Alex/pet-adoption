from typing import Optional
from models.user_local_model import UserLocalBase, UserLocalOtput, UserLocalRegistration, UserLocalAuthorization
from controllers.user_controller import UserController
from models.user_db_model import UserDB
from fastapi import HTTPException
from logging import Logger

logger = Logger("UserService")

class UserServiceInterface:
    def register_user(self, user_local:UserLocalRegistration):
        pass

    def authorize_user(self, user_local:UserLocalAuthorization):
        pass

class UserService(UserServiceInterface):
    def __init__(self, user_controller: UserController):
        self._user_controller = user_controller

    def register_user(self, user:UserLocalRegistration) -> UserLocalOtput:
        logger.info(f"Registrating user with email: {user.email}")

        user_db = self._user_controller.get_user_by_email(user.email)
        
        if user_db:
            logger.warn(error_msg:=f"User with email: {user.email} already exist")
            raise HTTPException(400, detail=error_msg)

        user_db = self._user_controller.create_user(user)
        logger.debug(f"User was successfully registered{str(user_db)=}")
        
        return UserLocalOtput(id=user_db.id, email=user_db.email, full_name=user_db.full_name)


    def authorize_user(self, user:UserLocalAuthorization) -> Optional[UserLocalOtput]:
        logger.info(f"Authorizing user with email: {user.email}")
        user_db = self._user_controller.get_user_by_email(user.email)
        logger.debug(f"User from db: {user_db=}")
        if not user_db:
            raise HTTPException(400, detail="User does not exist")
        
        if user.password != user_db.password:
            raise HTTPException(400, detail="Password is incorrect")
        
        return UserLocalOtput(id=user_db.id, email=user_db.email, full_name=user_db.full_name)
