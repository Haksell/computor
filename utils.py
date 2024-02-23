from math import isqrt
import sys


def ft_assert(check, message):
    if not check:
        print(message)
        sys.exit(1)


def get_degree(reduced):
    return len(reduced) - 1


def is_square(n):
    assert isinstance(n, int)
    if n < 0:
        return False
    i = isqrt(n)
    return i * i == n
