from collections.abc import Coroutine
from types import CoroutineType

# event_loop = asyncio.new_event_loop()
# event_loop.run_forever()


def print_hello():
    print("Hi, I am a lowly, simple printer, though I have all I need in life -- ")
    print("fresh paper and my dearly beloved octopus partner in crime.")


async def loudmouth_penguin(magic_number: int):
    print("I am a super special talking penguin. Far cooler than that printer. ")
    print(f"By the way, my lucky number is: {magic_number}.")


if __name__ == "__main__":
    print_hello()
    print(loudmouth_penguin(42))


CoroutineType
Coroutine
