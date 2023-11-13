from pydantic import BaseModel
from typing import Optional


class ShelterLocal(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    address: Optional[str] = None
    number: Optional[str] = None
    description: Optional[str] = None
    status: Optional[int] = None
