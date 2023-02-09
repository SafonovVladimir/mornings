from collections import Counter


def single_number(num_list: list) -> int:
    counter_num = Counter(num_list)
    for key, value in counter_num.items():
        if value == 1:
            return key


print(single_number([2,2,1]))# == 1

print(single_number([4,1,2,1,2]))# == 4
