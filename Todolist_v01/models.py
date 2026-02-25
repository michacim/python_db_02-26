from sqlalchemy import Column, Integer, String, Text, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship

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
# N   
class Todo(Base, BaseRepr):
    __tablename__ ="todos"
    id= Column(Integer, primary_key=True)
    task=Column(String(100))
    description=Column(Text(500))
    deadline=Column(Date)
    state=Column(Enum("OPEN","IN_PROGRESS","DONE"),nullable=False,default="OPEN")
    user_id=Column(Integer, ForeignKey("user.id"),nullable=False)
    user = relationship("User",back_populates="todos")

class User(Base,BaseRepr):
    __tablename__ ="user"
    id= Column(Integer, primary_key=True)
    username=Column(String(50),nullable=False)
    password=Column(String(100),nullable=False)
    todos= relationship("Todo",back_populates="user")#List[Todo]




