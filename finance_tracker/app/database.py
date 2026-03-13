from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Datenordner automatisch erstellen
os.makedirs("data", exist_ok=True)

DATABASE_URL = "sqlite:///./data/finance.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


#Aufgabe

#Datenbankverbindung

#Session Factory

#ORM Base