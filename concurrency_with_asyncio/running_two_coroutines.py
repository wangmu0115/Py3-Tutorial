import asyncio

from .util import delay


async def incr(number: int) -> int:
    await delay(1.0)
    return number + 1


async def hello_world() -> str:
    await delay(2.0)
    return "Hello World"


async def main():
    num = await incr(42)
    msg = await hello_world()
    print(num)
    print(msg)


if __name__ == "__main__":
    asyncio.run(main())
