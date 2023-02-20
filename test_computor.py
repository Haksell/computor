from decimal import Decimal
from parse_equation import parse_equation
import pytest


def check_equation(s, expected):
    assert parse_equation(s) == {p: Decimal(a) for p, a in expected.items()}


def test_parse_equation_good():
    check_equation("0=0", {})
    check_equation("1=0", {0: "1"})
    check_equation("X=0", {1: "1"})
    check_equation("X^2=0", {2: "1"})
    check_equation("1*X^2=0", {2: "1"})
    check_equation(
        "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0", {0: "4", 1: "4", 2: "-9.3"}
    )
    check_equation("5 * X^0 + 4 * X^1 = 4 * X^0", {0: "1", 1: "4"})
    check_equation(
        "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0",
        {0: "5", 1: "-6", 3: "-5.6"},
    )
    check_equation("5 + 4 * X + X^2= X^2", {0: "5", 1: "4"})


def test_parse_equation_bad():
    for s in ["42", "x = 0", "2X = 0", "="]:
        with pytest.raises(SystemExit):
            parse_equation(s)
