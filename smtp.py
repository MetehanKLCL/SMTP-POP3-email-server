import socket
from datetime  import datetime
from verify_email import verify
from save_email import save_email


def receive_data(client_socket):
    buffer = ""
    while True:
        data = client_socket.recv(1024).decode()
        buffer += data
        if "\r\n" in buffer:
            break
    return buffer.strip()

def smtp_server(host="192.168.0.18", port=587):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"SMTP Server is Running... {host}:{port}")

    sender = None
    receiver = None
    title = ""
    subject = ""

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection: {client_address}")

    
        client_socket.send(b"220 Welcome to Python SMTP Server\r\n")
        
        while True:
            data = receive_data(client_socket)
            print(f"From Client: {data}")

            if data.startswith("HELO"):
                client_socket.send(b"250 Hello Client\r\n")

            elif data.startswith("MAIL FROM:"):    
                sender = data.split(":")[1].strip()[1:-1]  
                if verify(sender):  
                    client_socket.send(b"250 OK\r\n")
                else:
                    client_socket.send(b"550 No such sender\r\n")

            elif data.startswith("RCPT TO:"):
                receiver  = data.split(":")[1].strip()[1:-1]  
                if verify(receiver):  
                    client_socket.send(b"250 OK\r\n")
                else:
                    client_socket.send(b"550 No email at address\r\n")

            elif data.startswith("DATA"):
                client_socket.send(b"354 Start mail input; end with <CRLF>.<CRLF>\r\n")
                message_data = ""
                while True:
                    line = receive_data(client_socket)
                    if line == ".":
                        break
                    message_data += line + "\r\n"

                    lines = message_data.split("\r\n")
                    for line in lines:
                        if line.startswith("Title:")and not title:
                            title = line.split(":", 1)[1].strip()

                        elif line.startswith("Subject:") and not subject:
                            subject = line.split(":", 1)[1].strip()
                    
                    send_date = datetime.now()
                        
                    save_email(sender, receiver, subject, title, message_data, send_date)

                print(f"E-mail content:\n{message_data}")
                client_socket.send(b"250 OK: Message sent\r\n")
            
            elif data.startswith("QUIT"):
                client_socket.send(b"221 Bye\r\n")
                client_socket.close()
                print("Connection closed.")
                break
            else:
                client_socket.send(b"500 Syntax error, command unrecognized\r\n")

smtp_server()
