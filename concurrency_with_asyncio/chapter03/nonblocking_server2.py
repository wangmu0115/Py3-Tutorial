import selectors
import socket

selector = selectors.DefaultSelector()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("127.0.0.1", 8000))
server_socket.listen()
server_socket.setblocking(False)

selector.register(server_socket, selectors.EVENT_READ)

while True:
    events: list[tuple[selectors.SelectorKey, int]] = selector.select(timeout=1.0)
    if len(events) == 0:
        print("No events, waiting a bit more.")
        continue
    for event, _ in events:
        event_socket = event.fileobj
        if event_socket == server_socket:
            conn, address = server_socket.accept()
            conn.setblocking(False)
            print(f"I got a connection from {address}.")
            selector.register(conn, selectors.EVENT_READ)
        else:
            data = event_socket.recv(1024)
            print(f"I got the data: {data}")
            event_socket.sendall(b"[ECHO] -> " + data)


# connections = []

# try:
#     while True:
#         try:
#             conn, client_address = server_socket.accept()
#             conn.setblocking(False)  # Make the client socket as non-blocking.
#             print(f"I got a connection from {client_address}.")
#             connections.append(conn)
#         except BlockingIOError:
#             pass

#         for connection in connections:
#             try:
#                 buffer = b""
#                 while buffer[-2:] != b"\r\n":
#                     data = connection.recv(4)
#                     if not data:
#                         break
#                     else:
#                         print(f"I got data: {data}")
#                         buffer += data
#                 print(f"All data is: {buffer}")
#                 connection.sendall(b"[ECHO] -> " + buffer)
#             except BlockingIOError:
#                 pass
# finally:
#     server_socket.close()
