from dataclasses import dataclass
from decimal import Decimal
from itertools import chain
import re
from src.utils import ft_assert

VALID_CHARACTERS = "0123456789X=.-+*^"
REGEX_V = r"(?:\d+)(?:\.\d+)?"
REGEX_D = r"X(?:\^\d+)?"
REGEX_MONOMIAL = rf"([+-])(?:({REGEX_V})\*?({REGEX_D})|({REGEX_V})|({REGEX_D}))"
REGEX_POLYNOMIAL = rf"({REGEX_MONOMIAL})+"


@dataclass
class Monomial:
    value: Decimal
    degree: int


def __create_monomial(sign, a1, p1, a2, p2):
    sign = 1 if sign == "+" else -1
    a = sign * Decimal(1 if p2 else a1 if a1 else a2)
    p = p1 or p2
    p = 0 if p == "" else 1 if p == "X" else int(p[2:])
    return Monomial(a, p)


def __reduce_equation(left, right):
    max_degree = max((m.degree for m in chain(left, right)), default=-1)
    reduced = [0] * (max_degree + 1)
    for m in chain(left):
        reduced[m.degree] += m.value
    for m in chain(right):
        reduced[m.degree] -= m.value
    while reduced and reduced[-1] == 0:
        reduced.pop()
    return reduced


def __parse_polynomial(s):
    p = s if s[0] in "-+" else "+" + s
    ft_assert(re.fullmatch(REGEX_POLYNOMIAL, p), f'"{s}" is not properly formatted')
    polynomial = re.findall(REGEX_MONOMIAL, p)
    return [__create_monomial(*groups) for groups in polynomial]


def parse_equation(s):
    s = "".join(c for c in s if not c.isspace())
    ft_assert(s.count("=") == 1, "There should be exactly one equal sign")
    invalid_characters = [c for c in s if c not in VALID_CHARACTERS]
    ft_assert(
        not invalid_characters,
        f"Invalid characters present in string: {invalid_characters}",
    )
    left, right = s.split("=")
    ft_assert(left or right, "both terms are empty")
    ft_assert(left, "left term is empty")
    ft_assert(right, "right term is empty")
    left, right = __parse_polynomial(left), __parse_polynomial(right)
    return __reduce_equation(left, right)
