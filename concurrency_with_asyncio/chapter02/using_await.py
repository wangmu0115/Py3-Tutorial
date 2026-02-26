import asyncio


async def incr(n: int) -> int:
    return n + 1


async def main():
    one_incr = await incr(1)
    two_incr = await incr(2)

    print(one_incr, two_incr)


if __name__ == "__main__":
    asyncio.run(main())
