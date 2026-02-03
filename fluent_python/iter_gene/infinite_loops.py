"""Replacing Infinite while Loops with an Iterator

Problem:
    You have code that uses a while loop to iteratively process data
    because it involves a function or some kind of unusual test condition
    that doesn't fall into the usual iteration pattern.

Solution:
    iter(callable, sentinel)
"""


def reader(s, chunksize: int = 8192):
    while True:
        data = s.recv(chunksize)
        if data == b"":
            break
        # Process Data


def reader2(s, chunksize: int = 8192):
    for chunk in iter(lambda: s.recv(chunksize), b""):
        pass  # Process Data


if __name__ == "__main__":
    with open("/etc/passwd") as fp:
        for chunk in iter(lambda: fp.read(128), ""):
            print(chunk)
