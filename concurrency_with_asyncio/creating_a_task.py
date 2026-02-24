import asyncio

from .util import delay


async def main():
    delay_times_task = asyncio.create_task(delay(1.5))
    print(type(delay_times_task))
    delay_times = await delay_times_task
    print(delay_times)


if __name__ == "__main__":
    asyncio.run(main())
