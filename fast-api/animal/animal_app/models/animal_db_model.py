from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from animal_app.database import Base

class AnimalDB(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    breed = Column(String)
    shelter_id = Column(Integer)
    description = Column(String, nullable=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def __repr__(self):
        return (
            f"AnimalDB(id={self.id}, name='{self.name}', "
            f"breed='{self.breed}', shelter_id={self.shelter_id}, "
            f"description='{self.description}')"
        )
    

    


