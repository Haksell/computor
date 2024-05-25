from src.utils import sqrt_fraction


def solve_second_degree(reduced):
    c, b, a = reduced
    assert a != 0
    discriminant = b * b - 4 * a * c
    sqrt_discriminant = sqrt_fraction(discriminant)
    x1 = (-b - sqrt_discriminant) / (2 * a)
    x2 = (-b + sqrt_discriminant) / (2 * a)
    return discriminant, (x1, x2)


CUBE_ROOT_OF_UNITY = -0.5 + 0.8660254037844386j


# https://youtu.be/N-KXStupwsc
# https://en.wikipedia.org/wiki/Cubic_equation#General_cubic_formula
def solve_third_degree(reduced):
    def find_solution(C):
        return -(b + C + (delta0 / C if C else 0)) / (3 * a)

    d, c, b, a = reduced
    assert a != 0
    discriminant = (
        18 * a * b * c * d
        - 4 * b * b * b * d
        + b * b * c * c
        - 4 * a * c * c * c
        - 27 * a * a * d * d
    )  # https://en.wikipedia.org/wiki/Cubic_equation#Discriminant_and_nature_of_the_roots
    delta0 = b * b - 3 * a * c
    delta1 = 2 * b * b * b - 9 * a * b * c + 27 * a * a * d
    C = ((delta1 + (delta1 * delta1 - 4 * delta0**3) ** 0.5) / 2) ** (1 / 3)
    if C == 0:
        C = ((delta1 - (delta1 * delta1 - 4 * delta0**3) ** 0.5) / 2) ** (1 / 3)
    return discriminant, (
        find_solution(C),
        find_solution(C * CUBE_ROOT_OF_UNITY),
        find_solution(C * CUBE_ROOT_OF_UNITY.conjugate()),
    )
