"""`Event` object

Used to communication between threads: one thread signals an event and other threads wait for it.
- set()
- wait(timeout_seconds=None)
"""

import time
from threading import Event, Thread


def countdown(n: int, started_event: Event):
    print("countdown starting")
    started_event.set()
    while n >= 0:
        print("T-minus:", n)
        n -= 1
        time.sleep(2)


if __name__ == "__main__":
    event = Event()
    print("Launching countdown")
    t = Thread(target=countdown, args=(10, event))
    t.start()

    event.wait()
    print("countdown is running")
