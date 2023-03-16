from typing import Callable


def add(a: int) -> None:
    def inner(b: int) -> int:
        return a + b

    return inner


def subtract(a: int) -> None:
    def inner(b: int) -> int:
        return a - b

    return inner


def multiply(a: int) -> None:
    def inner(b: int) -> int:
        return a * b

    return inner


def apply(func: Callable) -> None:
    return func

# print(add(3)(4))  # повертає 7
# print(subtract(3)(4))  # повертає -1
# print(multiply(3)(4))  # повертає 12

print(apply(add)(3)(4))  # повертає 7
print(apply(subtract)(3)(4))  # повертає -1
print(apply(multiply)(3)(4))  # повертає 12
