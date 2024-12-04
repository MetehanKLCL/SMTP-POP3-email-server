from connection_database import connect

def fetch_emails():
    try:
        conn = connect()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM mail_info")
            emails = cur.fetchall()  
            cur.close()
            return emails
        
        
    except Exception as e:

        print(f"Error fetching emails: {e}")
        return []
    
    finally:
        if conn:
            conn.close()

    