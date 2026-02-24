import asyncio
from asyncio import Future


async def main():
    my_future = Future()
    print(f"Is `future` done? {my_future.done()}")
    my_future.set_result(42)
    print(f"Is `future` done? {my_future.done()}")
    print(f"What's the result? {my_future.result()}")


if __name__ == "__main__":
    asyncio.run(main())
