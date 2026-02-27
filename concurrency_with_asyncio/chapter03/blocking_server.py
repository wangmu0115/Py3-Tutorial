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
    try:
        conn, client_address = server_socket.accept()  # Socket is blocked, the method will block.
        print(f"Get a connection from {client_address}")

        buffer = b""  # Received data
        while buffer[-2:] != b"\r\n":  # [Enter]
            data = conn.recv(8)
            if data:
                print(f"Get data by loop: {data}")
                buffer += data
            else:
                break
        print(f"All data is {buffer}")
        conn.sendall(b"[ECHO] -> " + buffer)
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
