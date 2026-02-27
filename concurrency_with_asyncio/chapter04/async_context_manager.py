import asyncio
import socket
from types import TracebackType
from typing import Optional, Type


class ConnectedSocket:
    def __init__(self, server_socket: socket.socket):
        self._server_socket = server_socket
        self._connection = None

    async def __aenter__(self):
        """This coroutine is called when we enter the with block.
        It waits until a client connects and returns the connection.
        """
        print("Enter context manager, waiting for connection.")
        loop = asyncio.get_running_loop()
        connection, address = await loop.sock_accept(self._server_socket)
        self._connection = connection
        print(f"Get a connection from {address}")
        return self._connection

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ):
        """This coroutine is called when we exit the with block.
        In it, we clean up any resources we use. In this case, we close the connection.
        """
        print("Exiting context manager.")
        self._connection.close()
        print("Closed connection.")


async def main():
    loop = asyncio.get_running_loop()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", 8000))
    server_socket.listen()
    server_socket.setblocking(False)

    async with ConnectedSocket(server_socket) as conn:
        data = await loop.sock_recv(conn, 1024)
        print(data)


if __name__ == "__main__":
    asyncio.run(main())
