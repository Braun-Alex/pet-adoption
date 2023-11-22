from pydantic import BaseModel
from typing import Optional


class ShelterLocal(BaseModel):
    id: Optional[str] = None
    email: str
    name: str
    password: str
    salt: Optional[str] = None
    address: Optional[str] = None
    number: str
    description: Optional[str] = None
    status: Optional[int] = None
