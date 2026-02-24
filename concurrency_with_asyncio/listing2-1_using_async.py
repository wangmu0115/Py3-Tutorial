import asyncio


async def incr(number: int) -> int:
    return number + 1


async def main():
    one_incr = await incr(1)
    two_incr = await incr(2)
    print(one_incr)
    print(two_incr)


if __name__ == "__main__":
    asyncio.run(main())
