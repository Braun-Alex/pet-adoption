# from http.client import HTTPException
from database import Base, engine, SessionLocal
from service.shelter_service import ShelterService
from controllers.shelter_controller import ShelterController
from models.shelter_local_model import ShelterLocal, ShelterLocalOutput, ShelterLocalRegistration, ShelterLocalUpdate
from fastapi import APIRouter, Depends, HTTPException
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
    logger.info(f"Handling /login: {shelter=}")
    return shelter_service.authorize_shelter(shelter=shelter)


@shelter_route.get('/profile', response_model=ShelterLocalOutput)
def get_curent_shelter(token_payload=Depends(get_current_shelter)):
    return shelter_service.get_shelter(token_payload.sub)

@shelter_route.get('/{id}', response_model=ShelterLocalOutput)
def get_shelter(id: int):
    return shelter_service.get_shelter(shelter_id=id)

@shelter_route.put("/{shelter_id}", response_model=bool)
def update_shelter_info(shelter_id: int, new_shelter_info: ShelterLocal):
    logger.info(f"Handling PUT: /shelter/{shelter_id} with {new_shelter_info=}")
    try:
        return shelter_service.update_shelter_info(new_shelter_info=ShelterLocalUpdate(**new_shelter_info.model_dump(), id=shelter_id))

    except RuntimeError as error:
        logger.error(f"RuntimeError: ")
        raise HTTPException(status_code=404, detail=str(error))

