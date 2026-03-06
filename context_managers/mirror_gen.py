import sys
from contextlib import contextmanager


@contextmanager
def looking_glass():
    try:
        original_write = sys.stdout.write
        sys.stdout.write = lambda text: original_write(text[::-1])
        yield "JABBERWOCKY"
    except:  # noqa: E722
        exc_type, exc_value, exc_tb = sys.exc_info()
        if exc_type is ZeroDivisionError:
            original_write("Please DO NOT divide zero.\n")
        else:
            raise
    finally:
        sys.stdout.write = original_write


if __name__ == "__main__":
    with looking_glass() as msg:
        print(msg)
        print("Hello World")
        print(1 / 0)
    print("Hello World")
