from collections import Counter


def find_all_pairs(num_list: list) -> int:
    if len(num_list) <= 1:
        return 0
    return sum([value // 2 for value in Counter(num_list).values()])


print(find_all_pairs([0, 0, 0, 0]))# == 2

print(find_all_pairs([1, 2, 5, 6, 5, 2]))# == 2

print(find_all_pairs([1, 2, 2, 20, 6, 20, 2, 6, 2]))# == 4


