from typing import Union


def trotter(number: int) -> Union[int, str]:
    start = number
    numbers = "0123456789"
    result_list = []

    if number == 0:
        return "INSOMNIA"

    while True:
        for i in list(str(number)):
            result_list.append(i)

        if "".join(sorted(set(result_list))) == numbers:
            return number
        else:
            number += start




# print(trotter(1692)) # повертає 5076
# print(trotter(2)) # повертає 90
# print(trotter(7)) # повертає 70
print(trotter(1234567890)) # повертає 70
print(trotter(0)) # повертає 70



