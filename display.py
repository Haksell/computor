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
    print(
        f"{real}{imag:+}i"
        if real and imag
        else f"{real}"
        if real
        else f"{imag}i"
        if imag
        else "0"
    )


def display_second_degree(reduced):
    a, b, c = (reduced.get(2, 0), reduced.get(1, 0), reduced.get(0, 0))
    discriminant = b**2 - 4 * a * c
    x1 = (-b - discriminant**0.5) / (2 * a)
    x2 = (-b + discriminant**0.5) / (2 * a)
    if discriminant == 0:
        print("Discriminant zero, the solution of multiplicity 2 is:")
        display_complex(x1)
    else:
        sign = "negative" if discriminant < 0 else "positive"
        print(f"Discriminant is strictly {sign}, the two solutions are:")
        display_complex(x1)
        display_complex(x2)


# https://stackoverflow.com/a/74198367/10793260
def display_third_degree(reduced):
    def gen_cbrt(polynomial):
        solution = set()
        root1 = polynomial ** (1 / 3)
        root2 = (polynomial ** (1 / 3)) * (-1 / 2 + (3**0.5 * 1j) / 2)
        root3 = (polynomial ** (1 / 3)) * (-1 / 2 - (3**0.5 * 1j) / 2)
        solution.update({root1, root2, root3})
        return solution

    def cardano(a, b, c, d):
        solutions = set()
        p = (3 * a * c - b**2) / (3 * a**2)
        q = (2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / (27 * a**3)
        alpha = gen_cbrt(-q / 2 + ((q / 2) ** 2 + (p / 3) ** 3) ** 0.5)
        beta = gen_cbrt(-q / 2 - ((q / 2) ** 2 + (p / 3) ** 3) ** 0.5)
        for i in alpha:
            for j in beta:
                if abs((i * j) + p / 3) <= 0.00001:
                    z = i + j - b / (3 * a)
                    solutions.add(
                        complex(round(z.real, PRECISION), round(z.imag, PRECISION))
                    )
        return solutions

    solutions = cardano(*[float(reduced.get(i, 0)) for i in [3, 2, 1, 0]])
    print(f"There are {len(solutions)} solutions:")
    for solution in solutions:
        display_complex(solution)


def display_solutions(reduced):
    degree = get_degree(reduced)
    reduced = {p: float(a) for p, a in reduced.items()}
    if degree == -1:
        print("There are infinitely many solutions.")
    elif degree == 0:
        print("There are no solutions.")
    elif degree == 1:
        print("The solution is:")
        display_complex(-reduced.get(0, 0) / reduced.get(1, 0))
    elif degree == 2:
        display_second_degree(reduced)
    elif degree == 3:
        display_third_degree(reduced)
    else:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
