# user_service.py
from fastapi import FastAPI, Depends, HTTPException
from database import Base, engine, get_db, SessionLocal

from service.user_service import UserService

from controllers.user_controller import UserController


from pydantic import BaseModel
from typing import Union


from models.user_db_model import UserDB
from models.user_local_model import UserLocal


app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/users/register")
def register_user(user: UserLocal):
    # user_db = user_controller.get_user_by_email(user.email)
    # print (f"{user_db=}")
    # if user_db:
    #     raise HTTPException(400, detail="User already exist")

    # user_db = user_controller.create_user(user)

    # return user
    return user_service.register_user(user=user)

@app.get("/users/authorize/{id}")
def authorize_user(id: int):
    # user_db = user_controller.get_user_by_email(email)
    # print (f"{user_db=}")
    # if not user_db:
    #     raise HTTPException(400, detail="User is not exist")

    # user_local = UserLocal(id=user_db.id, email=user_db.email, full_name=user_db.full_name)
    # return user_local
    return {"ABOBA": id}
    

# @app.post("/users/")  # Укажите UserModel в качестве response_model
# def create_user(user: User):
#     # db_user = user # Создаем объект UserModel
#     print("ABOBA ")
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return {"db_user": user}

if __name__ == "__main__":
    db = SessionLocal()

    user_service = UserService(user_controller=UserController(db=db)) 

