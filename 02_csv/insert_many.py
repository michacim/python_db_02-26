from db_connect  import  connect_db
from csv_reader import load_csv
try:
    conn =connect_db()
    cursor= conn.cursor()
    # daten = [
    #     ("Arno","arno@web.de"),
    #     ("Ina","ina@web.de"),
    #     ("Otto Krause","kr@gmail.com")
    # ]

    daten = load_csv("users.csv")

    sql ="INSERT INTO users (name,email) VALUES (%s,%s)"
    cursor.executemany(sql,daten)
    conn.commit()


except Exception as e:
    print(e)