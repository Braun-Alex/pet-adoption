import json
from sqlalchemy import Column, Integer, String
from database import Base


class ShelterDB(Base):
    __tablename__ = "shelters"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    password = Column(String)
    salt = Column(String)
    address = Column(String, nullable=True)
    number = Column(String, unique=True, index=True, nullable=True)
    description = Column(String, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "address": self.address,
            "number": self.number,
            "description": self.description,
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return self.to_json()
