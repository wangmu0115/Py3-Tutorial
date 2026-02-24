import asyncio


async def add_one(number: int) -> int:
    return number + 1


async def main():
    one_add_one = await add_one(1)
    two_add_one = await add_one(2)
    print(one_add_one)
    print(two_add_one)


if __name__ == "__main__":
    asyncio.run(main())
