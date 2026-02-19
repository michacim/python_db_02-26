import mysql.connector

def connect():
    try:
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="db_python01"
        )
        return conn
    except Exception as e:
        print(f"Error: {e}")

def create_table(conn):
  q= """
    CREATE TABLE IF NOT EXISTS todo (
    id          INT UNSIGNED NOT NULL AUTO_INCREMENT,
    task        VARCHAR(255) NOT NULL,
    description TEXT NULL,
    deadline    DATE NULL,
    done        BOOLEAN NOT NULL,
    PRIMARY KEY (id)
) """
  conn.cursor().execute(q)

def save(conn,task, description, deadline, done):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO todo (task, description, deadline, done) VALUES (%s, %s, %s, %s)"
        val = (task, description, deadline, done)
        cursor.execute(sql, val)
        conn.commit()
        print("Task erfolgreich gespeichert.")
    except Exception as e:
        print(f"Error: {e}")
def find_all(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM todo")
        return cursor.fetchall()
    except Exception as e:
        print(f"Error: {e}")

def find_by_task(conn,task):
    try:
        cursor = conn.cursor()
        sql = "SELECT * FROM todo WHERE task LIKE %s"
        cursor.execute(sql, (f"%{task}%",))
        return cursor.fetchall()
    except Exception as e:
        print(f"Error: {e}")
def main():
    conn  = connect()
    create_table(conn)
    #save(conn,"einkaufen","Brot und Milch","2026-02-19",False)
    print(find_all(conn))
    #print("find_by_task")
    print(find_by_task(conn,"kauf"))
   

if __name__ == "__main__":
    main()