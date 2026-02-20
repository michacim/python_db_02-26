import csv
import os
from models import Book
# "id","title","author","genre","published_year"
def create_books(csv_file:str)->list[Book]:
    ''' liest aus books.csv daten und gibt Liste mit Büchern zurück '''
      #Workaround für Umgang mit relativen Pfaden
    script_dir = os.path.dirname(__file__)
    full_path= os.path.join(script_dir,csv_file)

    book_list =[]
    with open(full_path,newline='',encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            book = Book(
                id= row['id'],
                title=row['title'],
                author= row['author'],
                genre= row['genre'],
                published_year= row['published_year']
            )
            book_list.append(book)

    
    return book_list
