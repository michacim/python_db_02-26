from models import Book
from crud import BookRepository
from db_connect import connect_db
from db_schema import create_books_table


def main():

    conn = connect_db()
    create_books_table(conn)
    repo = BookRepository(conn)
    savedbook = repo.save(Book(title="Kochbuch", author="Maxi",genre="Küche",published_year=2000))

    print(savedbook)


if __name__=="__main__":
    main()