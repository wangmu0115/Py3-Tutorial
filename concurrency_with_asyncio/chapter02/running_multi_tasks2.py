import asyncio

from utils import delay


async def print_every_second():
    index = 1
    while True:
        await asyncio.sleep(1.0)
        print(f"[{index}]: I'm running other codes while I'm waiting.")
        index += 1


async def main():
    sleep_task1 = asyncio.create_task(delay(3.0))
    sleep_task2 = asyncio.create_task(delay(5.0))
    asyncio.create_task(print_every_second())  # Background task
    await sleep_task1
    await sleep_task2


if __name__ == "__main__":
    asyncio.run(main())
