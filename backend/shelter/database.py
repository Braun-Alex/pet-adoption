from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os


import logging

logger = logging.getLogger(__name__)
# Replace 'your_username', 'your_password', and 'your_host' with your PostgreSQL credentials
db_username = 'admin'
# db_password = 'admin'
# db_host = 'user_db'
# db_name = 'mydb'  # Change to your desired database name

# Create a PostgreSQL database connection URL
DATABASE_URI="postgresql://shelter_db_user:shelter_db_password@localhost/shelter_db_dev"

db_url = os.getenv('DATABASE_URI') 
logger.info(f"env variable {os.getenv('DATABASE_URI')=}")

logger.info(f"DATABASE URL: {db_url}")
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
