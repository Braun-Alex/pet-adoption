from datetime import datetime
import os
import jose
from pydantic import BaseModel
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError

JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']
ALGORITHM = "HS256"

schema_valid = OAuth2PasswordBearer(
    tokenUrl=os.environ['SHELTER_SERVICE_HOST_URL']+"login",
    scheme_name="JWT"
)

class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None
    is_shelter: bool = None

def get_current_shelter(token:str = Depends(schema_valid)) -> TokenPayload:
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        if not token_data.is_shelter or datetime.fromtimestamp(token_data.exp) < datetime.now():
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
