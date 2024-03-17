import shutil
import hashlib
from fastapi import APIRouter, File, UploadFile, Form
from animal_app.database import Base, engine, get_db, SessionLocal
from animal_app.service.animal_service import AnimalService
from animal_app.controllers.animal_controller import AnimalController
from animal_app.models.animal_local_model import AnimalLocalIn, AnimalLocalOut
from typing import Optional

from typing import List

import logging

logger = logging.getLogger(__name__)

animals_router = APIRouter()

db = SessionLocal()

Base.metadata.create_all(bind=engine)

animal_service = AnimalService(AnimalController(db=db))


def save_image(file: UploadFile, name: str):
    image_location = f"/usr/share/nginx/html/images/{name}"
    with open(image_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return image_location


def hash_image(file_content: bytes) -> str:
    return hashlib.sha256(file_content).hexdigest()


@animals_router.get("/")
def read_root():
    return {"Hello": "animal"}


@animals_router.post("/add")
async def add_animal(
    name: str = Form(...),
    type: str = Form(...),
    sex: str = Form(...),
    month: Optional[str] = Form(None),
    year: Optional[str] = Form(None),
    shelter_id: int = Form(...),
    description: Optional[str] = Form(None),
    image: UploadFile = File(...)
):
    contents = await image.read()
    image_name = hash_image(contents)
    save_image(image, image_name)
    animal = AnimalLocalIn(
        name=name,
        photo=f"/usr/share/nginx/html/images/{image_name}",
        type=type,
        sex=sex,
        month=month,
        year=year,
        shelter_id=shelter_id,
        description=description
    )
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
