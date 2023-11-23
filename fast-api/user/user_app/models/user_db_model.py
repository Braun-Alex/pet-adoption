import json
from sqlalchemy import Column, String, Integer
from user_app.database import Base


class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    password = Column(String)
    salt = Column(String)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "full_name": self.full_name
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return self.to_json()
