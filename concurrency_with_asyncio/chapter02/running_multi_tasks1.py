import asyncio

from utils import delay


async def main():
    sleep_task1 = asyncio.create_task(delay(3.0))
    sleep_task2 = asyncio.create_task(delay(3.0))
    sleep_task3 = asyncio.create_task(delay(3.0))

    await sleep_task1
    await sleep_task2
    await sleep_task3


asyncio.run(main())
