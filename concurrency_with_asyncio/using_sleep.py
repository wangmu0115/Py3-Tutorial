import asyncio


async def hello_world() -> str:
    await asyncio.sleep(1)
    return "Hello World"


async def main():
    msg = await hello_world()
    print(msg)


if __name__ == "__main__":
    asyncio.run(main())
