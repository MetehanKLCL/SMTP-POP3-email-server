import socket

def smtp_server(host="192.168.19.136", port=587):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"SMTP Server is Running... {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection: {client_address}")

    
        client_socket.send(b"220 Welcome to Python SMTP Server\r\n")
        data = client_socket.recv(1024).decode()
        print(f"İstemciden Gelen: {data}")

        if data.startswith("HELO"):
            client_socket.send(b"250 Hello Client\r\n")

        elif data.startswith("MAIL FROM:"):
            client_socket.send(b"250 OK\r\n")

        elif data.startswith("RCPT TO:"):
            client_socket.send(b"250 OK\r\n")

        elif data.startswith("DATA"):
            client_socket.send(b"354 Start mail input; end with <CRLF>.<CRLF>\r\n")
            message_data = client_socket.recv(1024).decode()
            print(f"E-posta İçeriği:\n{message_data}")
            client_socket.send(b"250 OK: Message received\r\n")
        
        elif data.startswith("QUIT"):
            client_socket.send(b"221 Bye\r\n")
            client_socket.close()
            print("Connection closed.")
            break

smtp_server()
