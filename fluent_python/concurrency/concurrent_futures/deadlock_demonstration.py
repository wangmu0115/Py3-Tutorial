import time
from concurrent.futures import ThreadPoolExecutor


def wait_on_b():
    time.sleep(5)
    print(b.result())
    return 5


def wait_on_a():
    time.sleep(5)
    print(a.result())
    return 6


if __name__ == "__main__":
    print("=" * 40, "Deadlock Demonstration", "=" * 40)
    executor = ThreadPoolExecutor(max_workers=2)
    a = executor.submit(wait_on_b)
    b = executor.submit(wait_on_a)
