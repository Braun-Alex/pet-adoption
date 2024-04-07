import enum
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timedelta


#shared properties
class UserLocalBase(BaseModel):
    email: Optional[str] = None
    full_name: Optional[str] = None
    photo: Optional[str] = ""
    description: Optional[str] = "" 

 
class UserLocalOutput(UserLocalBase):
    id: int

class UserLocalUpdate(UserLocalBase):
    id: int


# Properties to receive via API on creation 
class UserLocalRegistration(BaseModel):
    email: str 
    full_name: str
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

class UserErrors(str, enum.Enum):
    USER_NOT_FOUND = "User not found"
    USER_ALREADY_EXISTS = "User already exists"
    INVALID_PASSWORD = "Invalid password"
    INVALID_EMAIL = "Invalid email"
    INVALID_ID = "Invalid id"
    INVALID_FULL_NAME = "Invalid name"
    INVALID_DESCRIPTION = "Invalid description"
