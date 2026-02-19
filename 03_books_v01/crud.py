from models import  Book


class BookRepository:

    def __init__(self,conn):
        self.conn=conn



    def save(self, book:Book)->Book:  #TODO try/Except
        try:
            cursor = self.conn.cursor()
            q =""" 
            INSERT INTO books(title, author, genre, published_year)
            VALUES (%s,%s,%s,%s)
            """
            values  = (book.title, book.author, book.genre, book.published_year)
            cursor.execute(q,values)
            self.conn.commit()
            book.id= cursor.lastrowid
            cursor.close()
            return book

        except Exception as e:
            print(f"Error: {e}")

    def find_all(self)->list[Book]:
        try:
            cursor = self.conn.cursor()

        except Exception as e:
            print(f"Error: {e}")
    def find_by_title(self, title:str)->list[Book]:
        try:
            cursor = self.conn.cursor()

        except Exception as e:
             print(f"Error: {e}")
    def delete_by_id(self,id:int)-> bool:
        try:
            cursor = self.conn.cursor()

        except Exception as e:
             print(f"Error: {e}")