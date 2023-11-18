# user_service.py
from fastapi import FastAPI, Depends, HTTPException, APIRouter, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm

from user_app.dependencies.dependencies import get_current_user

from user_app.database import Base, engine, SessionLocal
from user_app.utilities.utilities import TokenSchema, TokenPayload

from sqlalchemy.orm import sessionmaker

from user_app.service.user_service import UserService

from user_app.controllers.user_controller import UserController

from typing import Union

from user_app.models.user_db_model import UserDB
from user_app.models.user_local_model import UserLocalAuthorization, UserLocalBase, UserLocalOtput, UserLocalRegistration

import logging  

from user_app.dependencies.dependencies import LOGIN_URL




logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

users_route = APIRouter()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

user_service = UserService(user_controller=UserController(db=db)) 

@users_route.get("/")
def read_root():
    return {"Hello": "User Service"}

# @users_route.get("/users/{id}")
# def get_user_by_id(id: int):
#     logger.info(f"Handling request /users/{id}")
#     return user_service.get_user(id=id)

@users_route.post("/signup", response_model=bool)
def register_user(user: UserLocalRegistration):
    logger.info(f"{user=}")

    is_registration_success = user_service.register_user(user=user)

    if not is_registration_success:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return True


@users_route.post("/login", response_model=TokenSchema)
def authorize_user(user: OAuth2PasswordRequestForm = Depends()):
    logger.info(f"{user=}")
    return user_service.authorize_user(user=user)

    
@users_route.get('/profile', response_model=UserLocalOtput)
def get_user(token_payload: TokenPayload = Depends(get_current_user)):
    return user_service.get_user(token_payload.sub)
    
