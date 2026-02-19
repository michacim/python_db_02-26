import mysql.connector

try:
    conn = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="db_python01"
    )

    curser = conn.cursor()
    print("Autocommit aktiv:",conn.autocommit)

    q = '''
        CREATE TABLE IF NOT EXISTS users(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        
        )
    '''
    curser.execute(q)

    ##### insert ############
    insert_query ="INSERT INTO users (name,email) VALUES (%s,%s)"
    curser.execute(insert_query,("Max", "max@web.de"))
    conn.commit()

    ##### lesen /select #####
    curser.execute("SELECT * FROM users")

    for row in curser.fetchall():
        print(row)

    
    curser.close()
    conn.close()

except Exception as e:
    print(f"Error: {e}")

finally:
    pass