from typing import Callable


def find_function(list_with_function: list, list_to_filter: list) -> list:
    for item in list_with_function:
        if isinstance(item, Callable):
            return [i for i in list_to_filter if item(i)]




list_with_function = [lambda a: a% 2 == 0, 9, 3, 1, 0]
list_to_filter = [1, 2, 3, 4]
print(find_function(list_with_function, list_to_filter))  # повертає [2, 4]

list_with_function = [9, 3, lambda а: а % 2, 1, 0]
list_to_filter = [1, 2, 3, 4]
print(find_function(list_with_function, list_to_filter))  # повертає [1, 3]

list_with_function = [9, 3, lambda a: a % 13 == 0, 1, 0]
list_to_filter = [1, 2, 3, 4]
print(find_function(list_with_function, list_to_filter))  # повертає []
