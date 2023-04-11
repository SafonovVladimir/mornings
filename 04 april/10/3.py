def find_number(start: int, stop: int, string: str) -> list:
    range_list = list("".join([str(num) for num in range(start, stop + 1)]))
    print(range_list)

    for char in list(string):
        range_list.remove(char)
    sorted_numbers = sorted(range_list)
    print(sorted_numbers)
    print(list(string))

    return [num for num in range(start, stop + 1) if sorted(list(str(num))) == sorted_numbers]


print(find_number(1, 21,
                  "2198765123416171890101112131415"))  # повертає [12, 21] - ти не зможеш сказати, 21 це або 12,
# тому краще повертати всі можливі значення в списку.
# print(find_number(5, 10, "578910"))  # повертає [6]
