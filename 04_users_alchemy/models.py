from database import Base
from sqlalchemy import Column, Integer, String

#Entity
class User(Base):
    __tablename__="user"
    id=Column(Integer, primary_key=True) # implizit auto_increment
    name=Column(String(50),nullable=False )
    email=Column(String(50),nullable=False,unique=True )


    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"