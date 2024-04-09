from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timedelta


#shared properties
class UserLocalBase(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    photo: Optional[str] = ""
    description: Optional[str] = ""


class UserLocalOutput(UserLocalBase):
    id: int


# Properties to receive via API on creation
class UserLocalRegistration(BaseModel):
    email: str
    name: str
    password: str

# Properties to receive via API on authorization
class UserLocalAuthorization(BaseModel):
    email: str
    password: str

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    sub: str = None
    exp: datetime = None
    is_shelter: bool = None
