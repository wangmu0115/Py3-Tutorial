import asyncio
import socket
from asyncio import AbstractEventLoop


async def echo(connection: socket.socket, loop: AbstractEventLoop):
    # while data := await loop.sock_recv(connection, 1024):
    #     await loop.sock_sendall(connection, b"[ECHO] -> " + data)
    while True:
        buffer = b""
        while buffer[-2:] != b"\r\n":
            data = await loop.sock_recv(connection, 1024)
            if data:
                buffer += data
            else:
                break
        success = await loop.sock_sendall(connection, b"[ECHO] -> " + buffer) is None
        print(f"Data is {buffer}, sended: {success}")


async def listen_connections(server_socket: socket.socket, loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)  # non-blocking
        print(f"Get a connection from {address}")
        asyncio.create_task(echo(connection, loop))


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", 8000))
    server_socket.listen()
    server_socket.setblocking(False)

    await listen_connections(server_socket, asyncio.get_running_loop())


if __name__ == "__main__":
    asyncio.run(main())
