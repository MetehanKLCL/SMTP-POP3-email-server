import bcrypt
from connection_database import connect
from validate_password import validate_password

def add_user():
    username = input("Enter Username: ")

    while True:
        password = input("Enter Password: ")
        error_message = validate_password(password)

        if error_message:
            print(f"Invalid password: {error_message}")
            
        else:
            break

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    conn = connect()
    if conn:
        try:
            cur =conn.cursor()
            cur.execute("""
                    INSERT INTO users (username, password)
                    VALUES (%s, %s)
                """, (username, hashed_password))
            conn.commit()
            print("You  registered succesfully!!")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            conn.close()

add_user()


    