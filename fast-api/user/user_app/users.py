# user_service.py
from fastapi import FastAPI, Depends, HTTPException, APIRouter, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm

from user_app.dependencies.dependencies import get_current_user

from user_app.utilities.utilities import TokenSchema, TokenPayload

from user_app.models.user_local_model import UserLocalAuthorization, UserLocalBase, UserLocalOtput, UserLocalRegistration

import logging  

from user_app.config import config_service




logger = logging.getLogger(__name__)

user_service = config_service()

users_route = APIRouter()

LOGIN_URL = "/login"
PROFILE_URL = "/profile"


@users_route.get("/")
def read_root():
    return {"Hello": "User Service"}

@users_route.get("/exists/{id}")
def get_user_by_id(id: int):
    logger.info(f"Handling request /users/{id}")
    # return False
    return True if user_service.get_user(user_id=id) is not None else False
    # return True if user_service.get_user(user_id=id)

@users_route.post("/signup", response_model=bool)
def register_user(user: UserLocalRegistration):
    logger.info(f"{user=}")

    is_registration_success = user_service.register_user(user=user)

    if not is_registration_success:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return True


@users_route.post(LOGIN_URL, response_model=TokenSchema)
def authorize_user(user: OAuth2PasswordRequestForm = Depends()):
    logger.info(f"Handling {LOGIN_URL}: User from request: {user}")
    return user_service.authorize_user(user=user)

    
@users_route.get(PROFILE_URL, response_model=UserLocalOtput)
def get_user(token_payload: TokenPayload = Depends(get_current_user)):
    logger.info(f"Handling {PROFILE_URL}: {token_payload=}")
    return user_service.get_user(user_id=token_payload.sub)
    
