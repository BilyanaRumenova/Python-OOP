from itertools import permutations


def possible_permutations(sequence):
    for per in permutations(sequence):
        yield list(per)
