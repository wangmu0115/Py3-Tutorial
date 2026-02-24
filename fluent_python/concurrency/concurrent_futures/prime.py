import math

PRIME_FIXTURE = [
    (2, True),
    (142702110479723, True),
    (299593572317531, True),
    (3333333333333301, True),
    (3333333333333333, False),
    (3333335652092209, False),
    (4444444444444423, True),
    (4444444444444444, False),
    (4444444488888889, False),
    (5555553133149889, False),
    (5555555555555503, True),
    (5555555555555555, False),
    (6666666666666666, False),
    (6666666666666719, True),
    (6666667141414921, False),
    (7777777536340681, False),
    (7777777777777753, True),
    (7777777777777777, False),
    (9999999999999917, True),
    (9999999999999999, False),
]

NUMBERS = [num for num, _ in PRIME_FIXTURE]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        sqrt_n = math.isqrt(n)
        for i in range(3, sqrt_n + 1):
            if n % i == 0:
                return False
        return True


if __name__ == "__main__":
    import time

    t0 = time.perf_counter()
    for num, prime in PRIME_FIXTURE:
        prime_res = is_prime(num)
        assert prime_res == prime
        print(f"{num} is prime? {prime}")
    print(f"\nElasped: {(time.perf_counter() - t0): .4f} seconds.")
