import asyncio

from utils import delay


async def main():
    delay_task = asyncio.create_task(delay(3.0))
    try:
        result = await asyncio.wait_for(delay_task, timeout=1.0)
        print(result)
    except TimeoutError:
        print("Got a timeout")
        print("Was the task cancelled?", delay_task.cancelled(), delay_task.done())


asyncio.run(main())