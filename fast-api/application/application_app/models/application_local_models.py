from typing import Optional
from pydantic import BaseModel

from utilities.common import ApplicatioStatus

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

class ApplicationOut(ApplicationIn):
    shelter_id: Optional[int]= None
    user_id :  Optional[int]= None
    animal_id: Optional[int]= None
    #TODO: add status Enum
    status :  Optional[ApplicatioStatus]= None
    id :  Optional[int]= None

class ApplicationUpdate(BaseModel):
    """
        At this moment status:
        1. status=0: application is opened
        2. status=: application is closed
    """
    #TODO: add status Enum
    id: int
    status: ApplicatioStatus
    shelter_id: int
