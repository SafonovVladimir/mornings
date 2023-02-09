from collections import Counter


def simple_fun(num_list: list) -> int:
    count_nums = Counter(num_list)
    x = 0
    y = 0
    for key, value in count_nums.items():
        if value == 1:
            x = key
        if value == 2:
            y = key
    return x ** 2 * y



print(simple_fun([1, 1, 1, 2, 2, 3]))# == 18 # 3 * 3 * 2 = 18

print(simple_fun([6, 5, 4, 100, 6, 5, 4, 100, 6, 5, 4, 200]))# == 4000000 # 200 * 200 * 100 = 4000000
