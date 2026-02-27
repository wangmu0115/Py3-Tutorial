import asyncio

from .async_timer import async_timed


@async_timed()
async def delay(seconds: float, debug: bool = True) -> float:
    if debug:
        print(f"sleeping for {seconds} second(s).")
        await asyncio.sleep(seconds)
        print(f"finished sleeping for {seconds} second(s).")
    else:
        await asyncio.sleep(seconds)
    return seconds
