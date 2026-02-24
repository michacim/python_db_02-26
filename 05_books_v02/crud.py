from sqlalchemy.orm import Session
from models import Book


class BookRepository:

    def __init__(self, session: Session):
        self.session = session

    def create_book(self, book: Book) -> Book:
        self.session.add(book)
        self.session.commit()
        self.session.refresh(book)  # Optional: um ID usw. zu aktualisieren
        return book

    def get_book_by_id(self, book_id: int) -> Book | None:
        return self.session.get(Book, id)

    def get_book_by_isbn(self, isbn: str) -> Book | None:
        return self.session.query(Book).filter(Book.isbn == isbn).first()

    def get_all_books(self) -> list[Book]:
        return self.session.query(Book).all()

   

    def delete_book(self, book_id: int) -> Book |None:
        book = self.get_book_by_id(book_id)
        if book:
            self.session.delete(book)
            self.session.commit()
        return book

    def find_books_by_author(self, author: str) -> list[Book]:
        return self.session.query(Book).filter(Book.author.ilike(f"%{author}%")).all()
