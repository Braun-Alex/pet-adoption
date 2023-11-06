# models/user.py
from sqlalchemy import Column, Integer, String


from database import Base




class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    password = Column(String)

    def __str__(self):
        return f"User(id={self.id}, email={self.email}, full_name={self.full_name})"


