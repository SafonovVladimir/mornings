def maximum_product(num_list: list) -> int:
    # result = []
    # for i in range(len(num_list) - 1):
    #     result.append(num_list[i] * num_list[i + 1])
    return max(
        (num_list[i] * num_list[i + 1]) for i in range(len(num_list) - 1))


print(maximum_product([1, 2, 3]))# == 6
print(maximum_product([-5, 0, 3, 5, 2]))# == 21
