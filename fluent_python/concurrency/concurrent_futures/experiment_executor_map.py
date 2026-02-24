import time
from concurrent.futures import ThreadPoolExecutor


def display(*args):
    print(time.strftime("[%H:%M:%S]"), end=" ")
    print(*args)


def loiter(n):
    display(f"{'-' * n}loiter({n}): doing nothing for {n} seconds.")
    time.sleep(n)
    display(f"{'-' * n}loiter({n}): done.")
    return n * 10


def main():
    display("Script starting.")
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(loiter, range(1, 6))
        display("results: ", results)
        display("Waiting for individual results:")
        for i, result in enumerate(results, 1):
            display(f"result {i}: {result}")


if __name__ == "__main__":
    main()
