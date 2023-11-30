from sqlalchemy import Column, Integer, Enum as EnumType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from utilities.common import ApplicatioStatus

from application_app.db.database import Base


class ApplicationDB(Base):
    __tablename__ = 'applications'

    id = Column(Integer, primary_key=True, index=True)
    shelter_id = Column(Integer)
    user_id = Column(Integer)
    animal_id = Column(Integer)
    status = Column(EnumType(ApplicatioStatus), default=ApplicatioStatus.CREATED)
