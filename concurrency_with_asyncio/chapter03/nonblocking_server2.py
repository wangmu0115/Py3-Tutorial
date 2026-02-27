import selectors
import socket
from selectors import EVENT_READ, SelectorKey
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

    selector = selectors.DefaultSelector()
    selector.register(server_socket, EVENT_READ)  # available for read

    while True:
        events: list[tuple[SelectorKey, int]] = selector.select(timeout=1)
        if len(events) == 0:
            print("No events, wait for 1 second.")
            continue
        for event, _ in events:
            event_socket = event.fileobj  # Get socket
            if event_socket == server_socket:
                conn, client_address = server_socket.accept()
                conn.setblocking(False)  # non-blocking
                print(f"Get a connection from {client_address}")
                selector.register(conn, EVENT_READ)
            else:
                buffer = b""
                while buffer[-2:] != b"\r\n":
                    data = event_socket.recv(1024)
                    if data:
                        buffer += data
                    else:
                        break
                print(f"Get data: {buffer}")
                event_socket.sendall(b"[ECHO] -> " + buffer)


if __name__ == "__main__":
    main()
