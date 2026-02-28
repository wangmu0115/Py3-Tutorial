import asyncio

from aiohttp import ClientSession
from utils import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str, delay: float):
    if delay > 0.0:
        await asyncio.sleep(delay)

    async with session.get(url) as result:
        return (delay, result.status)


@async_timed()
async def main():
    async with ClientSession() as session:
        tasks = [
            fetch_status(session, "http://www.example.com", 5),
            fetch_status(session, "http://www.example.com", 3),
            fetch_status(session, "http://www.example.com", 1),
        ]
        for finished in asyncio.as_completed(tasks):
            print(await finished)


@async_timed()
async def main2():
    async with ClientSession() as session:
        tasks = [
            fetch_status(session, "http://www.example.com", 5),
            fetch_status(session, "http://www.example.com", 3),
            fetch_status(session, "http://www.example.com", 1),
        ]
        for finished_task in asyncio.as_completed(tasks, timeout=2.5):
            try:
                print(await finished_task)
            except TimeoutError:
                print("Timeout!!!")

        for task in asyncio.tasks.all_tasks():
            print(task)

        for task in asyncio.as_completed([task for task in asyncio.tasks.all_tasks() if task.get_name() != "Task-1"]):
            print(await task)


asyncio.run(main2())
