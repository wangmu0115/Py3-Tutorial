import asyncio

from utils import delay


async def main():
    task = asyncio.create_task(delay(5.0))

    try:
        result = await asyncio.wait_for(asyncio.shield(task), timeout=3.0)
        print(result)
    except TimeoutError:
        print("Task took longer than three seconds, it will finish soon.")
        result = await task
        print(result)


asyncio.run(main())
