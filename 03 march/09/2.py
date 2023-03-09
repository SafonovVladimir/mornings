from collections.abc import Iterable


def last(*args) -> None:
    if isinstance(args[-1], Iterable) and len(args[-1]) != 0:
        if isinstance(args[-1], (list, tuple, str)):
            return args[-1][-1]
    return args[-1]


print(last([1, 2, 3, 4]))  # == 4
print(last("xyz"))  # == "z"
print(last(1, 2, 3, 4))  # == 4
print(last(True, "qwerty", 56, []))  # == []
