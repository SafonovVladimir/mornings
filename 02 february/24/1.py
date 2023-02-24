from collections import Counter


def odd_ones_out(numbers: list) -> list:
    return [num for num in numbers if numbers.count(num) % 2 == 0]

print(odd_ones_out([26, 23, 24, 17, 23, 24, 23, 26]))# == [26, 24, 24, 26]
print(odd_ones_out([1, 2, 3, 1, 3, 3]))# == [1, 1]
print(odd_ones_out([1, 2, 3]))# == []
