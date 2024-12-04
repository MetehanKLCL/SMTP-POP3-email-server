from connection_database import connect
import traceback

def save_email(sender, receiver, title, subject, message_data, send_date):
    conn = connect()
    if conn:
        try:
            with conn.cursor() as cur:  
                cur.execute("""
                    INSERT INTO mail_info (sender, receiver, title, subject, message_data, send_date)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (sender, receiver, title, subject, message_data, send_date))
                conn.commit()
                print("Email sent and saved to database!!")
        except Exception as e:
            print("Error at saving the email:")
            traceback.print_exc() 
        finally:
            conn.close()
