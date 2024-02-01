import itertools


def permutations(line: str) -> list:
    return [''.join(elem) for elem in set(itertools.permutations(line))]
