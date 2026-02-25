from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, validates
from database import Base
import re

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


class Book(Base, BaseRepr):
    __tablename__ = "book"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    isbn: str = Column(String(20), nullable=False, unique=True)
    title: str = Column(String(200), nullable=False)

    # FK statt author-String
    # CASCADE, SET NULL, SET DEFAULT, RESTRICT, NO ACTION
    author_id: int = Column(Integer, ForeignKey("author.id", ondelete="CASCADE"), nullable=False) # TODO: RESTRICT statt CASCADE
    author = relationship("Author", back_populates="books") #lazy ="select" (default)| "joined"

    @validates("isbn")
    def validate_isbn(self, key, value: str) -> str:
        # Beispiel: nur Ziffern und Bindestriche, min 10 max 20 Zeichen
        if not re.fullmatch(r"[0-9-]{10,20}", value or ""):
            raise ValueError("Invalid ISBN format")
        return value
    
class Author(Base,BaseRepr):
    __tablename__ = "author"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(100), nullable=False, unique=True)

    # optional: backref auf Bücher
    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")