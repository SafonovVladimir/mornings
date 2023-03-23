from typing import Callable, Any
from math import floor


def zero(operation: Callable = None) -> int:
    if operation is None:
        return 0
    else:
        return operation(0)


def one(operation: Callable = None) -> int:
    if operation is None:
        return 1
    else:
        return operation(1)


def two(operation: Callable = None) -> int:
    if operation is None:
        return 2
    else:
        return operation(2)


def three(operation: Callable = None) -> int:
    if operation is None:
        return 3
    else:
        return operation(3)


def four(operation: Callable = None) -> int:
    if operation is None:
        return 4
    else:
        return operation(4)


def five(operation: Callable = None) -> int:
    if operation is None:
        return 5
    else:
        return operation(5)


def six(operation: Callable = None) -> int:
    if operation is None:
        return 6
    else:
        return operation(6)


def seven(operation: Callable = None) -> int:
    if operation is None:
        return 7
    else:
        return operation(7)


def eight(operation: Callable = None) -> int:
    if operation is None:
        return 8
    else:
        return operation(8)


def nine(operation: Callable = None) -> int:
    if operation is None:
        return 9
    else:
        return operation(9)


def plus(number: int) -> Any:
    return lambda x: x + number


def minus(number: int) -> Any:
    return lambda x: x - number


def times(number: int) -> Any:
    return lambda x: x * number


def divided_by(number: int) -> Any:
    return lambda x: floor(x / number)
