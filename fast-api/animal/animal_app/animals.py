# user_service.py
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from animal_app.database import Base, engine, get_db, SessionLocal
from animal_app.service.animal_service import AnimalService
from animal_app.controllers.animal_controller import AnimalController
from animal_app.models.animal_local_model import AnimalLocalIn

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
    return{"Hello":"animal"}

@animals_router.post("/add")
def add_animal(animal: AnimalLocalIn):
    logger.info(f"{__name__}: /animals/add handler")
    animal_service.add_animal(animal_local=animal)
    return {"aboba": "aboba"}






    
