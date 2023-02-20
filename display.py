from math import sqrt
from utils import get_degree


PRECISION = 6


def display_reduced_form(reduced):
    line = ["Reduced form:"]
    if not reduced:
        reduced[0] = 0
    for i, (p, m) in enumerate(sorted(reduced.items(), reverse=True)):
        if i != 0:
            line.append("-" if m < 0 else "+")
        line.append(f"{m if i==0 else abs(m)} * X^{p}")
    line.append("=")
    line.append("0")
    print(*line)


def display_polynomial_degree(reduced):
    print(f"Polynomial degree: {get_degree(reduced)}")


def display_complex(z):
    z = complex(z)
    real = round(z.real, PRECISION)
    imag = round(z.imag, PRECISION)
    if real.is_integer() and imag.is_integer():
        real = int(real)
        imag = int(imag)
    if real and imag:
        print(f"{real}{imag:+}i")
    elif real:
        print(f"{real}")
    elif imag:
        print(f"{imag}i")
    else:
        print("0")


def display_second_degree(a, b, c):
    discriminant = b**2 - 4 * a * c
    a2 = 2 * a
    x1 = (-b - discriminant**0.5) / a2
    x2 = (-b + discriminant**0.5) / a2
    if discriminant == 0:
        print("Discriminant zero, the solution of multiplicity 2 is:")
        display_complex(x1)
    else:
        sign = "negative" if discriminant < 0 else "positive"
        print(f"Discriminant is strictly {sign}, the two solutions are:")
        display_complex(x1)
        display_complex(x2)


def display_solutions(reduced):
    a, b, c = (
        float(reduced.get(2, 0)),
        float(reduced.get(1, 0)),
        float(reduced.get(0, 0)),
    )
    degree = get_degree(reduced)
    if degree == -1:
        print("There are infinitely many solutions.")
    elif degree == 0:
        print("There are no solutions.")
    elif degree == 1:
        print("The solution is:")
        display_complex(-c / b)
    elif degree == 2:
        display_second_degree(a, b, c)
    else:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
