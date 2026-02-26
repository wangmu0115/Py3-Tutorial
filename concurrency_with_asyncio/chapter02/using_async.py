async def coroutine_hello_world() -> str:
    return "Hello World"


def incr(n: int) -> int:
    return n + 1


if __name__ == "__main__":
    msg = coroutine_hello_world()
    num = incr(42)

    print(f"Function result is {num}, type is {type(num)}")
    print(f"Coroutine result is {msg}, type is {type(msg)}")
