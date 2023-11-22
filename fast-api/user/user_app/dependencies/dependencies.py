from datetime import datetime
import jose
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from user_app.utilities.utilities import TokenPayload, ALGORITHM, JWT_SECRET_KEY
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

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
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
