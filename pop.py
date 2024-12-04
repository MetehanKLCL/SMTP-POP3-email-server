import socket
from authentication import authenticate
from fetch_emails import fetch_emails

def pop3_server():
    host = "192.168.0.18"
    port = 110

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"POP3 working on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection: {client_address}")
        client_socket.send(b"OK POP3 Server is Ready\r\n")

        authenticated = False
        username = None

        while True:
            try:
                data = client_socket.recv(1024).decode()
                data = data.strip()
                print(f"{data} is coming")

                if not data:
                    client_socket.send(b"-ERR Empty command received\r\n")
                    continue

                if data.startswith("USER"):
                    try:
                        username = data.split(" ")[1]
                        print(f"Username received: {username}")
                        client_socket.send(b"OK User Accepted\r\n")
                    except IndexError:
                        client_socket.send(b"-ERR Invalid USER command \r\n")
                    
                elif data.startswith("PASS"):
                    if username:
                        print(f"Authenticating for user: {username}")
                        client_socket.send(b"OK Password Accepted\r\n")
                        authenticated = authenticate(username)
                        if authenticated:
                            client_socket.send(b"+OK Authentication successful\r\n")
                        else:
                            client_socket.send(b"-ERR Please provide USER before PASS\r\n")

                elif data.startswith("STAT"):
                    if authenticated:
                        emails = fetch_emails()
                        total_size = sum(len(email[5]) for email in emails)
                        client_socket.send(f"+OK {len(emails)} {total_size}\r\n".encode())
                    else:
                        client_socket.send(b"-ERR Authenticate first\r\n")

                elif data.startswith("LIST"):
                    if authenticated:
                        emails = fetch_emails()
                        response = f"+OK {len(emails)} messages\r\n"
                        for email in emails:
                            response += f"{email[0]} {len(email[5])}\r\n"
                        response += ".\r\n"
                        client_socket.send(response.encode())
                    else:
                        client_socket.send(b"-ERR Authenticate first\r\n")

                elif data.startswith("RETR"):
                    if authenticated:
                        emails = fetch_emails()
                        try:
                            msg_number = int(data.split(" ")[1]) - 1
                            if 0 < msg_number < len(emails):
                                email = emails[msg_number]
                                response = f"+OK {len(email[5])} octets\r\n{email[5]}\r\n.\r\n"
                                client_socket.send(response.encode())
                            else:
                                client_socket.send(b"-ERR No such message\r\n")
                        except (IndexError, ValueError):
                            client_socket.send(b"-ERR Invalid message number\r\n")
                    else:
                        client_socket.send(b"-ERR Authenticate first\r\n")

                elif data.startswith("QUIT"):
                    client_socket.send(b"OK Goodbye")
                    client_socket.close()
                    print("Connection is closed!!!")
                    break

                else:
                    client_socket.send(b"-ERR Invalid C ommand \r\n")

            except Exception as e:
                print(f"Error: {e}")
                client_socket.send(b"-ERR Internal Server Error\r\n")
                break

pop3_server()

