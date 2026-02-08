import time
from threading import Thread


def countdown(n: int):
    while n >= 0:
        print(f"T-minus: {n}")
        n -= 1
        time.sleep(2)


class CountdownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self._n = n

    def run(self):
        while self._n >= 0:
            print("T-MINUS:", self._n)
            self._n -= 1
            time.sleep(2)


class ControlTaskState:
    def __init__(self):
        self._running = True

    def stop(self):
        self._running = False

    def __call__(self, n):
        while self._running and n >= 0:
            print(f"Task-minus: {n}")
            n -= 1
            time.sleep(2)
        print("Exist Task")


if __name__ == "__main__":
    # t = Thread(target=countdown, args=(10,), daemon=True)
    # print(t.is_alive())
    # t.start()
    # print(t.is_alive())
    # t.join()

    # t2 = CountdownThread(10)
    # t2.start()

    task = ControlTaskState()
    t = Thread(target=task, args=(10,))
    t.start()
    time.sleep(5)
    task.stop()
