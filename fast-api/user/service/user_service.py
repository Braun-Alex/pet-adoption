from typing import Optional
from models.user_local_model import UserLocal
from controllers.user_controller import UserController
from models.user_db_model import UserDB
from fastapi import HTTPException



class UserServiceInterface:
    def register_user(self, user_local:UserLocal):
        pass

    def authorize_user(self, user_local:UserLocal):
        pass

class UserService(UserServiceInterface):
    def __init__(self, user_controller: UserController):
        self._user_controller = user_controller

    def register_user(self, user:UserLocal) -> UserLocal:
        user_db = self._user_controller.get_user_by_email(user.email)
        print (f"{user_db=}")
        if user_db:
            raise HTTPException(400, detail="User already exist")

        user_db = self._user_controller.create_user(user)
        return UserLocal(id=user_db.id, email=user_db.email, full_name=user_db.full_name)


    def authorize_user(self, user:UserLocal) -> Optional[UserLocal]:
        user_db = self._user_controller.get_user_by_email(user.email)
        print (f"{user_db=}")
        if not user_db:
            raise HTTPException(400, detail="User is not exist")
        
        return UserLocal(id=user_db.id, email=user_db.email, full_name=user_db.full_name)
