# models/shelter.py
from sqlalchemy import Column, Integer, String


from database import Base




class ShelterDB(Base):
    __tablename__ = "shelters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    address = Column(String)
    number = Column(String)
    description = Column(String)
    status = Column(Integer)

    def __str__(self):
        return f"Shelter(id={self.id}, name={self.name}, number={self.number})"
