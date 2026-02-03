"""Creating New Iteration Patterns with Generators

Problem:
    You want to implement a custom iteration pattern that's different than
    the usual built-in functions (e.g., range(), reversed(), etc.).

Solution:
    yield
    next()
"""


def frange(start, stop, increment):
    x = start
    while x <= stop:
        yield x
        x += increment


if __name__ == "__main__":
    for i in frange(0, 4, 0.5):
        print(i, end=", ")
    print()

    fr = frange(0, 2, 0.3)
    while True:
        try:
            print(next(fr), end=", ")
        except StopIteration:
            print()
            break
