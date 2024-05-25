from src.print_solutions import print_solutions
from src.parse_equation import parse_equation
from src.utils import ft_assert, get_degree
import sys


def print_reduced_form(reduced):
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


if __name__ == "__main__":
    ft_assert(len(sys.argv) == 2, f"Usage: python {sys.argv[0]} <equation>")
    reduced = parse_equation(sys.argv[1])
    print_reduced_form(reduced)
    print(f"Polynomial degree: {get_degree(reduced)}")
    print_solutions(reduced)
