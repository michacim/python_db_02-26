def create_books_table(conn):

    try:

        cursor =  conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS books")
        q='''
            CREATE TABLE books(
                id int NOT NULL AUTO_INCREMENT,
                title varchar(200) NOT NULL,
                author varchar(100) NOT NULL,
                genre varchar(100),
                published_year int(4),
                PRIMARY KEY (id)
            )
        '''
        cursor.execute(q)
        cursor.close()
    except Exception as e:
        print(f"Error: {e}")
