from pydantic import BaseModel
from typing import Optional
import enum


class ShelterLocal(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[str] = None
    description: Optional[str] = None


class ShelterLocalRegistration(BaseModel):
    name: str
    email: str
    password: str

class ShelterLocaAuthorization(BaseModel):
    email: str
    password: str

class ShelterLocalUpdate(ShelterLocal):
    id: int

class ShelterLocalOutput(ShelterLocalUpdate):
    pass


class ShelterErrors(str, enum.Enum):
    SHELTER_NOT_FOUND = "Shelter not found"
    SHELTER_ALREADY_EXISTS = "Shelter already exists"
    INVALID_PASSWORD = "Invalid password"
    INVALID_EMAIL = "Invalid email"
    INVALID_ID = "Invalid id"
    INVALID_NAME = "Invalid name"
    INVALID_ADDRESS = "Invalid address"
    INVALID_PHONE_NUMBER = "Invalid phone number"
    INVALID_DESCRIPTION = "Invalid description"
    INVALID_TYPE = "Invalid type"







