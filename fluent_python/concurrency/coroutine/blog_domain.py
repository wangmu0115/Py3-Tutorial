""""""

import asyncio


async def probe(domain: str) -> tuple[str, bool]:
    loop = asyncio.get_running_loop()
