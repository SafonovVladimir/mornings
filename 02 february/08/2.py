def sum_of_two_lowest(num_list: list) -> int:
    num_list.sort()
    return sum(num_list[:2])

print(sum_of_two_lowest([19, 5, 42, 2, 77]))# == 7
print(sum_of_two_lowest([10, 343445353, 3453445, 3453545353453]))# == 3453455
