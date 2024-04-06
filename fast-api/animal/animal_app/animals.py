# user_service.py
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from animal_app.database import Base, engine, get_db, SessionLocal
from animal_app.service.animal_service import AnimalService
from animal_app.controllers.animal_controller import AnimalController
from animal_app.models.animal_local_model import AnimalLocalIn, AnimalLocalOut
from animal_app.dependencies.dependencies import get_current_shelter

from typing import List

from pydantic import BaseModel
from typing import Union

import logging

logger = logging.getLogger(__name__)

animals_router = APIRouter()

db = SessionLocal()

Base.metadata.create_all(bind=engine)

animal_service = AnimalService(AnimalController(db=db))


@animals_router.get("/")
def read_root():
    return {"Hello": "animal"}


@animals_router.post("/add")
def add_animal(animal: AnimalLocalIn):
    logger.info(f"{__name__}: /animals/add handler")
    return animal_service.add_animal(animal_local=animal)


@animals_router.get("/all", response_model=List[AnimalLocalOut])
def get_all_animals():
    return animal_service.get_all_animals()


@animals_router.get("/animal/{id}", response_model=AnimalLocalOut)
def get_animal(id: int):
    return animal_service.get_animal(animal_id=id)


@animals_router.get("/get/", response_model=List[AnimalLocalOut])
def get_animals_by_shelter_id(shelter_id: int):
    return animal_service.get_animals_by_shelter_id(id=shelter_id)

@animals_router.delete("/delete/{id}", response_model=bool)
def delete_animal(id: int, shelter_token = Depends(get_current_shelter)):
    logger.info(f"Handling /delete/{id}: shelter_id: {shelter_token.sub}")

    return animal_service.delete_animal(id=id, shelter_id=int(shelter_token.sub))

@animals_router.delete("/delete_all_by_shelter", response_model=bool)
def delete_all_animals_by_shelter(token = Depends(get_current_shelter)):
    logger.info(f"Handling /delete_all_by_shelter: shelter_id: {token.sub}")
    animal_service.delete_all_animals_by_shelter(shelter_id=token.sub)
    return True
