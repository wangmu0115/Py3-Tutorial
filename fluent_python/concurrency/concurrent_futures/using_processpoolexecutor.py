import math
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

PRIMEs = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        sqrt_n = math.ceil(math.sqrt(n))
        for i in range(3, sqrt_n):
            if n % i == 0:
                return False
        return True


if __name__ == "__main__":
    t0 = time.perf_counter()
    with ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMEs, executor.map(is_prime, PRIMEs)):
            print(f"{number} is prime? {prime}")
    t1 = time.perf_counter()
    print(f"Using ProcessPoolExecutor elasped: {(t1 - t0): .4f} seconds\n")
    with ThreadPoolExecutor() as executor:
        for number, prime in zip(PRIMEs, executor.map(is_prime, PRIMEs)):
            print(f"{number} is prime? {prime}")
    t2 = time.perf_counter()
    print(f"Using ThreadPoolExecutor elasped: {(t2 - t1): .4f} seconds\n")
