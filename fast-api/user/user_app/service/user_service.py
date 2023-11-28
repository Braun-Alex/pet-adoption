from typing import Optional
from user_app.models.user_local_model import UserLocalBase, UserLocalOtput, UserLocalRegistration, UserLocalAuthorization
from user_app.controllers.user_controller import UserController
from user_app.models.user_db_model import UserDB
from fastapi import status, HTTPException

from user_app.utilities.converter import convert_from_user_db_to_local
# from user_app.utilities.utilities import hash_data


from fastapi.security import OAuth2PasswordRequestForm
from user_app.utilities.utilities import TokenSchema, create_access_token, create_refresh_token


import logging 

logger = logging.getLogger(__name__)

class UserServiceInterface:
    def register_user(self, user_local:UserLocalRegistration) -> bool:
        pass

    def authorize_user(self, user_local:UserLocalAuthorization):
        pass

    def get_user(self, user_id: int) -> list[UserLocalOtput]:
        pass

    def is_user_exists(self, user_id: int) -> bool:
        pass



class UserService(UserServiceInterface):
    def __init__(self, user_controller: UserController):
        self._user_controller = user_controller

    def register_user(self, user:UserLocalRegistration) -> bool:
        logger.info(f"Registrating user with email: {user.email}")
        user_db = self._user_controller.get_user_by_email(user.email)        
        
        if user_db:
            logger.warn(error_msg:=f"User with email: {user.email} already exist")
            raise HTTPException(status.HTTP_409_CONFLICT)

        return self._user_controller.create_user(user)
        

    def authorize_user(self, user: OAuth2PasswordRequestForm) -> Optional[TokenSchema]:
        user_db = self._user_controller.get_user_by_email(user.username)
        logger.info(f"{user.username=} {user.password=}")
        logger.info(f"{__class__.__name__}: {str(user_db)=}")
        logger.info(f"Authorizing user with email: {user.username}. User from db: {user_db=}")
        if not user_db or self._user_controller._hasher.hash_data(user.password, user_db.salt) != user_db.password:
            logger.warn(f"User with {user.username=} failed authorization")
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)
        
        return TokenSchema(access_token=create_access_token(user_db.id), refresh_token= create_refresh_token(user_db.id))
            
     
    def get_user(self, user_id: int) -> UserLocalOtput:
        user_db = self._user_controller.get_user_by_id(user_id)
        logger.info(f"{user_db=}")

        if not user_db:
            logger.info(f"{__name__}: User with id: {user_id} doesn't exist.")
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        
        logger.info(f"{user_db.email= }, {user_db.full_name= }, {user_id=}")

        # return str(user_db)
        # return(UserLocalOtput(id=user_db.id, full_name=user_db.full_name, email=self._user_controller._encrypter.decrypt_data(user_db.email)))
        return convert_from_user_db_to_local(user_db=user_db)

    # def get_user(self, user_id: str) -> str:
    #     user_db = self._user_controller.get_user_by_id(user_id)
    #     if not user_db:
    #         raise HTTPException(status.HTTP_404_NOT_FOUND)
    #     return str(user_db)
