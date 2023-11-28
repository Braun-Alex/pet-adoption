from typing import Optional
from pydantic import BaseModel

class ApplicationIn(BaseModel):
    """
        At this moment status:
        1. status=0: application is opened
        2. status=: application is closed
    """
    shelter_id: int 
    user_id: int
    animal_id: int 
    #TODO: add status Enum
    status: int

class ApplicationOut(ApplicationIn):
    shelter_id: Optional[int]= None
    user_id :  Optional[int]= None
    animal_id: Optional[int]= None
    #TODO: add status Enum
    status :  Optional[int]= None
    id :  Optional[int]= None

class ApplicationUpdate:
    """
        At this moment status:
        1. status=0: application is opened
        2. status=: application is closed
    """
    #TODO: add status Enum
    id: int
    status: int
