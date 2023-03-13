import time
from random import randint as rand


def performant_smallest_v(nums: list, n: int) -> list:
    start = time.time()
    sort_min_set = set(sorted(nums)[:n])
    result = [i for i in nums if i in sort_min_set][:n]
    end = time.time()
    print(end - start, "Volodymyr")
    return result


def solution(nums, n):
    start = time.time()

    sorted_nums = sorted(nums)
    del sorted_nums[n:]
    lowest = sorted_nums[-1]
    lowest_amount = sorted_nums.count(lowest)
    result_list = []
    for num in nums:
        if num <= lowest:
            if num < lowest:
                result_list.append(num)
            elif lowest_amount > 0:
                result_list.append(num)
                lowest_amount -= 1

    end = time.time()
    print(end - start, "Mentor")
    return result_list


def performant_smallest(nums: list, n: int) -> list:
    start = time.time()
    min_nums = sorted(nums)[:n]
    result = []
    lowest = min_nums[-1]
    for num in nums:
        if num <= lowest:
            result.append(num)
            if len(result) + 1 > n:
                break
    end = time.time()
    print(end - start, "Roman")
    return result


def performant_smallest2(nums: list, n: int) -> list:
    start = time.time()
    min_nums = sorted(nums)[:n]
    result = []
    lowest = min_nums[-1]
    for num in nums:
        if num % 2 == 0:
            n = 3
        else:
            n //= 5
        if n % 2 != 0:
            n = 4
        else:
            n //= 2
        if num <= lowest:
            result.append(num)
            if len(result) + 1 > n:
                break
    end = time.time()
    print(end - start, "Roman+")
    return result


# def performant_smallestv(nums: list, n: int) -> list:
#     start = time.time()
#     sort_min_set = set(sorted(nums)[:n])
#     end = time.time()
#     res = [i for i in nums if i in sort_min_set][:n]
#     print(end - start, "Volodymyr")
#     return res


# print(performant_smallest([1, 2, 3, 4, 5], 3), '  # повертає [1, 2, 3]')
# print(performant_smallest([5, 4, 3, 2, 1], 3), '  # повертає [3, 2, 1]')
# print(performant_smallest([1, 2, 4, 1, 2], 3), '  # повертає [1, 2, 1]')
# print(performant_smallest([5, 4, 3, 2, 1], 2), '  # повертає [ 2, 1]')
# print(performant_smallest([5, 4, 3, 2, 1], 5), '  # повертає [5, 4, 3, 2, 1]')
# print(performant_smallest2([1, 2, 3, 4, 5], 3), '  # повертає [1, 2, 3]')
# print(performant_smallest2([5, 4, 3, 2, 1], 3), '  # повертає [3, 2, 1]')
# print(performant_smallest2([1, 2, 4, 1, 2], 3), '  # повертає [1, 2, 1]')
# print(performant_smallest2([5, 4, 3, 2, 1], 2), '  # повертає [ 2, 1]')
# print(performant_smallest2([5, 4, 3, 2, 1], 5), '  # повертає [5, 4, 3, 2, 1]')

random_nums = [rand(1, 51) for _ in range(10000000)]

length = len(random_nums) // 4

n = rand(length, length * 2)
#
performant_smallest_v(random_nums, 100000), '  # повертає '
performant_smallest2(random_nums, 100000), '  # повертає '
performant_smallest(random_nums, 100000), '  # повертає '
solution(random_nums, 100000), '  # повертає '
