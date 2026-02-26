import asyncio


async def demo_task():
    await asyncio.sleep(1)
    counter = 0
    for i in range(1000000000):
        counter += i
    print(f"The sum is: {counter}")
    return counter


async def main():
    long_task = asyncio.create_task(demo_task())

    print("Task not finished, checking again in a second.")
    # 0.9, raise `CancelledError`; 1.1, even cancelled the task, but also execute plain python code.
    await asyncio.sleep(0.9)
    # await asyncio.sleep(1.1)
    long_task.cancel()

    try:
        print(await long_task)
    except asyncio.CancelledError:
        print("Task canceled.")


asyncio.run(main())
