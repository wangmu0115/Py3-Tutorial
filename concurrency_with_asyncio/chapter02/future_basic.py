import asyncio
from asyncio import Future


async def main():
    future = Future()
    print(f"Future is done? {future.done()}, value is {future.result()}")
    future.set_result(42)
    print(f"Future is done? {future.done()}, value is {future.result()}")


asyncio.run(main())
