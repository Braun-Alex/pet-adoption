import os

from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine, SessionLocal
from service.shelter_service import ShelterService
from controllers.shelter_controller import ShelterController
from models.shelter_local_model import ShelterLocal
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from dependencies.dependencies import get_current_shelter
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

shelter_service = ShelterService(shelter_controller=ShelterController(db=db))

Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"Hi from shelter": os.urandom(32).hex()}


@app.post("/shelter/signup", response_model=bool)
def register_user(shelter: ShelterLocal):
    return shelter_service.register_shelter(shelter=shelter)


@app.post("/shelter/login", response_model=TokenSchema)
def authorize_user(shelter: OAuth2PasswordRequestForm = Depends()):
    return shelter_service.authorize_shelter(shelter=shelter)


@app.get('/shelter/profile', response_model=str)
def get_shelter(token_payload=Depends(get_current_shelter)):
    return shelter_service.get_shelter(token_payload.sub)
