import socket
from socket import AF_INET, SO_REUSEADDR, SOCK_STREAM, SOL_SOCKET


def new_server_socket() -> socket.socket:
    server_socket = socket.socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", 8000))
    server_socket.listen()  # Enable server to accept connections

    return server_socket


def main():
    server_socket = new_server_socket()
    conn, client_address = server_socket.accept()  # Socket is blocked, the method will block.
    print(f"Get a connection from {client_address}")
    conn.sendall(b"Hello World\n")


if __name__ == "__main__":
    main()
