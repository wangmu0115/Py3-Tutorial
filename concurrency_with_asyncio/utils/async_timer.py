import functools
import time
from typing import Any, Callable


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f">>> starting {func} with args {args} {kwargs}")
            start = time.perf_counter()
            try:
                return await func(*args, **kwargs)
            finally:
                elapsed = time.perf_counter() - start
                print(f"<<< finished {func} with args {args} {kwargs} in {elapsed: .4f} second(s)")

        return wrapped

    return wrapper
