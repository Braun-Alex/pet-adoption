import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine, SessionLocal
from service.shelter_service import ShelterService
from controllers.shelter_controller import ShelterController
from models.shelter_local_model import ShelterLocal

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


@app.post("/shelters/registration")
def register_shelter(shelter: ShelterLocal):
    print(f"{shelter=}")
    return shelter_service.register_shelter(shelter=shelter)


@app.post("/shelters/authorization/")
def authorize_shelter(shelter: ShelterLocal):
    print(f"{shelter=}")
    return shelter_service.authorize_shelter(shelter=shelter)

# @app.post("/users/")  # Укажите UserModel в качестве response_model
# def create_user(user: User):
#     # db_user = user # Создаем объект UserModel
#     print("ABOBA ")
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return {"db_user": user}
