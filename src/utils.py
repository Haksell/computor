from decimal import Decimal
from fractions import Fraction
from math import isqrt
import sys


def ft_assert(check, message):
    if not check:
        print(message)
        sys.exit(1)


def get_degree(reduced):
    return len(reduced) - 1


def exact_isqrt(n):
    assert isinstance(n, int)
    if n < 0:
        return None
    i = isqrt(n)
    return i if i * i == n else None


def sqrt_fraction(frac):
    assert isinstance(frac, Fraction)
    return (
        Fraction(isqrt_numer, isqrt_denom)
        if frac >= 0
        and (isqrt_numer := exact_isqrt(frac.numerator)) is not None
        and (isqrt_denom := exact_isqrt(frac.denominator)) is not None
        else frac**0.5
    )


def is_integer(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return x.is_integer()
    elif isinstance(x, complex):
        return x.real.is_integer() and x.imag == 0
    elif isinstance(x, Decimal):
        return x.as_integer_ratio()[1] == 1
    elif isinstance(x, Fraction):
        return x.denominator == 1
    else:
        ft_assert(False, f"type {type(x)} not supported in function is_integer")
