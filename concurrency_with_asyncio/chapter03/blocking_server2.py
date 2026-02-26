import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)
server_socket.bind(server_address)
server_socket.listen()

connections = []

try:
    while True:
        conn, client_address = server_socket.accept()  # Wait for a connection and assign the client to a PO box.
        print(f"I get a connection from {client_address}")
        connections.append(conn)

        for connection in connections:
            buffer = b""
            while buffer[-2:] != b"\r\n":
                data = connection.recv(4)
                if not data:
                    break
                else:
                    print(f"I get data: {data}")
                    buffer += data
            print(f"All the data: {buffer}")
            connection.sendall(b"[ECHO]: " + buffer)
finally:
    server_socket.close()
