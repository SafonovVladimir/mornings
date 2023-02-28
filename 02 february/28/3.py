def remove_duplicates(sorted_numbers: list) -> int:
    set_num = set(sorted_numbers)
    sorted_numbers.clear()
    for num in set_num:
        sorted_numbers.append(num)

    sorted_numbers.sort()
    return sorted_numbers

# print(remove_duplicates([1, 1, 2])) # повертає 2 - довжина зміненого sorted_numbers [1, 2]
# print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])) # повертає 5 - довжина зміненого sorted_numbers [0,1,2,3,4]
# print(remove_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) # повертає 1
print(remove_duplicates([0, 1, 4, -23, -5, -2])) # повертає 1


