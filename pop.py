import socket

def pop3_server():
    host = "127.0.0.1"
    port = 110

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"POP3 working on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection: {client_address}")


        client_socket.send(b"OK POP3 Server is Ready\r\n")
        data = client_socket.recv(1024).decode()
        print(f"{data} is coming")

        if data.startswith("USER"):
            client_socket.send(b"OK User Accepted\r\n")

        elif data.startswith("PASS"):
            client_socket.send(b"OK Password Accepted\r\n")

        elif data.startswith("STAT"):
            client_socket.send(b"OK 1 100 \r\n")

        elif data.startswith("RETR"):
            client_socket.send(b"OK Message follows \r\n")

        elif data.startswith("QUIT"):
            client_socket.send(b"OK Goodbye")
            client_socket.close()
            print("Connection is closed!!!")
            break

pop3_server()

