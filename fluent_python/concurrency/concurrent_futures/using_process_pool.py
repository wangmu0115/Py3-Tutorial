import time
from concurrent.futures import ProcessPoolExecutor
from typing import NamedTuple

from .prime import NUMBERS, is_prime


class PrimeResult(NamedTuple):
    n: int
    prime: bool
    elapsed: float


def check(n: int) -> PrimeResult:
    t0 = time.perf_counter()
    prime = is_prime(n)
    return PrimeResult(n, prime, time.perf_counter() - t0)


def main():
    t0 = time.perf_counter()
    with ProcessPoolExecutor() as executor:
        n_workers = executor._max_workers
        print(f"Checking {len(NUMBERS)} numbers with {n_workers} processes:\n")
        for n, prime, elapsed in executor.map(check, reversed(NUMBERS)):
            print(f"{n:16}  {'P' if prime else ' '} {elapsed: 9.6f}s")
    print(f"\nTotal elapsed: {(time.perf_counter() - t0): .4f}s")


# uv run -m fluent_python.concurrency.concurrent_futures.using_process_pool
if __name__ == "__main__":
    main()
