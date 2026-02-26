import asyncio

import httpx

from concurrency_with_asyncio.utils.delay_functions import async_timed


@async_timed()
async def get_example_status() -> int:
    return httpx.get("http://www.example.com").status_code


@async_timed()
async def main():
    task1 = asyncio.create_task(get_example_status())
    task2 = asyncio.create_task(get_example_status())
    task3 = asyncio.create_task(get_example_status())

    print(await task1)
    print(await task2)
    print(await task3)


if __name__ == "__main__":
    asyncio.run(main())
