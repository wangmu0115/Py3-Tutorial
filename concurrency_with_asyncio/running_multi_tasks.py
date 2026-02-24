import asyncio
import time


async def main():
    start = time.perf_counter()
    sleep_for_three_1 = asyncio.create_task(asyncio.sleep(3.0))
    await sleep_for_three_1

    sleep_for_three_2 = asyncio.create_task(asyncio.sleep(3.0))
    sleep_for_three_3 = asyncio.create_task(asyncio.sleep(3.0))

    await sleep_for_three_2
    await sleep_for_three_3
    print(time.perf_counter() - start)


if __name__ == "__main__":
    asyncio.run(main())
