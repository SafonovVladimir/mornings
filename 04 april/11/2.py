from itertools import permutations, chain


def max_sub_list(nums: list[int]) -> int:

    if len(nums) == 1:
        return sum(nums)

    max_sum = current = 0

    for num in nums:
        current += num
        if current < 0:
            current = 0

        if max_sum < current:
            max_sum = current

    return max_sum


# print(max_sub_list([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # повертає 6 - [4, -1, 2, 1] має найбільшу суму = 6.
print(max_sub_list([1]))  # повертає 1
print(max_sub_list([-1]))  # повертає 1
# print(max_sub_list([5, 4, -1, 7, 8]))  # повертає 23
