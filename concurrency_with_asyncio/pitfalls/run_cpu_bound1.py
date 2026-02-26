import asyncio

from concurrency_with_asyncio.utils.delay_functions import async_timed


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(1, 100000000):
        counter += i
    return counter


@async_timed()
async def main():
    event_loop = asyncio.get_running_loop()
    event_loop.slow_callback_duration = 1.7
    task1 = asyncio.create_task(cpu_bound_work())
    task2 = asyncio.create_task(cpu_bound_work())
    await task1
    await task2


if __name__ == "__main__":
    asyncio.run(main(), debug=True)
