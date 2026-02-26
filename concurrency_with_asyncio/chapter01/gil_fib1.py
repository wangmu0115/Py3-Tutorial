import time


def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def print_fib(number: int) -> None:
    print(f"fib({number}) = {fib(number)}")


def fibs_no_threading():
    print_fib(40)
    print_fib(41)


start = time.perf_counter()
fibs_no_threading()
end = time.perf_counter()

print(f"Completed in {(end - start): .4f} seconds.")
