import asyncio

from concurrency_with_asyncio.util import async_timed, delay


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(1, 100000000):
        counter += i
    return counter


@async_timed()
async def main():
    task1 = asyncio.create_task(cpu_bound_work())
    task2 = asyncio.create_task(cpu_bound_work())
    delay_task = asyncio.create_task(delay(2))
    await task1
    await task2
    await delay_task


if __name__ == "__main__":
    asyncio.run(main())
