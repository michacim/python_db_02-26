from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from database import Base

class BaseRepr:
    """ generischhe __repr__Methode
        alle Klassen, die von  BaseRepr erben, bekommen automatisch eine
        def __repr__-Methode
    """
    def __repr__(self):
        fields = ", ".join(
            f"{col.name}={getattr(self, col.name)!r}"
            for col in self.__table__.columns
        )
        return f"<{self.__class__.__name__}({fields})>"
class User(Base, BaseRepr):
    __tablename__="user"
    id=Column(Integer,primary_key=True)
    name=Column(String(50),nullable=False)
    email=Column(String(50),nullable=False)
    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")


class Address(Base,BaseRepr):
    __tablename__="addresses"
    id=Column(Integer,primary_key=True)
    postal_code=Column(String(6),nullable=False)
    city=Column(String(50),nullable=False)
    street=Column(String(150),nullable=False)
    user_id=Column(Integer, ForeignKey("user.id",ondelete="CASCADE"),nullable=False) 
    user=relationship("User",back_populates="addresses")
    