from enum import Enum
from typing import Optional
from pydantic import BaseModel

# from utilities.common import ApplicationStatus
class ApplicationStatus(Enum):
    REJECTED = 0
    ACCEPTED = 1
    CREATED  = 2
class ApplicationIn(BaseModel):
    """
        At this moment status:
        1. status=2: application is opened`
        2. status=1: application is accepted
        3. status=0: application is rejected
    """
    shelter_id: int
    user_id: int
    animal_id: int
    # TODO: add status Enum

class ApplicationOut(ApplicationIn):
    shelter_id: Optional[int] = None
    user_id:  Optional[int] = None
    animal_id: Optional[int] = None
    # TODO: add status Enum
    status:  Optional[ApplicationStatus] = None
    id:  Optional[int] = None

class ApplicationUpdate(BaseModel):
    """
        At this moment status:
        1. status=2: application is opened
        2. status=1: application is accepted
        3. status=0: application is rejected
    """
    # TODO: add status Enum
    id: int
    status: ApplicationStatus
    shelter_id: int



