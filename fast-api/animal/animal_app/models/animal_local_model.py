from pydantic import BaseModel
from typing import Optional

class AnimalLocalIn(BaseModel):
    name: str
    breed: str
    shelter_id: int
    description: Optional[str] = None

class AnimalLocalOut(AnimalLocalIn):
    id: int

class AnimalLocalUpdate(BaseModel):
    name: Optional[str] = None
    breed: Optional[str] = None
    shelter_id: Optional[int] = None
