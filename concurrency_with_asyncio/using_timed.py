import asyncio

from .util import async_timed, delay


@async_timed()
async def main():
    task1 = asyncio.create_task(delay(2))
    task2 = asyncio.create_task(delay(3))

    await task1
    await task2


if __name__ == "__main__":
    asyncio.run(main())
