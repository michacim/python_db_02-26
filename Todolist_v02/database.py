from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


#FIXME - verbessern: Session per MEthode laden
# DATABASE_URL = "mysql+pymysql://root:@localhost:3306/db_python04" # mysql+pymysql://USERNAME:PASSWORD@HOST:PORT/DB-NAME

DATABASE_URL ="sqlite:///todo.db"
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session() # Objekt erzeugen
Base = declarative_base() #alle Model(Entity)-Klassen erben von Base
