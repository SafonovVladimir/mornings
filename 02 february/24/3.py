def list_comparator(first: list, second: list) -> int:
    # count = 0
    # for elem in first:
    #     if elem in second:
    #         count += 1
    print(set(first).intersection(second))
    # return sum(1 for elem in first if elem in second)


print(list_comparator(first=[True, 3, 9, 11, 15], second=[True, 3, 11]))# == 3
print(list_comparator(first=['Erlang', 'JavaScript'], second=['Go', 'C++', 'Python']))# == 0

