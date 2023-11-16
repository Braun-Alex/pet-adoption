import hashlib
from jose import jwt
from enum import Enum
import os
from datetime import datetime, timedelta
from typing import Union, Any
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

ALGORITHM = "HS256"  # HMAC-SHA256
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']  # should be kept secret


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None


class JWTTokenTypeExpiration(Enum):
    ACCESS_TOKEN_EXPIRATION = 15  # 15 minutes
    REFRESH_TOKEN_EXPIRATION = 60 * 24 * 7  # 7 days


def hash_data(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()


def create_jwt_token(subject: Union[str, Any], expires_delta: timedelta = None,
                     jwt_token_type_expiration: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = (datetime.utcnow() +
                         timedelta(minutes=jwt_token_type_expiration))

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    return create_jwt_token(subject, expires_delta,
                            JWTTokenTypeExpiration.ACCESS_TOKEN_EXPIRATION.value)


def create_refresh_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    return create_jwt_token(subject, expires_delta,
                            JWTTokenTypeExpiration.REFRESH_TOKEN_EXPIRATION.value)
