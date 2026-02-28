import asyncio

from utils import async_timed, delay


@async_timed()
async def main():
    delay_times = [3, 5, 3]
    # [await asyncio.create_task(delay(delay_time)) for delay_time in delay_times]
    tasks = [asyncio.create_task(delay(delay_time)) for delay_time in delay_times]
    [await task for task in tasks]


asyncio.run(main())
