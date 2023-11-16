import os

from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine, SessionLocal
from service.shelter_service import ShelterService
from controllers.shelter_controller import ShelterController
from models.shelter_local_model import ShelterLocal
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from dependencies.dependencies import get_current_shelter
from utilities.utilities import TokenSchema, TokenPayload

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # або "*" для дозволу всіх джерел
    allow_credentials=True,
    allow_methods=["*"],  # Дозволяє всі методи
    allow_headers=["*"],  # Дозволяє всі заголовки
)

db = SessionLocal()

shelter_service = ShelterService(shelter_controller=ShelterController(db=db))

Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"Hi from shelter": os.urandom(32).hex()}


@app.post("/shelters/signup", response_model=bool)
def register_user(shelter: ShelterLocal):
    print(f"{shelter=}")
    return shelter_service.register_shelter(shelter=shelter)


@app.post("/shelters/login", response_model=TokenSchema)
def authorize_user(shelter: OAuth2PasswordRequestForm = Depends()):
    print(f"{shelter=}")
    return shelter_service.authorize_shelter(shelter=shelter)


@app.get('/me', response_model=TokenPayload)
def get_me(token_payload=Depends(get_current_shelter)):
    return token_payload
