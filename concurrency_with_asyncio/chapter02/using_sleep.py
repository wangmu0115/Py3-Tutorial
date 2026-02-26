import asyncio

from utils import delay


async def hello_world() -> str:
    await delay(3.0)
    return "Hello World"


async def incr(n: int) -> int:
    return n + 1


async def main():
    msg = await hello_world()
    num = await incr(42)
    print(num)
    print(msg)


if __name__ == "__main__":
    asyncio.run(main())
