from database import Base, engine, SessionLocal
from service.shelter_service import ShelterService
from controllers.shelter_controller import ShelterController
from models.shelter_local_model import ShelterLocal, ShelterLocalRegistration
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from dependencies.dependencies import get_current_shelter
from utilities.utilities import TokenSchema

import os


db = SessionLocal()

shelter_service = ShelterService(shelter_controller=ShelterController(db=db))

Base.metadata.create_all(bind=engine)


shelter_route = APIRouter()


@shelter_route.get("/")
def read_root():
    return {"Hi from shelter": os.urandom(32).hex()}


@shelter_route.post("/signup", response_model=bool)
def register_user(shelter: ShelterLocalRegistration):
    return shelter_service.register_shelter(shelter=shelter)


@shelter_route.post("/login", response_model=TokenSchema)
def authorize_user(shelter: OAuth2PasswordRequestForm = Depends()):
    return shelter_service.authorize_shelter(shelter=shelter)


@shelter_route.get('/profile', response_model=str)
def get_shelter(token_payload=Depends(get_current_shelter)):
    return shelter_service.get_shelter(token_payload.sub)

@shelter_route.get('/{id}', response_model=bool)
def is_shelter_exist(id: int):
    if shelter_service.get_shelter(shelter_id=id):
        return True