# user_service.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine, get_db, SessionLocal

from service.user_service import UserService

from controllers.user_controller import UserController


from pydantic import BaseModel
from typing import Union

from models.user_db_model import UserDB
from models.user_local_model import UserLocalAuthorization, UserLocalBase, UserLocalOtput, UserLocalRegistration

from logging import Logger

logger = Logger("UserRequests")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # або "*" для дозволу всіх джерел
    allow_credentials=True,
    allow_methods=["*"],  # Дозволяє всі методи
    allow_headers=["*"],  # Дозволяє всі заголовки
)

db = SessionLocal()

user_service = UserService(user_controller=UserController(db=db)) 


Base.metadata.create_all(bind=engine)



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/users/register", response_model=UserLocalOtput)
def register_user(user: UserLocalRegistration):
    logger.info(f"{user=}")
    return user_service.register_user(user=user)

@app.post("/users/authorize/", response_model=UserLocalOtput)
def authorize_user(user: UserLocalAuthorization):
    # user_db = user_controller.get_user_by_email(email)
    # print (f"{user_db=}")
    # if not user_db:
    #     raise HTTPException(400, detail="User is not exist")

    # user_local = UserLocal(id=user_db.id, email=user_db.email, full_name=user_db.full_name)
    # return user_local
    logger.info(f"{user=}")
    return user_service.authorize_user(user=user)
    

# @app.post("/users/")  # Укажите UserModel в качестве response_model
# def create_user(user: User):
#     # db_user = user # Создаем объект UserModel
#     print("ABOBA ")
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return {"db_user": user}

    
