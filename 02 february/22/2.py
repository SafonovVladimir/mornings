import math


def you_are_a_square(number: int) -> bool:
    return number > -1 and number == math.isqrt(number) ** 2

print(you_are_a_square(-1))# is False # no square root from the negative number
print(you_are_a_square(0))# is True # square root of 0 is 0
print(you_are_a_square(1))# is True # square root of 1 is 1
print(you_are_a_square(25))# is True # square root of 25 is 5
print(you_are_a_square(40))# is False # square root of 40 is not an integer
