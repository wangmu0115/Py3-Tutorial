import asyncio

from aiohttp import ClientSession, ClientTimeout


async def fetch_status(session: ClientSession, url: str) -> int:
    timeout = ClientTimeout(total=0.8)
    async with session.get(url, timeout=timeout) as result:
        return result.status


async def main():
    async with ClientSession(timeout=ClientTimeout(total=1, connect=0.1)) as session:
        url = "http://www.example.com"
        status = await fetch_status(session, url)
        print(f"Status of {url} is {status}")


asyncio.run(main())
