from fractions import Fraction
from src.solve import solve_second_degree, solve_third_degree
from src.utils import get_degree, is_integer


PRECISION = 6


def __format_real(x):
    assert isinstance(x, float) or isinstance(x, Fraction)
    if isinstance(x, float):
        x += 0.0  # avoids -0.0
    rounded = str(round(float(x), PRECISION))
    if is_integer(x):
        return str(x)
    elif isinstance(x, float):
        return rounded
    else:
        return f"{x} ({rounded})"


def __format_complex(z):
    z = complex(z)
    real = round(z.real, PRECISION)
    imag = round(z.imag, PRECISION)
    if real.is_integer() and imag.is_integer():
        real = int(real)
        imag = int(imag)
    return (
        f"{real}{imag:+}i"
        if real and imag
        else f"{imag}i"
        if imag
        else str(z).replace("j", "i").replace("(", "").replace(")", "")
    )


def __print_first_degree(reduced):
    print(f"The solution is {__format_real(-reduced[0] / reduced[1])}")


def __print_second_degree(reduced):
    discriminant, (x1, x2) = solve_second_degree(reduced)
    if discriminant > 0:
        print("Discriminant is positive, the two solutions are:")
        print(__format_real(x1))
        print(__format_real(x2))
    elif discriminant < 0:
        print("Discriminant is negative, the two solutions are:")
        print(__format_complex(x1))
        print(__format_complex(x2))
    else:
        print(
            f"Discriminant is zero, the solution of multiplicity 2 is {__format_real(x1)}"
        )


def __print_third_degree(reduced):
    discriminant, (x1, x2, x3) = solve_third_degree(reduced)
    if discriminant >= 0:
        print("Discriminant is non-negative, the 3 real solutions are:")
        for x in sorted([x1.real, x2.real, x3.real]):
            print(__format_real(x))
    elif discriminant < 0:
        print("Discriminant is negative, the 3 real solutions are:")
        x1, x2, x3 = sorted([x1, x2, x3], key=lambda x: abs(x.imag))
        print(__format_real(x1.real))
        print(__format_complex(x2))
        print(__format_complex(x3))


def print_solutions(reduced):
    degree = get_degree(reduced)
    reduced = list(map(Fraction, reduced))
    if degree == -1:
        print("There are infinitely many solutions.")
    elif degree == 0:
        print("There are no solutions.")
    elif degree == 1:
        __print_first_degree(reduced)
    elif degree == 2:
        __print_second_degree(reduced)
    elif degree == 3:
        __print_third_degree(reduced)
    else:
        print("The polynomial degree is greater than 3, I can't solve.")
