import asyncio
import logging

from aiohttp import ClientSession
from utils import async_timed


async def fetch_status(session: ClientSession, url: str):
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    async with ClientSession() as session:
        good_request = fetch_status(session, "http://www.example.com")
        bad_request = fetch_status(session, "http://bad")
        tasks = [asyncio.create_task(good_request), asyncio.create_task(bad_request)]

        done_tasks, pending_tasks = await asyncio.wait(tasks)
        print(f"Done task count: {len(done_tasks)}")
        print(f"Pending task count: {len(pending_tasks)}")

        for done_task in done_tasks:
            # print(await done_task)
            if done_task.exception() is None:
                print("Result::::", done_task.result())
            else:
                logging.error("Request get an exception", exc_info=done_task.exception())


asyncio.run(main())
