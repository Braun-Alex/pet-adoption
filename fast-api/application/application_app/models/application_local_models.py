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
    id: int

class ApplicationUpdate:
    """
        At this moment status:
        1. status=0: application is opened
        2. status=: application is closed
    """
    #TODO: add status Enum
    id: int
    status: int
