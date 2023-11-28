from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

import logging

logger = logging.getLogger(__name__)
# Create a PostgreSQL database connection URL
DATABASE_URI="postgresql://user_db_user:user_db_password@localhost/user_db_dev"
DATABASE_URI="postgresql://application_db_user:application_db_password@localhost:/applicationdb_dev"
db_url = os.getenv('DATABASE_URI') 

logger.info(f"{db_url=}")

#engine_local = create_engine(DATABASE_URI)
#SessionLocalLL =
# db_url = f'postgresql://{db_username}:{db_password}@{db_host}/{db_name}'

#print(f"Trying to create connection with DB. {db_url=}")

# Create an SQLAlchemy engine
engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a declarative base
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
