from fractions import Fraction
from math import isqrt, sqrt
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
