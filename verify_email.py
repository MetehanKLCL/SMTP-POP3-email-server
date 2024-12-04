from connection_database import connect

def verify(email):
    conn = connect()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM valid_mails WHERE email = %s", (email,))
            result = cursor.fetchall()
            if result:
                print(f"Email: {email} is verified.")
                return True
            else:
                print(f"Email: {email} is not verified.")
                return False
        except Exception as e:
            print("This email is not verificated",e)
            return False
        finally:
            cursor.close()
            conn.close()
    return False