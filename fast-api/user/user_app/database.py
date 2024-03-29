from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Create a PostgreSQL database connection URL
DATABASE_URI="postgresql://user_db_user:user_db_password@localhost/user_db_dev"

db_url = os.getenv('DATABASE_URI') or DATABASE_URI
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
