def find_unknown_number(first: int, second: int, third: int) -> int:
    unknown_number = 0
    while True:
        unknown_number += 1
        if unknown_number % 3 == first and unknown_number % 5 == second and unknown_number % 7 == third:
            return unknown_number



print(find_unknown_number(2, 3, 2))  # повертає 23 | 23 % 3 = 2, 23 % 5 = 3, 23 % 7 = 2
print(find_unknown_number(1, 2, 3))  # повертає 52 | 52 % 3 = 1, 52 % 5 = 2, 52 % 7 = 3
print(find_unknown_number(1, 3, 5))  # повертає 103
print(find_unknown_number(1, 1, 1))  # повертає 1
print(find_unknown_number(0, 0, 0))  # повертає 105
