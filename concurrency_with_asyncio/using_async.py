import asyncio


async def my_coroutine() -> None:
    print("Hello World")


def add_one(number: int) -> int:
    return number + 1


async def coroutine_add_one(number: int) -> int:
    return number + 1


if __name__ == "__main__":
    function_result = add_one(42)
    coroutine_result = coroutine_add_one(42)
    print(function_result, type(function_result))
    print(coroutine_result, type(coroutine_result))
    new_coroutine_result = asyncio.run(coroutine_add_one(42))
    print(new_coroutine_result, type(new_coroutine_result))
