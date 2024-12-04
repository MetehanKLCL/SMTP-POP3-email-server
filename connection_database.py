import psycopg as pg

def connect():
    hostname = 'localhost'
    database = 'e-mail'
    username = 'postgres'
    password = 'password'
    port_id = 5432

    try: 
        conn = pg.connect(
            host=hostname,
            dbname=database, 
            user=username,
            password=password,
            port=port_id
        )
        print("Database connection successful!")
        return conn  
    except Exception as err:
        print("An error occurred:", repr(err))
        return None  

connection = connect()
if connection:
    print("Connection object:", connection)
    connection.close()
    print("Connection closed.")
