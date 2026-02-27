import socket
from socket import AF_INET, SO_REUSEADDR, SOCK_STREAM, SOL_SOCKET


def new_server_socket():
    server_socket = socket.socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", 8000))
    server_socket.listen()

    return server_socket


def main():
    server_socket = new_server_socket()
    server_socket.setblocking(False)  # non-blocking

    all_conns: list[socket.socket] = []
    try:
        while True:
            try:
                connection, client_address = server_socket.accept()
                connection.setblocking(False)  # non-blocking
                print(f"Get a connection from {client_address}")
                all_conns.append(connection)

                print(f"connections: {len(all_conns)}")
            except BlockingIOError:
                pass
            for conn in all_conns:
                try:
                    buffer = b""
                    while buffer[-2:] != b"\r\n":
                        data = conn.recv(1024)
                        if not data:
                            break
                        else:
                            print(f"Get data from {conn}: {data}")
                            buffer += data
                    print(f"All data is: {buffer}")
                    conn.sendall(b"[ECHO] -> " + buffer)
                except BlockingIOError:
                    pass
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
