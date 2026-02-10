"""`Lock` object

Thread scheduling is **nondeterministic**.
"race condition" <= locks should always be used whenever shared mutable state.
"""

from threading import Lock


class SharedCounter:
    def __init__(self, init_value: int = 0):
        self._value = init_value
        self._value_lock = Lock()

    def incr(self, delta: int = 1):
        with self._value_lock:
            self._value += delta

    def decr(self, delta: int = 1):
        with self._value_lock:
            self._value -= delta
