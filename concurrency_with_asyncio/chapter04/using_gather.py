import asyncio

from aiohttp import ClientSession
from utils import async_timed, delay


async def fetch_status(session: ClientSession, url):
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ["http://www.example.com" for _ in range(200)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)


async def main2():
    results = await asyncio.gather(delay(3), delay(1))
    print(results)


# asyncio.run(main())

asyncio.run(main2())
