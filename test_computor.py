from decimal import Decimal
from parse_equation import parse_equation
import pytest

# TODO test display_complex
# TODO test display_reduced_form
# TODO test get_solutions (2nd and 3rd)
# TODO full bonus


def check_equation(s, expected):
    assert parse_equation(s) == list(map(Decimal, expected))


def test_parse_equation_good():
    check_equation("0=0", [])
    check_equation("3X=2X+1*X^1", [])
    check_equation("1=0", [1])
    check_equation("0=42", [-42])
    check_equation("X=0", [0, 1])
    check_equation("X^2=0", [0, 0, 1])
    check_equation("1*X^2=0", [0, 0, 1])
    check_equation("1X^2=0", [0, 0, 1])
    check_equation("5 * X^0 + 4 * X^1 = 4 * X^0", [1, 4])
    check_equation("5 + 4 * X + X^2= X^2", [5, 4])
    check_equation("X^3+18X^2+X+1=0", [1, 1, 18, 1])
    check_equation("-7X^5 = X^2", [0, 0, -1, 0, 0, -7])
    check_equation("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0", [4, 4, "-9.3"])
    check_equation(
        "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0", [5, -6, 0, "-5.6"]
    )


def test_parse_equation_bad():
    for s in ["42", "2x=0", "=", "X^-1 = 42", "(2+2)*X^2=0"]:
        with pytest.raises(SystemExit):
            parse_equation(s)
