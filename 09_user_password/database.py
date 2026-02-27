from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


#TODO - verbessern
DATABASE_URL = "sqlite:///user.db" 
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session() # Objekt erzeugen
Base = declarative_base() #alle Model(Entity)-Klassen erben von Base
