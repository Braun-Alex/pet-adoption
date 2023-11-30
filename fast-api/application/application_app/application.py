# application.py
from typing import List
from fastapi import FastAPI, Depends, HTTPException, APIRouter, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm

from fastapi import FastAPI, Depends, HTTPException, APIRouter, status as FastApiStatus

from application_app.service.application_service import ApplicationService
from application_app.controllers.application_controller import ApplicationController

from application_app.models.application_local_models import ApplicationIn, ApplicationOut, ApplicationUpdate

from application_app.db.database import Base, engine, SessionLocal

import logging  

logger = logging.getLogger(__name__)

UPDATE_STATUS_URI = "/update_status"

db = SessionLocal()

Base.metadata.create_all(bind=engine)

logger.info(f"Creating instance of application_service!!!!!!")
application_service = ApplicationService(controller=ApplicationController(db=db))

application_router = APIRouter()

CREATE_APPLICATION_URL = "/create"


@application_router.get("/")
def read_root():
    return {"Hello": "Application Service"}

@application_router.post(CREATE_APPLICATION_URL, response_model=bool)
def create_application(application: ApplicationIn):
    logger.info(f"Handling {CREATE_APPLICATION_URL}: {application=}")
    return application_service.add_application(application_in=application)

@application_router.get("/get/", response_model=List[ApplicationOut])
def get_application(shelter_id: int):
    logger.info(f"Handling get request {shelter_id=}")
    applications = application_service.get_application_by_shelter_id(shelter_id=shelter_id) 
    logger.info(f"Get applications from DB: {applications}")
    return applications if applications else [ApplicationOut]

@application_router.post(UPDATE_STATUS_URI)
def update_status(application_update: ApplicationUpdate):
    logger.info(f"Handling {UPDATE_STATUS_URI}: {application_update=}")
    a = application_service.update_application(application_update=application_update)
    if a == None:
        HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
