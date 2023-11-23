from database import Base, engine, SessionLocal
from service.shelter_service import ShelterService
from controllers.shelter_controller import ShelterController
from models.shelter_local_model import ShelterLocal, ShelterLocalOutput, ShelterLocalRegistration
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from dependencies.dependencies import get_current_shelter
from utilities.utilities import TokenSchema

import logging

import os

logger = logging.getLogger(__name__)

db = SessionLocal()

shelter_service = ShelterService(shelter_controller=ShelterController(db=db))

Base.metadata.create_all(bind=engine)


shelter_route = APIRouter()

SIGNUP_URL = "/signup"

@shelter_route.get("/")
def read_root():
    return {"Hi from shelter": os.urandom(32).hex()}


@shelter_route.post(SIGNUP_URL, response_model=bool)
def register_user(shelter: ShelterLocalRegistration):
    logger.info(f"Handling {SIGNUP_URL}: {shelter=}")
    return shelter_service.register_shelter(shelter=shelter)


@shelter_route.post("/login", response_model=TokenSchema)
def authorize_user(shelter: OAuth2PasswordRequestForm = Depends()):
    return shelter_service.authorize_shelter(shelter=shelter)


@shelter_route.get('/profile', response_model=str)
def get_curent_shelter(token_payload=Depends(get_current_shelter)):
    return shelter_service.get_shelter(token_payload.sub)

@shelter_route.get('/{id}', response_model=ShelterLocalOutput)
def get_shelter(id: int):
    shelter_service.get_shelter(shelter_id=id)