from sqlalchemy import Column, Integer, String
from database import Base  # dein Base = declarative_base()
from sqlalchemy.orm import validates
import re
class Book(Base):
    __tablename__ = "book"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    isbn: str = Column(String(20), nullable=False, unique=True)
    title: str = Column(String(200), nullable=False)
    author: str = Column(String(100), nullable=False)

    def __repr__(self) -> str:
        return f"Book(id={self.id}, isbn='{self.isbn}', title='{self.title}', author='{self.author}')"



