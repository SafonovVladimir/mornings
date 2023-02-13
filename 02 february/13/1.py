from functools import reduce
from typing import Callable


def composition(first_function: Callable, second_function: Callable) -> Callable:
    return lambda *args: first_function(second_function(*args))


# "Композиція функцій" – це застосування однієї функції до результатів іншої:
# first_function(input) = 2 * (input) + 3
# second_function(input) = (input) ** 2
# second_function(first_function(x)) - Спочатку ми застосовуємо first_function, потім застосовуємо second_function до цього результату:
# x -> 2 * (input) + 3 == 2x + 3 -> (input) ** 2 == (2x + 3) ** 2
# second_function(first_function(x)) # повертає (2x + 3) ** 2


first_function = lambda a: 2 * a + 3
second_function = lambda a: a ** 2
print(composition(first_function, second_function)(2)) # повертає 11

first_function = lambda a: 2 * a + 3
second_function = lambda a, b: a + b
print(composition(first_function, second_function)(2, 3)) # повертає 13
