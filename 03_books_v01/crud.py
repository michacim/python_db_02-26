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
        cursor = self.conn.cursor(dictionary=True)
        try:
            sql='SELECT * FROM books'
            cursor.execute(sql)
            result= cursor.fetchall()
            return [Book(**row) for row in result]# create Book-List
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
         
    def find_by_title(self, title:str)->list[Book]:
        try:
            cursor = self.conn.cursor(dictionary=True) # Dictionary! Standard: Tupel
            sql ='SELECT * FROM books WHERE TITLE LIKE %s'
            cursor.execute(sql,(f"%{title}%",))
            results = cursor.fetchall()
            return [Book(**row) for row in results] #Liste mit Dictionary wird zu Liste mit Books
        except Exception as e:
             print(f"Error: {e}")
    def delete_by_id(self,id:int)-> bool:
        """ 
        Args:
            id: Primary Key from book
        Return:
            True, wenn erfolgreich gelöscht
        Raise:
           
        """
        try:
            cursor = self.conn.cursor()
            sql = "DELETE FROM books WHERE id = %s"
            cursor.execute(sql,(id,))
            self.conn.commit()
            del_rows = cursor.rowcount 
            cursor.close()
            return del_rows == 1 ## True, wenn genau 1 Datensatz gelöscht
        except Exception as e:
             print(f"Error: {e}")