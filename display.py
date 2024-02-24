from fractions import Fraction
from utils import get_degree, sqrt_fraction


PRECISION = 6


def display_reduced_form(reduced):
    line = ["Reduced form:"]
    if len(reduced) <= 1:
        line.append(reduced[0] if reduced else 0)
    else:
        for d, v in enumerate(reduced):
            if d != 0:
                line.append("-" if v < 0 else "+")
            line.append(f"{v if d==0 else abs(v)} * X^{d}")
    line.append("=")
    line.append("0")
    print(*line)


def display_polynomial_degree(reduced):
    print(f"Polynomial degree: {get_degree(reduced)}")


def format_real(x):
    assert isinstance(x, float) or isinstance(x, Fraction)
    rounded = str(round(float(x), PRECISION))
    if x.is_integer():
        return str(x)
    elif isinstance(x, float):
        return rounded
    else:
        return f"{x} ({rounded})"


def format_complex(z):
    z = complex(z)
    real = round(z.real, PRECISION)
    imag = round(z.imag, PRECISION)
    if real.is_integer() and imag.is_integer():
        real = int(real)
        imag = int(imag)
    return f"{real}{imag:+}i" if real and imag else f"{imag}i" if imag else str(z)


def display_first_degree(reduced):
    print(f"The solution is {format_real(-reduced[0] / reduced[1])}")


def display_second_degree(reduced):
    c, b, a = reduced
    discriminant = b * b - 4 * a * c
    sqrt_discriminant = sqrt_fraction(discriminant)
    x1 = (-b - sqrt_discriminant) / (2 * a)
    x2 = (-b + sqrt_discriminant) / (2 * a)
    if discriminant > 0:
        print("Discriminant is strictly positive, the two solutions are:")
        print(format_real(x1))
        print(format_real(x2))
    elif discriminant < 0:
        print("Discriminant is strictly negative, the two solutions are:")
        print(format_complex(x1))
        print(format_complex(x2))
    else:
        print(
            f"Discriminant is zero, the solution of multiplicity 2 is {format_real(x1)}"
        )


# https://stackoverflow.com/a/74198367/10793260
def display_third_degree(reduced):
    def cube_roots(z):
        root1 = z ** (1 / 3)
        sqrt3j2 = (3**0.5 * 1j) / 2
        return {root1, root1 * (-0.5 + sqrt3j2), root1 * (-0.5 - sqrt3j2)}

    def cardano(a, b, c, d):
        solutions = set()
        p = (3 * a * c - b**2) / (3 * a**2)
        q = (2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / (27 * a**3)
        alpha = cube_roots(-q / 2 + ((q / 2) ** 2 + (p / 3) ** 3) ** 0.5)
        beta = cube_roots(-q / 2 - ((q / 2) ** 2 + (p / 3) ** 3) ** 0.5)
        for i in alpha:
            for j in beta:
                if abs((i * j) + p / 3) <= 1e-6:
                    z = i + j - b / (3 * a)
                    solutions.add(
                        complex(round(z.real, PRECISION), round(z.imag, PRECISION))
                    )
        return solutions

    solutions = cardano(*[float(reduced.get(i, 0)) for i in [3, 2, 1, 0]])
    print(f"There are {len(solutions)} solutions:")
    for solution in solutions:
        print(format_complex(solution))


def display_solutions(reduced):
    degree = get_degree(reduced)
    reduced = list(map(Fraction, reduced))
    if degree == -1:
        print("There are infinitely many solutions.")
    elif degree == 0:
        print("There are no solutions.")
    elif degree == 1:
        display_first_degree(reduced)
    elif degree == 2:
        display_second_degree(reduced)
    # elif degree == 3:
    #     display_third_degree(reduced)
    else:
        print("The polynomial degree is strictly greater than 3, I can't solve.")
