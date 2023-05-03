import math

from collections import Counter


def hasGroupsSizeX(deck: list[int]) -> bool:
    deck_dict = Counter(deck)
    result = math.gcd(*deck_dict.values())

    if result < 2:
        return False
    return True


# deck = [1, 2, 3, 4, 4, 3, 2, 1]
# deck = [1, 1, 1, 2, 2, 2, 3, 3]
deck = [0, 0, 0, 0, 0, 1, 1, 2, 3, 4]

print(hasGroupsSizeX(deck))
