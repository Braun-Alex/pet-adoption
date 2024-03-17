from sqlalchemy import Column, Integer, String

from animal_app.database import Base

class AnimalDB(Base):
    __tablename__ = "animals"

    id =          Column(Integer, primary_key=True, index=True)
    name =        Column(String, index=True)
    photo =       Column(String)
    type =        Column(String)
    sex =         Column(String)
    month =       Column(String, nullable=True)
    year =        Column(String, nullable=True)
    shelter_id =  Column(Integer)
    description = Column(String, nullable=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)





