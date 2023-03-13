import datetime
# import heapq
from random import randint as rand


def volodymyr(nums: list, n: int) -> list:
    sort_min_set = set(sorted(nums)[:n])
    return [i for i in nums if i in sort_min_set][:n]

    # for i in sort_min_list:
    #     nums_dict[i] = sort_min_list.index(i)
    #
    # print(nums_dict)
    # for i in sort_min_list:
    #     result.append(nums.pop(nums.index(i)))
    # print(nums)
        # result.append(heapq.heappop(nums))
    # for i in sort_min_list:
    #     print(heapq.heappush(nums, i))

    # return [i for i in nums if i in heapq.nsmallest(n, nums)[:n]][:n]

def roman(nums: list, n: int) -> list:
    min_nums = sorted(nums)[:n]
    result = []
    lowest = min_nums[-1]
    for num in nums:
        if num <= lowest:
            result.append(num)
            if len(result) + 1 > n:
                break

    return result

def solution(nums, n):
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
    return result_list


random_nums = [rand(1, 51) for _ in range(20000000)]
length = len(random_nums) // 4
n = rand(length, length * 2)

start_time = datetime.datetime.now()
solution(random_nums, n)
end_time = datetime.datetime.now()
print("Mentor's solution: ", end_time - start_time)

start_time1 = datetime.datetime.now()
volodymyr(random_nums, n)
end_time1 = datetime.datetime.now()
print("My solution: ", end_time1 - start_time1)

start_time1 = datetime.datetime.now()
roman(random_nums, n)
end_time1 = datetime.datetime.now()
print("Roman's solution: ", end_time1 - start_time1)

start_time = datetime.datetime.now()
solution(random_nums, n)
end_time = datetime.datetime.now()
print("Mentor's solution: ", end_time - start_time)

start_time1 = datetime.datetime.now()
volodymyr(random_nums, n)
end_time1 = datetime.datetime.now()
print("My solution: ", end_time1 - start_time1)

start_time1 = datetime.datetime.now()
roman(random_nums, n)
end_time1 = datetime.datetime.now()
print("Roman's solution: ", end_time1 - start_time1)

start_time = datetime.datetime.now()
solution(random_nums, n)
end_time = datetime.datetime.now()
print("Mentor's solution: ", end_time - start_time)

start_time1 = datetime.datetime.now()
volodymyr(random_nums, n)
end_time1 = datetime.datetime.now()
print("My solution: ", end_time1 - start_time1)

start_time1 = datetime.datetime.now()
roman(random_nums, n)
end_time1 = datetime.datetime.now()
print("Roman's solution: ", end_time1 - start_time1)


# assert (
#         performant_smallest(random_nums, n) == solution(random_nums, n)
#         or "Incorrect output list"
# )

# print(performant_smallest([1, 2, 3, 4, 5], 3))#  # повертає [1, 2, 3]
# print(performant_smallest([5, 4, 3, 2, 1], 3))#  # повертає [3, 2, 1]
# print(performant_smallest([1, 2, 4, 1, 2], 3))#  # повертає [1, 2, 1]
