from pydantic import BaseModel
from typing import Optional


class ShelterLocal(BaseModel):
    email: str
    name: str
    address: Optional[str] = None
    phone_number: str
    description: Optional[str] = None
    status: Optional[int] = None

class ShelterLocalRegistration(BaseModel):
    email: str
    name: str
    password: str

class ShelterLocaAuthorization(BaseModel):
    email: str
    password: str

class ShelterLocalOutput(ShelterLocal):
    id: int
