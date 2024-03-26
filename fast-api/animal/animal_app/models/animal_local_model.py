from pydantic import BaseModel
from typing import Optional

class AnimalLocalIn(BaseModel):
    name:       str
    photo:      str
    type:       str
    sex:        str
    month:      Optional[str] = None
    year:       Optional[str] = None
    shelter_id: int
    description: Optional[str] = None


class AnimalLocalOut(AnimalLocalIn):
    id: int

class AnimalLocalUpdate(BaseModel):
    name:       Optional[str] = None
    type:       Optional[str] = None
    sex:        Optional[str] = None
    month:      Optional[str] = None
    year:       Optional[str] = None
    shelter_id: Optional[int] = None
    description: Optional[str] = None
