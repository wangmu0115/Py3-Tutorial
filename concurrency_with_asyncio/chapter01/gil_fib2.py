import time
from threading import Thread


def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def print_fib(number: int) -> None:
    print(f"fib({number}) = {fib(number)}")


def fibs_with_threads():
    thread1 = Thread(target=print_fib, args=(40,))
    thread2 = Thread(target=print_fib, args=(41,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


start = time.perf_counter()
fibs_with_threads()
end = time.perf_counter()

print(f"Completed in {(end - start): .4f} seconds.")
