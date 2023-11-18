from typing import Optional
from user_app.models.user_local_model import UserLocalBase, UserLocalOtput, UserLocalRegistration, UserLocalAuthorization
from user_app.controllers.user_controller import UserController
from user_app.models.user_db_model import UserDB
from fastapi import HTTPException
import logging 

logger = logging.getLogger(__name__)

class UserServiceInterface:
    def register_user(self, user_local:UserLocalRegistration):
        pass

    def authorize_user(self, user_local:UserLocalAuthorization):
        pass

    def get_user(self, ids: list[int]) -> list[UserLocalOtput]:
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
        logger.info(f"User was successfully registered{str(user_db)=}")
        
        return UserLocalOtput(id=user_db.id, email=user_db.email, full_name=user_db.full_name)


    def authorize_user(self, user:UserLocalAuthorization) -> Optional[UserLocalOtput]:
        user_db = self._user_controller.get_user_by_email(user.email)
        logger.info(f"Authorizing user with email: {user.email}. User from db: {user_db=}")
        if not user_db:
            raise HTTPException(400, detail="User does not exist")
        
        if user.password != user_db.password:
            raise HTTPException(400, detail="Password is incorrect")
        
        return UserLocalOtput(id=user_db.id, email=user_db.email, full_name=user_db.full_name)
    
    def get_user(self, id: int) -> list[UserLocalOtput]:
        user_db = self._user_controller.get_user_by_id(id)
        logger.info(f"{user_db=}")
        # for id in ids:  
        if self._user_controller.get_user_by_id(id):
            
            
            return(UserLocalOtput(id=user_db.id, full_name=user_db.full_name, email=user_db.email))
        # return users
        