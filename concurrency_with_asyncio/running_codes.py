import asyncio

from .util import delay


async def hello_every_seconds():
    for i in range(10):
        await asyncio.sleep(1)
        print(f"{i}: I'm running other codes while I'm waiting.")


async def main():
    first_delay = asyncio.create_task(delay(2.0))
    second_delay = asyncio.create_task(delay(5.0))

    asyncio.create_task(hello_every_seconds())

    delay1 = await first_delay
    print(delay1)
    delay2 = await second_delay
    print(delay2)


if __name__ == "__main__": 
    asyncio.run(main())
