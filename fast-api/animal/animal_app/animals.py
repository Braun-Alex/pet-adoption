from http.client import HTTPException
import os
import hashlib
from fastapi import APIRouter, File, UploadFile, Form
from animal_app.database import Base, engine, get_db, SessionLocal
from animal_app.service.animal_service import AnimalService
from animal_app.controllers.animal_controller import AnimalController
from animal_app.models.animal_local_model import AnimalLocalIn, AnimalLocalOut, AnimalLocalUpdate
from typing import Optional

from typing import List

import logging

logger = logging.getLogger(__name__)

animals_router = APIRouter()

db = SessionLocal()

Base.metadata.create_all(bind=engine)

animal_service = AnimalService(AnimalController(db=db))


def save_image(image: bytes, name: str, extension: str):
    image_location = f"data/images/{name}{extension}"
    with open(image_location, "wb") as buffer:
        buffer.write(image)
    return image_location


def hash_image(file_content: bytes):
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
    image_extension = os.path.splitext(image.filename)[1]
    save_image(contents, image_name, image_extension)
    animal = AnimalLocalIn(
        name=name,
        photo=f"https://api.takeapet.me/images/{image_name}",
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


@animals_router.put("/animal/{id}")
def update_animal(id: int, updated_data: AnimalLocalUpdate):
    animal = animal_service.get_animal(id)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal not found")
    updated_animal = animal_service.update_animal(id, updated_data)
    return updated_animal


@animals_router.patch("/animal/{id}")
def partial_update_animal(id: int, updated_data: AnimalLocalUpdate):
    animal_db = animal_service.get_animal(id)
    if animal_db:
        # Об'єкт тварини знайдено, тому створюємо об'єкт AnimalLocalOut
        animal_local = AnimalLocalOut(**animal_db.__dict__)
        # Проводимо оновлення об'єкта animal_local за допомогою даних з updated_data
        # Наприклад:
        for field, value in updated_data.dict().items():
            setattr(animal_local, field, value)
        # Повертаємо оновлений об'єкт animal_local
        return animal_local
    else:
        # Якщо тварина не знайдена, повертаємо None або розраховуємо на обробку помилки
        return None




#def partial_update_animal(id: int, updated_data: AnimalLocalUpdate):
   # animal = animal_service.get_animal(id)
   # if not animal:
    #    raise HTTPException(status_code=404, detail="Animal not found")
    #updated_animal = animal_service.partial_update_animal(id, updated_data)
    #return updated_animal
