"""Starting and Stopping Threads

- `threading` module: https://docs.python.org/3/library/threading.html
"""

import time
from threading import Thread


def countdown(n: int):
    while n > 0:
        print("T-minus:", n)
        n -= 1
        time.sleep(1)


def check_state(t: Thread):
    while True:
        if t.is_alive():
            print("Still running")
        else:
            print("Completed")
            break
        time.sleep(3)


if __name__ == "__main__":
    t = Thread(target=countdown, args=(10,))
    t.start()

    t2 = Thread(target=check_state, args=(t,), daemon=True)
    t2.start()
    # t2.join()
