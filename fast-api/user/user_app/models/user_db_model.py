import json
from user_app.utilities.utilities import AES_SECRET_KEY, decrypt_data
from sqlalchemy import Column, String, Integer
from user_app.database import Base


class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    password = Column(String)
    salt = Column(String)

    def to_dict(self):
        return {
            "id": self.id,
            "email": decrypt_data(self.email, AES_SECRET_KEY),
            "full_name": decrypt_data(self.full_name, AES_SECRET_KEY)
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return self.to_json()
