from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


#TODO - verbessern
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/db_python04" # mysql+pymysql://USERNAME:PASSWORD@HOST:PORT/DB-NAME
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session() # Objekt erzeugen
Base = declarative_base() #alle Model(Entity)-Klassen erben von Base
