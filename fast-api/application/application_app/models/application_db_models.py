from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ApplicationDB(Base):
    __tablename__ = 'applications'

    id = Column(Integer, primary_key=True, index=True)
    shelter_id = Column(Integer)
    user_id = Column(Integer)
    animal_id = Column(Integer)
    status = Column(Integer)