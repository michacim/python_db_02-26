import mysql.connector

def connect_db():
    try:
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="db_python02"
        )
        return conn

    except Exception as e:
        print(f"Error {e}")