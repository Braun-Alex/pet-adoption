from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timedelta


#shared properties
class UserLocalBase(BaseModel):
    email: Optional[str] = None
    full_name: Optional[str] = None
    photo: Optional[str] = None
    description: Optional[str] = None
 
class UserLocalOtput(UserLocalBase):
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

 
