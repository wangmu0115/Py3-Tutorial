"""Round a floating-point number to a fixed number of decimal places.

- round(number, ndigits=None)
"""


def builtin_round():
    print(">>>", round(1.23, 1))  # 1.2
    print(">>>", round(1.27, 1))  # 1.3
    print(">>>", round(-1.23, 1))  # -1.2
    print(">>>", round(-1.27, 1))  # -1.3
    print(">>>", round(1.25361, 3))  # 1.254
    print(">>>", round(1.5, 0))  # 2.0
    print(">>>", round(2.5, 0))  # 2.0

    print(">>>", round(1627731, -1))  # 1627730
    print(">>>", round(1627731, -2))  # 1627700
    print(">>>", round(1627731, -3))  # 1628000


def builtin_format():
    print(">>>", format(1.23456, ".3f"))  # '1.235'
    print(">>>", round(1.23456, 3))  # 1.235

    print(">>>", format(2.5, ".0f"))  # '2'
    print(">>>", format(3.5, ".0f"))  # '4'
    print(">>>", round(2.5))  # 2
    print(">>>", round(3.5))  # 4


if __name__ == "__main__":
    builtin_round()
    print("-" * 80)
    builtin_format()
