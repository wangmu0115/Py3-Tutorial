import asyncio

from aiohttp import ClientSession
from utils import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url):
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ["http://www.example.com", "python://www.example.com"]
        requests = [fetch_status(session, url) for url in urls]
        responses = await asyncio.gather(*requests, return_exceptions=True)

        failure_results = [response for response in responses if isinstance(response, BaseException)]
        success_results = [response for response in responses if not isinstance(response, BaseException)]
        print(f"All results: {responses}")
        print(f"Failure results: {failure_results}")
        print(f"Success results: {success_results}")


asyncio.run(main())
