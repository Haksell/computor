from display import display_polynomial_degree, display_reduced_form, display_solutions
from parse_equation import parse_equation
import sys
from utils import ft_assert


if __name__ == "__main__":
    ft_assert(len(sys.argv) == 2, f"Usage: python {sys.argv[0]} <equation>")
    reduced = parse_equation(sys.argv[1])
    display_reduced_form(reduced)
    # display_polynomial_degree(reduced)
    # display_solutions(reduced)
