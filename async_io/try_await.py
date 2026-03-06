class Rock:
    def __await__(self):
        value_sent_in = yield 9
        print(f"Rock.__await__ resuming with value: {value_sent_in}.")
        return value_sent_in


async def main():
    print("Beginning coroutine main().")
    rock = Rock()
    print("Awaiting rock...")
    value_from_rock = await rock
    print(f"Coroutine received value: {value_from_rock} from rock.")
    return 24


if __name__ == "__main__":
    coro = main()
    intermediate_result = coro.send(None)
    print(f"Coroutine paused and returned intermediate value: {intermediate_result}.")
    print("Resuming coroutine and sending in value: 42.")
    try:
        coro.send(42)
    except StopIteration as e:
        returned_value = e.value
        print(f"Coroutine main() finished and provided value: {returned_value}.")
