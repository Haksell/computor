from decimal import Decimal
from parse_equation import parse_equation
import pytest


def check_equation(s, expected):
    assert parse_equation(s) == expected


def test_parse_equation_good():
    check_equation("0=0", {})
    check_equation("1=0", {0: Decimal("1")})
    check_equation("X=0", {1: Decimal("1")})
    check_equation("X^2=0", {2: Decimal("1")})
    check_equation("1*X^2=0", {2: Decimal("1")})


def test_parse_equation_bad():
    for s in ["42", "x = 0", "2X = 0"]:
        with pytest.raises(SystemExit):
            parse_equation(s)
