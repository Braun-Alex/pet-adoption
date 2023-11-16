import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine, SessionLocal
from service.user_service import UserService
from controllers.user_controller import UserController
from models.user_local_model import UserLocal

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


@app.post("/users/registration")
def register_user(user: UserLocal):
    print(f"{user=}")
    return user_service.register_user(user=user)


@app.post("/users/authorization")
def authorize_user(user: UserLocal):
    print(f"{user=}")
    return user_service.authorize_user(user=user)
