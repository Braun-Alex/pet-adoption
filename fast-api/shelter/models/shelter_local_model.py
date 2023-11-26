from pydantic import BaseModel
from typing import Optional


class ShelterLocal(BaseModel):
    email: str
    full_name: str
    address: Optional[str] = None
<<<<<<< HEAD
    phone_number: Optional[str] = None
=======
    number: Optional[str] = None
>>>>>>> 7533c49 (init commit to application service)
    description: Optional[str] = None
    address: Optional[str] = None
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
