import asyncio

from aiohttp import ClientSession
from utils import async_timed


async def fetch_status(session: ClientSession, url: str):
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    async with ClientSession() as session:
        tasks = [
            asyncio.create_task(fetch_status(session, "https://www.example.com")),
            asyncio.create_task(fetch_status(session, "https://www.example.com")),
        ]
        done, pending = await asyncio.wait(tasks)
        print(f"Done task count: {len(done)}")
        print(f"Pending task count: {len(pending)}")

        for done_task in done:
            result = await done_task
            print(result)


asyncio.run(main())
