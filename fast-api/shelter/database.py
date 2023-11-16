from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Replace 'your_username', 'your_password', and 'your_host' with your PostgreSQL credentials
db_username = 'admin'
db_password = 'admin'
db_host = 'localhost'
db_name = 'aboba'  # Change to your desired database name

# Create a PostgreSQL database connection URL
db_url = f'postgresql://{db_username}:{db_password}@{db_host}/{db_name}'

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
