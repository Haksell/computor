import sys


def main(equation):
    print(equation)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <equation>")
        print(
            f'Example: python {sys.argv[0]} "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"'
        )
    else:
        main(sys.argv[1])
