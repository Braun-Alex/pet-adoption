import os

from fastapi.middleware.cors import CORSMiddleware
from user_app.database import Base, engine, SessionLocal
from user_app.service.user_service import UserService
from user_app.controllers.user_controller import UserController
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from user_app.dependencies.dependencies import get_current_user
from user_app.utilities.utilities import TokenSchema

from user_app.models.user_local_model import UserLocalAuthorization, UserLocalBase, UserLocalOtput, UserLocalRegistration

from logging import Logger

logger = Logger("UserRequests")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # або "*" для дозволу всіх джерел
    allow_credentials=True,
    allow_methods=["*"],  # Дозволяє всі методи
    allow_headers=["*"],  # Дозволяє всі заголовки
)

db = SessionLocal()

user_service = UserService(user_controller=UserController(db=db))

Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"Hi from user": os.urandom(32).hex()}


@app.post("/user/signup", response_model=bool)
def register_user(user: UserLocalRegistration):
    logger.info(f"{user=}")

    return user_service.register_user(user=user)


@app.post("/user/login", response_model=TokenSchema)
def authorize_user(user: OAuth2PasswordRequestForm = Depends()):
    logger.info(f"{user=}")
    return user_service.authorize_user(user=user)

    
@app.get('/user/profile', response_model=str)
def get_user(token_payload=Depends(get_current_user)):
    return user_service.get_user(token_payload.sub)
