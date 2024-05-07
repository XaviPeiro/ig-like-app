from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

postgres_service_address = os.getenv("POSTGRES_SERVICE_HOST")
postgres_service_port = os.getenv("POSTGRES_SERVICE_PORT")
postgres_db = os.getenv("POSTGRES_DB")
postgres_user = os.getenv("POSTGRES_USER")
postgres_pw = os.getenv("POSTGRES_PASSWORD")
print("----------------------")
print(postgres_service_address)
print("----------------------")

# "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = f'postgresql://{postgres_user}:{postgres_pw}@{postgres_service_address}:{postgres_service_port}/{postgres_db}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
