import asyncio

from .util import delay


async def main():
    long_task = asyncio.create_task(delay(5))

    seconds_elapsed = 0
    while not long_task.done():
        print(f"{seconds_elapsed}. Task not finished, checking again in a second.")
        await asyncio.sleep(1)
        seconds_elapsed = seconds_elapsed + 1
        if seconds_elapsed >= 3:
            long_task.cancel()
            break
    print(long_task.done())
    print(long_task.cancelled())
    await asyncio.sleep(1)
    print(long_task.done())
    print(long_task.cancelled())

    # try:
    #     await long_task
    # except asyncio.CancelledError:
    #     print("Task cancelled.")


if __name__ == "__main__":
    asyncio.run(main())
