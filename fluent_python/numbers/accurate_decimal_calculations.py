"""Perform accurate calculations with decimal numbers.

- `decimal` module: https://docs.python.org/3/library/decimal.html
"""


def using_decimal():
    from decimal import Decimal

    a = 4.2
    b = 2.1
    real_a = Decimal(str(a))
    real_b = Decimal(str(b))
    read_sum = real_a + real_b
    print(f"{read_sum!r}")  # Decimal('6.3')


if __name__ == "__main__":
    print(">>>", "a = 4.2")
    print(">>>", "b = 2.1")
    print(">>>", f"a + b = {4.2 + 2.1}")
    print(">>>", f"(a + b) == 6.3 ? {4.2 + 2.1 == 6.3}")
    # These errors are a "feature" of the underlying CPU and
    # the IEEE 754 arithmetic per‐ formed by its floating-point unit.
    print("\n" + "=" * 80 + "\n")

    using_decimal()
