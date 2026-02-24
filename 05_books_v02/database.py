# Standard Configuration
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL="mysql+pymysql://root:@localhost:3306/db_python03"

engine =  create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session() # kapselt Datenbankzugriff -> kein direkter Zugriff auf Datenbank
Base = declarative_base()  # alle Model-Klassen erben von Base (Objekte für die Datenbank)
