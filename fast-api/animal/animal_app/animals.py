# user_service.py
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from animal_app.database import Base, engine, get_db, SessionLocal
from animal_app.service.animal_service import AnimalService
from animal_app.controllers.animal_controller import AnimalController
from animal_app.models.animal_local_model import AnimalLocalIn, AnimalLocalOut

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
def get_animal(animal_id: int):
    return animal_service.get_animal(animal_id=animal_id)


@animals_router.get("/get/", response_model=List[AnimalLocalOut])
def get_animals_by_shelter_id(shelter_id: int):
    return animal_service.get_animals_by_shelter_id(id=shelter_id)
