"""Exchanged safely between multiple threads: https://docs.python.org/3/library/queue.html

`queue` module implements three types of queue:
- `Queue`: a FIFO queue.
- `LifoQueue`: a LIFO queue.
- `PriorityQueue`: a priority queue.
"""

import time
from queue import Queue
from threading import Thread


def producer(q: Queue, n):
    while n >= 0:
        # Produce some data
        data = {"version": "v1", "data": "Hello World" + str(n)}
        q.put(data)
        n -= 1
        time.sleep(1)


def consumer(q: Queue):
    while True:
        data = q.get()
        print(data)


if __name__ == "__main__":
    q = Queue(maxsize=1024)
    t1 = Thread(target=producer, args=(q, 10))
    t2 = Thread(target=consumer, args=(q,))

    t1.start()
    time.sleep(5)
    t2.start()

    import sys

    print(sys.getswitchinterval())
