import asyncio


async def hello_world() -> str:
    return "Hello World"


async def incr(n: int) -> int:
    return n + 1


if __name__ == "__main__":
    msg = hello_world()
    num = incr(42)
    print(asyncio.run(msg))
    print(asyncio.run(num))
