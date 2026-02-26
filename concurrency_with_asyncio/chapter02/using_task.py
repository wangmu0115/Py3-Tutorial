import asyncio

from utils import delay


async def main():
    sleep_three_seconds = asyncio.create_task(delay(3.0))
    print(type(sleep_three_seconds))
    result = await sleep_three_seconds
    print(result)


asyncio.run(main())
