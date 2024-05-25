from decimal import Decimal
from fractions import Fraction
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
    if n == 0:
        return 0
    g1 = 0
    g2 = n
    while True:
        g3 = (g2 + n // g2) >> 1
        if g3 == g1:
            return g1 if g1 * g1 == n else None
        g1 = g2
        g2 = g3


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
