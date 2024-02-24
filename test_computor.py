from decimal import Decimal
from fractions import Fraction
from math import sqrt
from display import display_reduced_form, display_solutions
from parse_equation import parse_equation
import pytest
from utils import exact_isqrt, sqrt_fraction

# TODO test display_complex
# TODO test display_reduced_form
# TODO test get_solutions (2nd and 3rd)
# TODO full bonus


def test_exact_isqrt():
    assert exact_isqrt(-4) is None
    assert exact_isqrt(-3) is None
    assert exact_isqrt(-2) is None
    assert exact_isqrt(-1) is None
    assert exact_isqrt(0) == 0
    assert exact_isqrt(1) == 1
    assert exact_isqrt(2) is None
    assert exact_isqrt(3) is None
    assert exact_isqrt(4) == 2
    assert exact_isqrt(5) is None
    assert exact_isqrt(6) is None
    assert exact_isqrt(7) is None
    assert exact_isqrt(8) is None
    assert exact_isqrt(9) == 3
    assert exact_isqrt(10) is None


def test_sqrt_fraction():
    def is_complex_close(a, b):
        assert isinstance(a, float) or isinstance(a, complex)
        return abs(a - b) < 1e-4

    assert sqrt_fraction(Fraction(8, 2)) == Fraction(2, 1)
    assert sqrt_fraction(Fraction(9, 4)) == Fraction(3, 2)
    assert sqrt_fraction(Fraction(0, 42)) == Fraction(0, 1)
    assert is_complex_close(sqrt_fraction(Fraction(7, 2)), sqrt(3.5))
    assert is_complex_close(sqrt_fraction(Fraction(-4, 1)), 2j)
    assert is_complex_close(
        sqrt_fraction(Fraction(-42, 10)), 1.2548895456552942e-16 + 2.04939015319192j
    )


def test_parse_equation_good():
    def check_equation(s, expected):
        assert parse_equation(s) == list(map(Decimal, expected))

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
    for s in ["42", "2x=0", "3*X^2", "3*X^2=", "=", "X^-1 = 42", "(2+2)*X^2=0"]:
        with pytest.raises(SystemExit):
            parse_equation(s)


def test_display_reduced_form(capfd):
    def check_reduced_form(reduced, expected):
        display_reduced_form(reduced)
        out, _ = capfd.readouterr()
        assert out == f"Reduced form: {expected} = 0\n"

    check_reduced_form([], "0")
    check_reduced_form([42], "42")
    check_reduced_form([Decimal("-17.3")], "-17.3")
    check_reduced_form(
        [Decimal("-17.3"), Decimal("4.2"), 0, -4],
        "-17.3 * X^0 + 4.2 * X^1 + 0 * X^2 - 4 * X^3",
    )


def test_display_solutions(capfd):
    def check_solutions(reduced, expected):
        display_solutions(reduced)
        out, _ = capfd.readouterr()
        assert out == expected

    check_solutions([], "There are infinitely many solutions.\n")
    check_solutions([42], "There are no solutions.\n")
    check_solutions([Decimal("-13.37")], "There are no solutions.\n")
    check_solutions([0, 2], "The solution is 0\n")
    check_solutions([6, 3], "The solution is -2\n")
    check_solutions([2, -3], "The solution is 2/3 (0.666667)\n")
    check_solutions([Decimal("-4.2"), 3], "The solution is 7/5 (1.4)\n")
    check_solutions(
        [0, 0, -1],
        "Discriminant is zero, the solution of multiplicity 2 is 0\n",
    )
    check_solutions(
        [Decimal("-9.68"), 0, 2],
        "Discriminant is strictly positive, the two solutions are:\n-11/5 (-2.2)\n11/5 (2.2)\n",
    )
    check_solutions(
        [3, -6, 2],
        "Discriminant is strictly positive, the two solutions are:\n0.633975\n2.366025\n",
    )
    check_solutions(
        [4, -6, 2],
        "Discriminant is strictly positive, the two solutions are:\n1\n2\n",
    )
    check_solutions(
        [4.5, -6, 2],
        "Discriminant is zero, the solution of multiplicity 2 is 3/2 (1.5)\n",
    )
    # check_solutions([5, -6, 2], "")
    # check_solutions([6, -6, 2], "")
    check_solutions(
        [1, 2, 3, 4, 5],
        "The polynomial degree is strictly greater than 3, I can't solve.\n",
    )
