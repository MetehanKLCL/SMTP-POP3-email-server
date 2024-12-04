from connection_database import connect
import bcrypt

def authenticate(username, password):
    try:
        conn = connect()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT password FROM users WHERE username = %s", (username,))
            result = cur.fetchone()
            cur.close()

            if result:
                hashed_password = result[0]
                if bcrypt.checkpw(password.encode(), hashed_password.encode()):
                    return True
            return False
    except Exception as e:
        print(f"Authentication error: {e}")
        return False
    finally:
        if conn:
            conn.close()