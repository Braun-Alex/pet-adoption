from datetime import datetime
import jose
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from user_app.utilities.utilities import TokenSchema, TokenPayload, ALGORITHM, JWT_SECRET_KEY, create_custom_access_token
from jose import jwt
from pydantic import ValidationError


import logging

logger = logging.getLogger(__name__)


LOGIN_URL = "/api/v1/users/login"

reusable_oauth = OAuth2PasswordBearer(
    tokenUrl=LOGIN_URL,
    scheme_name="JWT"
)

def get_current_user(token: str = Depends(reusable_oauth)) -> TokenPayload:
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )

        logger.info(f"{payload=}")
        token_data = TokenPayload(**payload)

        naive_exp = token_data.exp.replace(tzinfo=None)
        if token_data.is_shelter or naive_exp < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                headers={"WWW-Authenticate": "Bearer"}
            )
    except (jose.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            headers={"WWW-Authenticate": "Bearer"}
        )

    return token_data

def get_current_user_by_shelter(token: str = Depends(reusable_oauth)) -> bool:
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )

        logger.info(f"{payload=}")
        token_data = TokenPayload(**payload)

        naive_exp = token_data.exp.replace(tzinfo=None)
        if naive_exp < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                headers={"WWW-Authenticate": "Bearer"}
            )
    except (jose.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            headers={"WWW-Authenticate": "Bearer"}
        )

    return True

def refresh_access_token(token: str = Depends(reusable_oauth)) -> TokenSchema:
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )

        logger.info(f"{payload=}")
        token_data = TokenPayload(**payload)

        naive_exp = token_data.exp.replace(tzinfo=None)
        if naive_exp < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                headers={"WWW-Authenticate": "Bearer"}
            )
    except (jose.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            headers={"WWW-Authenticate": "Bearer"}
        )

    return TokenSchema(access_token=create_custom_access_token(subject=token_data.sub, is_shelter=token_data.is_shelter),
                       refresh_token=token)
