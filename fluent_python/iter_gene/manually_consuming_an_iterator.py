"""Manually Consuming an Iterator

Problem:
    You need to process items in an iterable, but for whatever reason,
    you can't or don't want to use a `for` loop.

Solution:
    iter()
    next(it)
    next(it, default)
    StopIteration
"""

from typing import Iterator


def manual_iter(it: Iterator):
    while True:
        try:
            item = next(it)
            print(item)
        except StopIteration:
            break
        except:
            raise


if __name__ == "__main__":
    with open("/etc/passwd") as fp:
        manual_iter(fp)

    items = [1, 3, 5, 7, 2, 4, 6, 8]
    it = iter(items)
    while True:
        item = next(it, None)
        if item:
            print(item, end=", ")
        else:
            print()
            break
