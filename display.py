from math import sqrt
from utils import get_degree


PRECISION = 6


def display_reduced_form(reduced):
    line = ["Reduced form:"]
    if not reduced:
        reduced[0] = 0
    for p in range(max(reduced.keys()) + 1):
        m = reduced.get(p, 0)
        if p != 0:
            line.append("-" if m < 0 else "+")
        line.append(f"{abs(m)} * X^{p}")
    line.append("=")
    line.append("0")
    print(*line)


def display_polynomial_degree(reduced):
    print(f"Polynomial degree: {get_degree(reduced)}")


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
        print(round(-c / b, PRECISION))
    elif degree == 2:
        discriminant = b**2 - 4 * a * c
        a2 = 2 * a
        if discriminant < 0:
            print("Discriminant is strictly negative, the two solutions are:")
            real = round(-b / a2, PRECISION)
            imag = round(sqrt(-discriminant) / a2, PRECISION)
            print(f"{real} + {imag}i")
            print(f"{real} - {imag}i")
        elif discriminant > 0:
            print("Discriminant is strictly positive, the two solutions are:")
            print(round((-b - sqrt(discriminant)) / a2, PRECISION))
            print(round((-b + sqrt(discriminant)) / a2, PRECISION))
        else:
            print("Discriminant zero, the solutions of multiplicity 2 is:")
            print(round(-b / a2, PRECISION))
    else:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
