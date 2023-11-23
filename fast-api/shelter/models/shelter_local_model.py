from pydantic import BaseModel
from typing import Optional


class ShelterLocal(BaseModel):
    email: str
    full_name: str
    address: Optional[str] = None
    phone_number: Optional[str] = None
    description: Optional[str] = None
    status: Optional[int] = None
    address: Optional[str] = None
    number: Optional[str] = None
    description: Optional[str] = None


class ShelterLocalRegistration(BaseModel):
    email: str
    full_name: str
    password: str

class ShelterLocaAuthorization(BaseModel):
    email: str
    password: str

class ShelterLocalOutput(ShelterLocal):
    id: int
