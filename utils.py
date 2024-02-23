import sys


def ft_assert(check, message):
    if not check:
        print(message)
        sys.exit(1)


def get_degree(reduced):
    return max(reduced.keys(), default=-1)
