from controllers.user_controller import UserController
from models.user_local_model import UserLocal
from utilities.utilities import hash_data
from fastapi import status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from utilities.utilities import TokenSchema, create_access_token, create_refresh_token


class UserServiceInterface:
    def register_user(self, success: bool):
        pass

    def authorize_user(self, tokens: TokenSchema):
        pass


class UserService(UserServiceInterface):
    def __init__(self, user_controller: UserController):
        self._user_controller = user_controller

    def register_user(self, user: UserLocal) -> bool:
        user_db = self._user_controller.get_user_by_email(user.email)

        if user_db:
            raise HTTPException(status.HTTP_409_CONFLICT)

        return self._user_controller.create_user(user)

    def authorize_user(self, user: OAuth2PasswordRequestForm) -> TokenSchema:
        user_db = self._user_controller.get_user_by_email(user.username)
        print(f"{user_db=}")
        if not user_db or hash_data(user.password + user_db.salt) != user_db.password:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        return {
            "access_token": create_access_token(user_db),
            "refresh_token": create_refresh_token(user_db),
        }
