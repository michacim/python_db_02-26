from models import Book
from crud import BookRepository
from db_connect import connect_db
from db_schema import create_new_books_table
from csv_service import create_books


def main():

    conn = connect_db()
    create_new_books_table(conn)
    repo = BookRepository(conn)
    #########
    book_list= create_books('books.csv')
    repo.save_books(book_list)
    #########
    savedbook = repo.save(Book(title="Kochbuch", author="Maxi",genre="Küche",published_year=2000))

    print("save: ",savedbook)
    
    books = repo.find_all()
    print(books)

    print("Find by Title")
    print(repo.find_by_title('Kochbuch'))
    del_book= repo.delete_by_id(1)
    print(f"Buch gelöscht: {del_book}")

   




if __name__=="__main__":
    main()