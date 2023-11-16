from pydantic import BaseModel
from typing import Optional

#shared properties
class UserLocalBase(BaseModel):
    email: str 
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

 