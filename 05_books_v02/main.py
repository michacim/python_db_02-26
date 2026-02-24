from database import  session, Base,engine
from models import Book
from crud import BookRepository

def main():
    Base.metadata.drop_all(engine) # Drop table if exists
    Base.metadata.create_all(engine) # Create table if not exists
    # Repository erstellen
    repo = BookRepository(session)

    # --- Testfälle ---

    # 1. Buch anlegen
    new_book = Book(isbn="978-1-23456-789-0", title="Clean Code", author="Robert C. Martin")
    created = repo.create_book(new_book)
    print(f">>> Created: {created}")

    # 2. Buch abrufen
    fetched = repo.get_book_by_isbn("978-1-23456-789-0")
    print(f">>> Fetched by ISBN: {fetched}")


    # # 4. Alle Bücher auflisten
    all_books = repo.get_all_books()
    print(">>> All books:", all_books)

    # # 5. Autorensuche
    author_books = repo.find_books_by_author("martin")
    print(">>> Books by author:", author_books)

    # # 6. Buch löschen
    deleted = repo.delete_book(created.id)
    print(f">>> Deleted: {deleted}")


if __name__=='__main__':
    main()