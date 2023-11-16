# user_service.py
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from user_app.database import Base, engine, SessionLocal

from sqlalchemy.orm import sessionmaker

from user_app.service.user_service import UserService

from user_app.controllers.user_controller import UserController

from typing import Union

from user_app.models.user_db_model import UserDB
from user_app.models.user_local_model import UserLocalAuthorization, UserLocalBase, UserLocalOtput, UserLocalRegistration

import logging  

logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

users_route = APIRouter()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

user_service = UserService(user_controller=UserController(db=db)) 

@users_route.get("/")
def read_root():
    return {"Hello": "World"}

@users_route.post("/register", response_model=UserLocalOtput)
def register_user(user: UserLocalRegistration):
    logger.info(f"{user=}")
    return user_service.register_user(user=user)

@users_route.post("/authorize/", response_model=UserLocalOtput)
def authorize_user(user: UserLocalAuthorization):
    logger.info(f"{user=}")
    return user_service.authorize_user(user=user)

@users_route.get("/users/{id}")
def get_user_by_id(id: int):
    logger.info(f"Handling request /users/{id}")
    return user_service.get_user(id=id)
    
