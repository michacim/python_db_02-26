from database import Base
from sqlalchemy import Column, Integer, String


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
    name=Column(String(100), nullable=False)
    email=Column(String(100), nullable=False, unique=True)