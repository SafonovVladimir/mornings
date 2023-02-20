import math


def product_of_maximum(num_list: list, number: int) -> int:
    return math.prod(sorted(num_list)[-number:])


print(product_of_maximum(num_list=[4, 3, 5], number=2))  # == 20
print(product_of_maximum(num_list=[3, 3, 4], number=3))  # == 20

print(product_of_maximum(num_list=[-2, 0, 2], number=1))  # == 2
