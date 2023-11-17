import os

from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine, SessionLocal
from service.user_service import UserService
from controllers.user_controller import UserController
from models.user_local_model import UserLocal
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from dependencies.dependencies import get_current_user
from utilities.utilities import TokenSchema

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # або "*" для дозволу всіх джерел
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
def register_user(user: UserLocal):
    return user_service.register_user(user=user)


@app.post("/user/login", response_model=TokenSchema)
def authorize_user(user: OAuth2PasswordRequestForm = Depends()):
    return user_service.authorize_user(user=user)


@app.get('/user/profile', response_model=str)
def get_user(token_payload=Depends(get_current_user)):
    return user_service.get_user(token_payload.sub)
