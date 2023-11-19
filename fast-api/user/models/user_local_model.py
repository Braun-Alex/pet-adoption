from pydantic import BaseModel
from typing import Optional

#shared properties
class UserLocalBase(BaseModel):
    email: str 
    full_name: Optional[str] = None
    photo: Optional[str] = None
    description: Optional[str] = None

# Properties to receive via API on creation 
class UserLocalRegistration(UserLocalBase):
    full_name: str
    password: str

# Properties to receive via API on authorization
class UserLocalAuthorization(UserLocalBase):
    password: str
    
class UserLocalOtput(UserLocalBase):
    id: int

 